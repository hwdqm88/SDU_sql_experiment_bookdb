from PySide2.QtWidgets import QWidget, QMessageBox
from userWidget_ui import Ui_Widget
from userIntoWidget import userIntoWidget
from lib.share import SI
import pymysql

class userWidget(QWidget):
    def __init__(self):
        super(userWidget, self).__init__()
        self.ui=Ui_Widget()
        self.ui.setupUi(self)
        self.ui.pushButton_login.clicked.connect(self.intoUser)
        self.ui.lineEdit_password.returnPressed.connect(self.intoUser)

    def intoUser(self):
        try:
            con = pymysql.connect(host='localhost',user='root',password='root',database='bookdb',port=3306)
            cursor = con.cursor()
            sql='''
                select * from user;
            '''
            cursor.execute(sql)
            data = cursor.fetchall()
            self.__flag = False
            for eachAdminMessage in data:
                if(eachAdminMessage[1]==self.ui.lineEdit_name.text() and eachAdminMessage[2]==self.ui.lineEdit_password.text()):
                    self.__flag = True
                    userId=eachAdminMessage[0]
                    break
            cursor.close()
            con.close()
            if(self.__flag==False):
                QMessageBox.warning(self, '登陆失败', '账号或密码错误')
                return
        except:
            QMessageBox.warning(self,'登陆失败','数据库错误，请检查数据库')
            return
        SI.userIntoWidget = userIntoWidget(userId)
        SI.userIntoWidget.show()
        self.ui.lineEdit_password.setText('')
        self.hide()
