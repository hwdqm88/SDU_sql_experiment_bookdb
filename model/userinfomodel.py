from typing import Any
from PySide6.QtCore import QAbstractTableModel, QModelIndex, QPersistentModelIndex
from PySide6.QtCore import Qt

import lib.share
from database.connector import Connector
from lib.share import SI


class UserInfoModel(QAbstractTableModel):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.__userInfo = [[0, 0, 0, 0, 0, 0, 0]]
        self.__headerList = ['帐号', '余额', '类别', '已借阅数量', '最大借阅数量', '最大借阅时长', '查看已借阅书籍']
        lib.share.SI.g_userInfoModel = self

    def headerData(self, section: int, orientation: Qt.Orientation, role: int = ...) -> Any:
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            if 0 <= section < len(self.__headerList):
                return self.__headerList[section]
        return super().headerData(section, orientation, role)

    def rowCount(self, parent: [QModelIndex, QPersistentModelIndex] = ...) -> int:
        return len(self.__userInfo)

    def columnCount(self, parent: [QModelIndex, QPersistentModelIndex] = ...) -> int:
        return len(self.__headerList)

    def data(self, index: [QModelIndex, QPersistentModelIndex], role: int = ...) -> Any:
        if not index.isValid():
            return None
        if role != Qt.ItemDataRole.DisplayRole:
            return None
        if 0 <= index.column() < len(self.__headerList) and 0 <= index.row() < len(self.__userInfo):
            return self.__userInfo[index.row()][index.column()]
        return None

    def update(self):
        cursor = Connector.get_cursor()
        sql = """
            SELECT u_name, balance, r_name, COUNT(b_id), max_number, max_day, u.u_id
            FROM user u
                     JOIN role r on r.r_id = u.r_id
                     LEFT JOIN borrow b on u.u_id = b.u_id
            WHERE u.u_id = %s;
        """
        cursor.execute(sql, (SI.g_userId))
        self.__userInfo = list(cursor.fetchall())
        self.dataChanged.emit(self.index(0, 0), self.index(len(self.__userInfo) - 1, len(self.__headerList) - 1))