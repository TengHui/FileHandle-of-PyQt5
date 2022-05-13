import sys
import os
from PyQt5.QtWidgets import QApplication
from login.login_form import login_form
from login.splash import SplashScreen

os.chdir(os.path.dirname(__file__))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))


class App(QApplication):
    def __init__(self):
        super().__init__(sys.argv)
        self.windows = {}

    def run(self, pytest=False):
        splash = SplashScreen()  # 启动界面
        splash.loadProgress()  # 启动界面

        self.windows["login"] = login_form()
        self.windows["login"].show()

        if not pytest:
            sys.exit(self.exec_())


if __name__ == "__main__":
    App().run()