from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from function import FileHandle
from ui_main import Ui_Form
import sys
import os
os.chdir(os.path.dirname(__file__))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))


class App(QWidget):
    def __init__(self):
        super().__init__()
        #动态加载界面
        uic.loadUi('ui/main.ui', self)
        self.initUI()
        # 初始化变量
        self.source_pathlist = []
        self.goal_path = ''
        self.split_list = []
        self.password = ''
        self.flag = 0

        #pdf模块
        self.PdfToWordButton.clicked.connect(self.PdfToWord)
        self.PdfToWordButton.clicked.connect(self.ButtomColor)
        self.PdfMergeButton.clicked.connect(self.PdfMerge)
        self.PdfMergeButton.clicked.connect(self.ButtomColor)
        self.PdfSplitButton.clicked.connect(self.PdfSplit)
        self.PdfSplitButton.clicked.connect(self.ButtomColor)
        self.PdfEncrypteButton.clicked.connect(self.PdfEncrypte)
        self.PdfEncrypteButton.clicked.connect(self.ButtomColor)
        #ppt模块
        self.PptToPdfButton.clicked.connect(self.PptToPdf)
        self.PptToPdfButton.clicked.connect(self.ButtomColor)
        self.PptToWordButton.clicked.connect(self.PptToWord)
        self.PptToWordButton.clicked.connect(self.ButtomColor)
        self.PptToImageButton.clicked.connect(self.PptToImage)
        self.PptToImageButton.clicked.connect(self.ButtomColor)
        #word模块
        self.WordToPdfButton.clicked.connect(self.WordToPdf)
        self.WordToPdfButton.clicked.connect(self.ButtomColor)
        self.WordMergeButton.clicked.connect(self.WordMerge)
        self.WordMergeButton.clicked.connect(self.ButtomColor)
        self.WordSplitButton.clicked.connect(self.WordSplit)
        self.WordSplitButton.clicked.connect(self.ButtomColor)
        #文件处理模块
        self.FileArrangeButton.clicked.connect(self.FileArrange)
        self.FileArrangeButton.clicked.connect(self.ButtomColor)
        self.FileCleanButton.clicked.connect(self.FileDuplicate)
        self.FileCleanButton.clicked.connect(self.ButtomColor)
        #开始转换
        self.StartButton.clicked.connect(self.Start)

    #初始化界面
    def initUI(self):
        self.setWindowTitle("TengHui")
        self.setGeometry(800, 360, 1000, 900)

    #获取文本框输入
    def GetTextInput(self):
        #每次转换都要清空上一次的数据,再获取输入
        self.source_pathlist=[]
        self.goal_path=''
        self.split_list=[]
        self.password=''
        pathlist=self.FilePathTextEdit.toPlainText()
        if pathlist=='':
            QMessageBox(self,'警告','目标文件源路径输入不能为空！')
        else:
            self.PathArrange(pathlist)
        goal_path=self.GoalPathLineEdit.text()
        print(goal_path)
        self.GoalPath(goal_path)
        split_list=self.SplitLineEdit.text()
        if split_list!='':
            self.SplitList(split_list)
        else:
            if self.flag==3:
                QMessageBox(self,'警告','还未输入分割序列！')
        self.password=self.PasswordLineEdit.text()
    #处理拖拽产生的路径
    def PathArrange(self,pathlist):
        file_list=pathlist.splitlines()
        for file in file_list:
            file_path=file.split('///')[-1]
            self.source_pathlist.append(file_path)
    #处理目标路径
    def GoalPath(self,goal_path):
        self.goal_path=goal_path.replace('\\','/')
    #处理分割序列
    def SplitList(self,split_list):
        if '-' in split_list:
            split_list_str=split_list.split('-')
        elif ',' in split_list:
            split_list_str=split_list.split(',')
        else:
            split_list_str=split_list.split(' ')
        for i in split_list_str:
            self.split_list.append(int(i))

    #转换事件函数
    def Start(self):
        if self.flag==0:
            QMessageBox.information(self,'提示','还未选择功能~')
        if self.flag!=0:
            self.GetTextInput()
            #print(self.source_pathlist)
            self.filehandle = FileHandle(self.source_pathlist, self.goal_path, self.split_list, self.password)
        if self.flag==1:
            try:
                self.filehandle.PdfToWord()
            except:
                defeat=QMessageBox.warning(self, '警告', 'pdf转换word失败,请阅读阅读使用规则和注意事项,输入正确后重新进行操作！',
                                    QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel, QMessageBox.Save)
            else:
                success = QMessageBox.information(self,'提示','pdf文件已成功转化为word文件~')
        if self.flag==2:
            try:
                self.filehandle.PdfMerge()
            except:
                defeat = QMessageBox.warning(self, '警告', 'pdf合并失败,请阅读阅读使用规则和注意事项,输入正确后重新进行操作！',
                                             QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel,
                                             QMessageBox.Save)
            else:
                success = QMessageBox.information(self, '提示', 'pdf文件已成功合并~')
        if self.flag==3:
            try:
                self.filehandle.PdfSplit()
            except:
                defeat = QMessageBox.warning(self, '警告', 'pdf拆分失败,请阅读阅读使用规则和注意事项,输入正确后重新进行操作！',
                                             QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel,
                                             QMessageBox.Save)
            else:
                success = QMessageBox.information(self, '提示', 'pdf文件已成功拆分~')
        if self.flag==4:
            try:
                self.filehandle.PdfEncrypte()
            except:
                defeat = QMessageBox.warning(self, '警告', 'pdf加密失败,请阅读阅读使用规则和注意事项,输入正确后重新进行操作！',
                                             QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel,
                                             QMessageBox.Save)
            else:
                success = QMessageBox.information(self, '提示', 'pdf文件已成功加密~')
        if self.flag==5:
            try:
                self.filehandle.PptToPdf()
            except:
                defeat = QMessageBox.warning(self, '警告', 'ppt转换pdf失败,请阅读阅读使用规则和注意事项,输入正确后重新进行操作！',
                                             QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel,
                                             QMessageBox.Save)
            else:
                success = QMessageBox.information(self, '提示', 'ppt文件已成功转化为pdf文件~')
        if self.flag==6:
            try:
                self.filehandle.PptToWord()
            except:
                defeat = QMessageBox.warning(self, '警告', 'ppt转换word失败,请阅读阅读使用规则和注意事项,输入正确后重新进行操作！',
                                             QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel,
                                             QMessageBox.Save)
            else:
                success = QMessageBox.information(self, '提示', 'ppt文件已成功转化为word文件~')
        if self.flag==7:
            try:
                self.filehandle.PptToImage()
            except:
                defeat = QMessageBox.warning(self, '警告', 'ppt转换jpg图像失败,请阅读阅读使用规则和注意事项,输入正确后重新进行操作！',
                                             QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel,
                                             QMessageBox.Save)
            else:
                success = QMessageBox.information(self, '提示', 'ppt文件已成功转化为jpg图像~')
        if self.flag==8:
            try:
                self.filehandle.WordToPdf()
            except:
                defeat = QMessageBox.warning(self, '警告', 'word转换pdf失败,请阅读阅读使用规则和注意事项,输入正确后重新进行操作！',
                                             QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel,
                                             QMessageBox.Save)
            else:
                success = QMessageBox.information(self, '提示', 'word文件已成功转化为pdf文件~')
        if self.flag==9:
            try:
                self.filehandle.WordMerge()
            except:
                defeat = QMessageBox.warning(self, '警告', 'word合并失败,请阅读阅读使用规则和注意事项,输入正确后重新进行操作！',
                                             QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel,
                                             QMessageBox.Save)
            else:
                success = QMessageBox.information(self, '提示', 'word文件已成功合并~')
        if self.flag==10:
            try:
                self.filehandle.WordSplit()
            except:
                defeat = QMessageBox.warning(self, '警告', 'word拆分失败,请阅读阅读使用规则和注意事项,输入正确后重新进行操作！',
                                             QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel,
                                             QMessageBox.Save)
            else:
                success = QMessageBox.information(self, '抱歉', '该功能华腾辉小哥哥正在修复中，请先使用其他功能吧~')
        if self.flag==11:
            try:
                self.filehandle.FileArrange()
            except:
                defeat = QMessageBox.warning(self, '警告', '文件整理失败,请阅读阅读使用规则和注意事项,输入正确后重新进行操作！',
                                             QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel,
                                             QMessageBox.Save)
            else:
                success = QMessageBox.information(self, '提示', '已完成目标文件夹的整理工作~')
        if self.flag==12:
            try:
                self.filehandle.FileDuplicate()
            except:
                defeat = QMessageBox.warning(self, '警告', '文件去重失败,请阅读阅读使用规则和注意事项,输入正确后重新进行操作！',
                                             QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel,
                                             QMessageBox.Save)
            else:
                success = QMessageBox.information(self, '提示', '已完成目标文件夹的重复文件去除工作~')

    def PdfToWord(self):
        self.flag=1
    def PdfMerge(self):
        self.flag=2
    def PdfSplit(self):
        self.flag=3
    def PdfEncrypte(self):
        self.flag=4
    def PptToPdf(self):
        self.flag=5
    def PptToWord(self):
        self.flag=6
    def PptToImage(self):
        self.flag=7
    def WordToPdf(self):
        self.flag=8
    def WordMerge(self):
        self.flag=9
    def WordSplit(self):
        self.flag=10
    def FileArrange(self):
        self.flag=11
    def FileDuplicate(self):
        self.flag=12

    def ButtomColor(self):

        if self.flag==1:
            self.PdfToWordButton.setStyleSheet \
                ('QPushButton{background-color:rgb(75,170,255);}')
        else:
            self.PdfToWordButton.setStyleSheet \
                ('QPushButton{background-color:white;}')
        if self.flag==2:
            self.PdfMergeButton.setStyleSheet \
                ('QPushButton{background-color:rgb(75,170,255);}')
        else:
            self.PdfMergeButton.setStyleSheet \
                ('QPushButton{background-color:white;}')
        if self.flag==3:
            self.PdfSplitButton.setStyleSheet \
                ('QPushButton{background-color:rgb(75,170,255);}')
        else:
            self.PdfSplitButton.setStyleSheet \
                ('QPushButton{background-color:white;}')

        if self.flag==4:
            self.PdfEncrypteButton.setStyleSheet \
                ('QPushButton{background-color:rgb(75,170,255);}')
        else:
            self.PdfEncrypteButton.setStyleSheet \
                ('QPushButton{background-color:white;}')

        if self.flag==5:
            self.PptToPdfButton.setStyleSheet \
                ('QPushButton{background-color:rgb(75,170,255);}')
        else:
            self.PptToPdfButton.setStyleSheet \
                ('QPushButton{background-color:white;}')
        if self.flag==6:
            self.PptToWordButton.setStyleSheet \
                ('QPushButton{background-color:rgb(75,170,255);}')
        else:
            self.PptToWordButton.setStyleSheet \
                ('QPushButton{background-color:white;}')
        if self.flag==7:
            self.PptToImageButton.setStyleSheet \
                ('QPushButton{background-color:rgb(75,170,255);}')
        else:
            self.PptToImageButton.setStyleSheet \
                ('QPushButton{background-color:white;}')
        if self.flag==8:
            self.WordToPdfButton.setStyleSheet \
                ('QPushButton{background-color:rgb(75,170,255);}')
        else:
            self.WordToPdfButton.setStyleSheet \
                ('QPushButton{background-color:white;}')
        if self.flag==9:
            self.WordMergeButton.setStyleSheet \
                ('QPushButton{background-color:rgb(75,170,255);}')
        else:
            self.WordMergeButton.setStyleSheet \
                ('QPushButton{background-color:white;}')
        if self.flag==10:
            self.WordSplitButton.setStyleSheet \
                ('QPushButton{background-color:rgb(75,170,255);}')
        else:
            self.WordSplitButton.setStyleSheet \
                ('QPushButton{background-color:white;}')
        if self.flag==11:
            self.FileArrangeButton.setStyleSheet \
                ('QPushButton{background-color:rgb(75,170,255);}')
        else:
            self.FileArrangeButton.setStyleSheet \
                ('QPushButton{background-color:white;}')
        if self.flag==12:
            self.FileCleanButton.setStyleSheet \
                ('QPushButton{background-color:rgb(75,170,255);}')
        else:
            self.FileCleanButton.setStyleSheet \
                ('QPushButton{background-color:white;}')

    def closeEvent(self, event):
        result = QMessageBox.question(self, "惜别~", "不陪腾辉哥哥再愉快地玩耍一会吗？",QMessageBox.Yes | QMessageBox.No,QMessageBox.No)
        if (result == QMessageBox.Yes):
            event.accept()
        else:
            event.ignore()


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     APP=App()
#     APP.show()
#     app.exec_()