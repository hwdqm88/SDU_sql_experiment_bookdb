import pymysql
from PySide6.QtWidgets import QMessageBox
from lib.share import SI


class Connector:
    __connection = None
    __cursor = None

    def __init__(self):
        self.__userName = 'root'
        self.__password = 'root'
        self.__databaseName = 'bookdb'
        self.__port = 3306
        try:
            Connector.__connection = pymysql.connect(host='localhost',
                                                     user=self.__userName,
                                                     password=self.__password,
                                                     database=self.__databaseName,
                                                     port=self.__port)
            Connector.__cursor = Connector.__connection.cursor()
        except:
            QMessageBox.critical(SI.g_mainWindow, '错误',
                                 '数据库链接错误，请检查用户名、密码、端口号和数据库名是否已正确设置')

    @staticmethod
    def get_cursor():
        if Connector.__connection is not None:
            Connector.__connection.commit()
            Connector.__cursor.close()
            Connector.__connection.close()
        Connector()
        return Connector.__cursor

    @staticmethod
    def get_connection():
        if Connector.__connection is not None:
            Connector.__connection.commit()
            Connector.__cursor.close()
            Connector.__connection.close()
        Connector()
        return Connector.__connection

    @staticmethod
    def close_connection():
        if Connector.__cursor is not None:
            Connector.__connection.close()
        Connector.__connection = None
        Connector.__cursor = None

