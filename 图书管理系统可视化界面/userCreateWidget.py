from PySide2.QtWidgets import QWidget, QMessageBox
from userCreateWidget_ui import Ui_Widget
import pymysql

class userCreateWidget(QWidget):
    def __init__(self):
        super(userCreateWidget, self).__init__()
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.ui.pushButton_add.clicked.connect(self.createUser)

    def createUser(self):
        try:
            con = pymysql.connect(host='localhost', user='root', password='root', database='bookdb',
                                  port=3306)
            cursor = con.cursor()
            sql = '''
                insert into `user`(
                    `user_name`,
                    `password`,
                    `sex`,
                    `balance`,
                    `phone_number`,
                    `role_id`,
                    `unit`)
                values(%s,%s,%s,%s,%s,%s,%s);
            '''
            infoTuple=(
                self.ui.lineEdit_name.text(),
                self.ui.lineEdit_password.text(),
                self.ui.comboBox_sex.currentText(),
                float(self.ui.lineEdit_balance.text()),
                self.ui.lineEdit_tele.text(),
                self.ui.comboBox_role.currentIndex()+1,
                self.ui.lineEdit_unit.text(),
            )
            cursor.execute(sql,infoTuple)
            con.commit()
            cursor.close()
            con.close()
            QMessageBox.about(self, '成功', '新增读者成功')
        except:
            QMessageBox.critical(self, '错误', '信息输入有误')
            con.close()
            return