from PySide2.QtWidgets import QWidget,QMessageBox
from adminWidget_ui import Ui_Widget
from lib.share import SI
from adminIntoWidget import adminIntoWidget
import pymysql

class adminWidget(QWidget):
    def __init__(self):
        super(adminWidget, self).__init__()
        self.ui=Ui_Widget()
        self.ui.setupUi(self)
        self.ui.pushButton_login.clicked.connect(self.intoAdmin)
        self.ui.lineEdit_password.returnPressed.connect(self.intoAdmin)

    def intoAdmin(self):
        try:
            con = pymysql.connect(host='localhost',user='root',password='root',database='bookdb',port=3306)
            cursor = con.cursor()
            sql='''
                select * from administor;
            '''
            cursor.execute(sql)
            data = cursor.fetchall()
            self.__flag = False
            for eachAdminMessage in data:
                if(eachAdminMessage[1]==self.ui.lineEdit_name.text() and eachAdminMessage[2]==self.ui.lineEdit_password.text()):
                    self.__flag = True
                    break
            cursor.close()
            con.close()
            if(self.__flag==False):
                QMessageBox.warning(self, '登陆失败', '账号或密码错误')
                return
        except:
            QMessageBox.warning(self,'登陆失败','数据库错误，请检查数据库')
            return
        SI.adminIntoWidget = adminIntoWidget()
        SI.adminIntoWidget.show()
        self.ui.lineEdit_password.setText('')
        self.hide()