from PySide2.QtWidgets import QWidget, QMessageBox
from userEditWidget_ui import Ui_Widget
import pymysql


class userEditWidget(QWidget):
    def __init__(self, userId):
        super(userEditWidget, self).__init__()
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.__userId=userId
        con = pymysql.connect(host='localhost', user='root', password='root', database='bookdb',
                              port=3306)
        cursor = con.cursor()
        sql = '''
            select * from `user` where `id`=%s;
        '''
        cursor.execute(sql, (userId))
        userInformation = cursor.fetchone()
        self.ui.comboBox_sex.setCurrentText(userInformation[3])
        self.ui.comboBox_role.setCurrentIndex(int(userInformation[6]) - 1)
        self.ui.lineEdit_name.setText(userInformation[1])
        self.ui.lineEdit_password.setText(userInformation[2])
        self.ui.lineEdit_balance.setText(str(userInformation[4]))
        self.ui.lineEdit_tele.setText(userInformation[5])
        self.ui.lineEdit_unit.setText(userInformation[7])
        cursor.close()
        con.close()
        self.ui.pushButton_edit.clicked.connect(self.userInformationChage)
        self.ui.pushButton_delete.clicked.connect(self.userDelete)

    def userInformationChage(self):
        try:
            con = pymysql.connect(host='localhost', user='root', password='root', database='bookdb',
                                  port=3306)
            cursor = con.cursor()
            sql = '''
                update `user` 
                set 
                    `user_name`=%s,
                    `password`=%s,
                    `sex`=%s,
                    `balance`=%s,
                    `phone_number`=%s,
                    `role_id`=%s,
                    `unit`=%s
                where
                    `id`=%s;
            '''
            infoTuple=(
                self.ui.lineEdit_name.text(),
                self.ui.lineEdit_password.text(),
                self.ui.comboBox_sex.currentText(),
                float(self.ui.lineEdit_balance.text()),
                self.ui.lineEdit_tele.text(),
                self.ui.comboBox_role.currentIndex()+1,
                self.ui.lineEdit_unit.text(),
                self.__userId
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

    def userDelete(self):
        con = pymysql.connect(host='localhost', user='root', password='root', database='bookdb',
                              port=3306)
        cursor = con.cursor()
        sql = '''
            delete from `user` where `id`=%s;
        '''
        cursor.execute(sql, (self.__userId))
        con.commit()
        cursor.close()
        con.close()
        QMessageBox.about(self, '成功', '用户删除成功')
        self.close()