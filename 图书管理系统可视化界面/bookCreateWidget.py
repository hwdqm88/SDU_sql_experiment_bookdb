from PySide2.QtWidgets import QWidget, QMessageBox
from bookCreateWidget_ui import Ui_Widget
import pymysql

class bookCreateWidget(QWidget):
    def __init__(self):
        super(bookCreateWidget, self).__init__()
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.ui.pushButton_add.clicked.connect(self.createBook)

    def createBook(self):
        try:
            con = pymysql.connect(host='localhost', user='root', password='root', database='bookdb',
                                  port=3306)
            cursor = con.cursor()
            sql = '''
                insert into `book`(
                    `name`,
                    `author`,
                    `publish_date`,
                    `publish_name`,
                    `borrowed`,
                    `price`,
                    `intro`)
                values(%s,%s,%s,%s,%s,%s,%s);
            '''
            infoTuple=(
                self.ui.lineEdit_name.text(),
                self.ui.lineEdit_author.text(),
                self.ui.lineEdit_date.text(),
                self.ui.lineEdit_publish.text(),
                self.ui.comboBox_borrowed.currentIndex(),
                self.ui.lineEdit_price.text(),
                self.ui.lineEdit_intro.text(),
            )
            cursor.execute(sql,infoTuple)
            con.commit()
            cursor.close()
            con.close()
            QMessageBox.about(self, '成功', '新增图书成功')
        except:
            QMessageBox.critical(self, '错误', '信息输入有误')
            con.close()
            return