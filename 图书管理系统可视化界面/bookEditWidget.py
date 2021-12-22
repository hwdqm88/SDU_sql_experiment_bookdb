from PySide2.QtWidgets import QWidget, QMessageBox
from bookEditWidget_ui import Ui_Widget
import pymysql

class bookEditWidget(QWidget):
    def __init__(self, bookId):
        super(bookEditWidget, self).__init__()
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.__bookId = bookId
        con = pymysql.connect(host='localhost', user='root', password='root', database='bookdb',
                              port=3306)
        cursor = con.cursor()
        sql = '''
            select * from `book` where `id`=%s;
        '''
        cursor.execute(sql, (bookId))
        bookInformation = cursor.fetchone()
        self.ui.comboBox_borrowed.setCurrentIndex(bookInformation[5])
        self.ui.lineEdit_name.setText(bookInformation[1])
        self.ui.lineEdit_author.setText(bookInformation[2])
        self.ui.lineEdit_date.setText(str(bookInformation[3]))
        self.ui.lineEdit_publish.setText(bookInformation[4])
        self.ui.lineEdit_price.setText(str(bookInformation[6]))
        self.ui.lineEdit_intro.setText(bookInformation[7])
        cursor.close()
        con.close()
        self.ui.pushButton_edit.clicked.connect(self.bookInformationChage)
        self.ui.pushButton_delete.clicked.connect(self.bookDelete)

    def bookInformationChage(self):
        try:
            con = pymysql.connect(host='localhost', user='root', password='root', database='bookdb',
                                  port=3306)
            cursor = con.cursor()
            sql = '''
                update `book` 
                set 
                    `name`=%s,
                    `author`=%s,
                    `publish_date`=%s,
                    `publish_name`=%s,
                    `borrowed`=%s,
                    `price`=%s,
                    `intro`=%s
                where
                    `id`=%s;
            '''
            infoTuple=(
                self.ui.lineEdit_name.text(),
                self.ui.lineEdit_author.text(),
                self.ui.lineEdit_date.text(),
                self.ui.lineEdit_publish.text(),
                self.ui.comboBox_borrowed.currentIndex(),
                float(self.ui.lineEdit_price.text()),
                self.ui.lineEdit_intro.text(),
                self.__bookId
            )
            cursor.execute(sql,infoTuple)
            con.commit()
            cursor.close()
            con.close()
            QMessageBox.about(self, '成功', '信息编辑成功')
        except:
            QMessageBox.critical(self, '错误', '信息输入有误')
            con.close()
            return

    def bookDelete(self):
        con = pymysql.connect(host='localhost', user='root', password='root', database='bookdb',
                              port=3306)
        cursor = con.cursor()
        sql = '''
            delete from `book` where `id`=%s;
        '''
        cursor.execute(sql, (self.__bookId))
        con.commit()
        cursor.close()
        con.close()
        QMessageBox.about(self, '成功', '图书删除成功')
        self.close()