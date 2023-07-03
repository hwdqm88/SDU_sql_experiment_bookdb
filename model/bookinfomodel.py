from typing import Any
from PySide6.QtCore import QAbstractTableModel, QModelIndex, QPersistentModelIndex
from PySide6.QtCore import Qt
from database.connector import Connector
from lib.share import SI


class BookInfoModel(QAbstractTableModel):

    s_instance = None

    @staticmethod
    def getInstance():
        if BookInfoModel.s_instance is None:
            BookInfoModel.s_instance = BookInfoModel()
        return BookInfoModel.s_instance

    def __init__(self, parent=None):
        super().__init__(parent)
        self.__bookInfoList = []
        self.__headerList = ['标题', '作者', '出版日期', '出版社', '是否已借出', '借阅/归还']
        SI.g_bookInfoModel = self
        self.update()

    def headerData(self, section: int, orientation: Qt.Orientation, role: int = ...) -> Any:
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            if 0 <= section < len(self.__headerList):
                return self.__headerList[section]
        return super().headerData(section, orientation, role)

    def rowCount(self, parent: [QModelIndex, QPersistentModelIndex] = ...) -> int:
        return len(self.__bookInfoList)

    def columnCount(self, parent: [QModelIndex, QPersistentModelIndex] = ...) -> int:
        return len(self.__headerList)

    def data(self, index: [QModelIndex, QPersistentModelIndex], role: int = ...) -> Any:
        if not index.isValid():
            return None
        if role != Qt.ItemDataRole.DisplayRole:
            return None
        if 0 <= index.column() < len(self.__headerList) and 0 <= index.row() < len(self.__bookInfoList):
            return self.__bookInfoList[index.row()][index.column()]
        return None

    def sort(self, column: int, order: Qt.SortOrder = ...) -> None:
        self.__bookInfoList.sort(key=lambda row: row[column], reverse=order == Qt.SortOrder.DescendingOrder)
        self.dataChanged.emit(self.index(0, 0), self.index(len(self.__bookInfoList) - 1, len(self.__headerList) - 1))

    def update(self):
        self.beginResetModel()
        cursor = Connector.get_cursor()
        sql = 'SELECT b_name, author, publish_date, publish_name, borrowed, b_id FROM book'
        cursor.execute(sql)
        result = cursor.fetchall()
        self.__bookInfoList = []
        for row in result:
            self.__bookInfoList.append([row[0],
                                        row[1],
                                        row[2].strftime('%Y-%m-%d'),
                                        row[3],
                                        '否' if row[4] == 0 else '是',
                                        row[5]])
        self.endResetModel()
