from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QFrame, QApplication,QMessageBox
from ui_login import Ui_Frame as ui_form
from MainWindow import App


class login_form(ui_form, QFrame):
    def __init__(self):
        super(login_form, self).__init__()
        self.setupUi(self)
        self.app=App()

        # 加载字体
        QtGui.QFontDatabase.addApplicationFont("res/Social Media Circled.otf")

        # 隐藏原始的框
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # 按钮事件绑定
        self.close_pushButton.clicked.connect(self.close_event)
        self.min_pushButton.clicked.connect(self.showMinimized)

        self.login_pushButton.clicked.connect(self.login_pushButton_event)
        self.forget_password_pushButton.clicked.connect(self.forget_password_pushButton_event)
        self.register_pushButton.clicked.connect(self.register_pushButton_event)

        # 底部按钮
        self.github_pushButton.clicked.connect(self.github_pushButton_event)
        self.phone_pushButton.clicked.connect(self.phone_pushButton_event)
        self.email_pushButton.clicked.connect(self.email_pushButton_event)

    # 关闭的逻辑
    def close_event(self):
        # 退出应用程序
        QApplication.instance().quit()

    def login_pushButton_event(self):
        user_name=self.user_name_lineEdit.text()
        password=self.password_lineEdit.text()
        if user_name=='华腾辉' and password=='1217':
            self.app.show()
            self.close()
        else:
            QMessageBox.warning(self,'asshole','居然不记得我的名字和生日,气煞我也~')
            self.user_name_lineEdit.clear()
            self.password_lineEdit.clear()

    def forget_password_pushButton_event(self):
        pass

    def register_pushButton_event(self):
        pass

    def github_pushButton_event(self):
        QtGui.QDesktopServices.openUrl(QtCore.QUrl("https://github.com/wp19991/pyqt5_example"))
        pass

    def phone_pushButton_event(self):
        pass

    def email_pushButton_event(self):
        pass
