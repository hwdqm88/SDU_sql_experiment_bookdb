from PySide2.QtWidgets import QWidget, QMessageBox
from adminIntoWidget_ui import Ui_Widget
import pymysql
from userEditWidget import userEditWidget
from userCreateWidget import userCreateWidget
from bookEditWidget import bookEditWidget
from bookCreateWidget import bookCreateWidget
from lib.share import SI

class adminIntoWidget(QWidget):
    def __init__(self):
        super(adminIntoWidget, self).__init__()
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        con = pymysql.connect(host='localhost', user='root', password='root', database='bookdb',
                              port=3306)
        cursor = con.cursor()
        sql = '''
            select * from `role`;
        '''
        cursor.execute(sql)
        roleInformation = cursor.fetchall()
        self.ui.lineEdit_day_teacher.setText(str(roleInformation[0][3]))
        self.ui.lineEdit_day_graduate.setText(str(roleInformation[1][3]))
        self.ui.lineEdit_day_under.setText(str(roleInformation[2][3]))
        self.ui.lineEdit_day_other.setText(str(roleInformation[3][3]))
        cursor.close()
        con.close()

        self.ui.pushButton_admin_change.clicked.connect(self.changeAdminPassword)
        self.ui.pushButton_admin_add.clicked.connect(self.setNewAdmin)
        self.ui.pushButton_user_find.clicked.connect(self.findUser)
        self.ui.pushButton_user_add.clicked.connect(self.createUser)
        self.ui.pushButton_book_find.clicked.connect(self.findBook)
        self.ui.pushButton_book_add.clicked.connect(self.createBook)
        self.ui.pushButton_day_set.clicked.connect(self.setDay)

    def changeAdminPassword(self):
        try:
            con = pymysql.connect(host='localhost', user='root', password='root', database='bookdb',
                                  port=3306)
            cursor = con.cursor()
            sql = '''
                select * from `administor` where `name`=%s;
            '''
            cursor.execute(sql, (self.ui.lineEdit_admin_name.text()))
            if (len(cursor.fetchall()) == 0):
                cursor.close()
                raise Exception
            sql = '''
                update `administor` set `password`=%s where `name`=%s;
            '''
            cursor.execute(sql, (self.ui.lineEdit_admin_password.text(), self.ui.lineEdit_admin_name.text()))
            con.commit()
            cursor.close()
            con.close()
            QMessageBox.about(self, '成功', '密码修改成功')
        except:
            QMessageBox.critical(self, '错误', '用户名错误，请重新输入目标用户名')
            con.close()
            return

    def setNewAdmin(self):
        try:
            con = pymysql.connect(host='localhost', user='root', password='root', database='bookdb',
                                  port=3306)
            cursor = con.cursor()
            sql = '''
                select * from `administor` where `name`=%s;
            '''
            cursor.execute(sql, (self.ui.lineEdit_admin_name.text()))
            if (len(cursor.fetchall()) > 0):
                cursor.close()
                raise Exception
            sql = '''
                insert into `administor`(`name`,`password`) values(%s,%s);
            '''
            cursor.execute(sql, (self.ui.lineEdit_admin_name.text(), self.ui.lineEdit_admin_password.text()))
            con.commit()
            cursor.close()
            con.close()
            QMessageBox.about(self, '成功', '新增管理员成功')
        except:
            QMessageBox.critical(self, '错误', '管理员已存在')
            con.close()
            return

    def findUser(self):
        try:
            con = pymysql.connect(host='localhost', user='root', password='root', database='bookdb',
                                  port=3306)
            cursor = con.cursor()
            sql = '''
                select * from `user` where `user_name`=%s and `phone_number`=%s;
            '''
            cursor.execute(sql, (self.ui.lineEdit_user_name.text(), self.ui.lineEdit_user_tele.text()))
            userInformation = cursor.fetchone()
            if (userInformation == None):
                cursor.close()
                raise Exception
            cursor.close()
            con.close()
            SI.userEditWidget = userEditWidget(userInformation[0])
            SI.userEditWidget.show()

        except:
            QMessageBox.critical(self, '错误', '用户不存在')
            con.close()
            return

    def createUser(self):
        SI.userCreateWidget = userCreateWidget()
        SI.userCreateWidget.show()

    def findBook(self):
        try:
            con = pymysql.connect(host='localhost', user='root', password='root', database='bookdb',
                                  port=3306)
            cursor = con.cursor()
            sql = '''
                select * from `book` where `name`=%s;
            '''
            cursor.execute(sql, (self.ui.lineEdit_book_name.text()))
            userInformation = cursor.fetchone()
            if (userInformation == None):
                cursor.close()
                raise Exception
            cursor.close()
            con.close()
            SI.bookEditWidget = bookEditWidget(userInformation[0])
            SI.bookEditWidget.show()
        except:
            QMessageBox.critical(self, '错误', '图书不存在')
            con.close()
            return

    def createBook(self):
        SI.bookCreateWidget = bookCreateWidget()
        SI.bookCreateWidget.show()

    def setDay(self):
        con = pymysql.connect(host='localhost', user='root', password='root', database='bookdb',
                              port=3306)
        cursor = con.cursor()
        sql = '''
            update `role` set `max_day`=%s where `id`=1;
        '''
        cursor.execute(sql, (self.ui.lineEdit_day_teacher.text()))
        sql = '''
            update `role` set `max_day`=%s where `id`=2;
        '''
        cursor.execute(sql, (self.ui.lineEdit_day_graduate.text()))
        sql = '''
            update `role` set `max_day`=%s where `id`=3;
        '''
        cursor.execute(sql, (self.ui.lineEdit_day_under.text()))
        sql = '''
            update `role` set `max_day`=%s where `id`=4;
        '''
        cursor.execute(sql, (self.ui.lineEdit_day_other.text()))
        con.commit()
        cursor.close()
        con.close()
        QMessageBox.about(self,'成功','修改成功')