from PySide2.QtWidgets import QWidget, QMessageBox
from bookBorrowWidget_ui import Ui_Widget
import pymysql

class bookBorrowWidget(QWidget):
    def __init__(self,bookId):
        super(bookBorrowWidget, self).__init__()
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.__bookId=bookId
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
        self.ui.pushButton_add.clicked.connect(self.borrow)

    def borrow(self):
        if(self.ui.comboBox_borrowed.currentIndex()==1):
            QMessageBox.warning(self,'借阅失败','图书已被借出')
            return
        con = pymysql.connect(host='localhost', user='root', password='root', database='bookdb',
                              port=3306)
        cursor = con.cursor()
        sql = '''
            update `book` set `borrowed`=1 where `id`=%s;
        '''
        cursor.execute(sql, (self.__bookId))
        con.commit()
        cursor.close()
        con.close()
        QMessageBox.about(self,'成功','借阅成功')