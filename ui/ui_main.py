# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resource

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(759, 591)
        self.horizontalLayout_10 = QHBoxLayout(Form)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.widget_11 = QWidget(Form)
        self.widget_11.setObjectName(u"widget_11")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_11.sizePolicy().hasHeightForWidth())
        self.widget_11.setSizePolicy(sizePolicy)
        self.verticalLayout_5 = QVBoxLayout(self.widget_11)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_4 = QLabel(self.widget_11)
        self.label_4.setObjectName(u"label_4")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)
        self.label_4.setStyleSheet(u"border-image: url(:/images/rule.jpg);")

        self.verticalLayout_5.addWidget(self.label_4)

        self.widget = QWidget(self.widget_11)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.LabelPdf = QLabel(self.widget)
        self.LabelPdf.setObjectName(u"LabelPdf")
        self.LabelPdf.setStyleSheet(u"border-image: url(:/icons/pdf.png);")

        self.horizontalLayout.addWidget(self.LabelPdf)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.PdfToWordButton = QPushButton(self.widget)
        self.PdfToWordButton.setObjectName(u"PdfToWordButton")

        self.verticalLayout.addWidget(self.PdfToWordButton)

        self.PdfMergeButton = QPushButton(self.widget)
        self.PdfMergeButton.setObjectName(u"PdfMergeButton")

        self.verticalLayout.addWidget(self.PdfMergeButton)

        self.PdfSplitButton = QPushButton(self.widget)
        self.PdfSplitButton.setObjectName(u"PdfSplitButton")

        self.verticalLayout.addWidget(self.PdfSplitButton)

        self.PdfEncrypteButton = QPushButton(self.widget)
        self.PdfEncrypteButton.setObjectName(u"PdfEncrypteButton")

        self.verticalLayout.addWidget(self.PdfEncrypteButton)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout_5.addWidget(self.widget)

        self.widget_2 = QWidget(self.widget_11)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"border-image: url(:/icons/PPTX.png);")

        self.horizontalLayout_3.addWidget(self.label)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.PptToPdfButton = QPushButton(self.widget_2)
        self.PptToPdfButton.setObjectName(u"PptToPdfButton")

        self.verticalLayout_2.addWidget(self.PptToPdfButton)

        self.PptToWordButton = QPushButton(self.widget_2)
        self.PptToWordButton.setObjectName(u"PptToWordButton")

        self.verticalLayout_2.addWidget(self.PptToWordButton)

        self.PptToImageButton = QPushButton(self.widget_2)
        self.PptToImageButton.setObjectName(u"PptToImageButton")

        self.verticalLayout_2.addWidget(self.PptToImageButton)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)


        self.verticalLayout_5.addWidget(self.widget_2)

        self.widget_3 = QWidget(self.widget_11)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_7 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_2 = QLabel(self.widget_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"border-image: url(:/icons/word.png);")

        self.horizontalLayout_5.addWidget(self.label_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.WordToPdfButton = QPushButton(self.widget_3)
        self.WordToPdfButton.setObjectName(u"WordToPdfButton")

        self.verticalLayout_3.addWidget(self.WordToPdfButton)

        self.WordMergeButton = QPushButton(self.widget_3)
        self.WordMergeButton.setObjectName(u"WordMergeButton")

        self.verticalLayout_3.addWidget(self.WordMergeButton)

        self.WordSplitButton = QPushButton(self.widget_3)
        self.WordSplitButton.setObjectName(u"WordSplitButton")

        self.verticalLayout_3.addWidget(self.WordSplitButton)


        self.horizontalLayout_5.addLayout(self.verticalLayout_3)


        self.horizontalLayout_7.addLayout(self.horizontalLayout_5)


        self.verticalLayout_5.addWidget(self.widget_3)

        self.widget_4 = QWidget(self.widget_11)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_9 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_3 = QLabel(self.widget_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"border-image: url(:/icons/file.png);")

        self.horizontalLayout_8.addWidget(self.label_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.FileArrangeButton = QPushButton(self.widget_4)
        self.FileArrangeButton.setObjectName(u"FileArrangeButton")

        self.verticalLayout_4.addWidget(self.FileArrangeButton)

        self.FileCleanButton = QPushButton(self.widget_4)
        self.FileCleanButton.setObjectName(u"FileCleanButton")

        self.verticalLayout_4.addWidget(self.FileCleanButton)


        self.horizontalLayout_8.addLayout(self.verticalLayout_4)


        self.horizontalLayout_9.addLayout(self.horizontalLayout_8)


        self.verticalLayout_5.addWidget(self.widget_4)


        self.horizontalLayout_10.addWidget(self.widget_11)

        self.line = QFrame(Form)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_10.addWidget(self.line)

        self.widget_5 = QWidget(Form)
        self.widget_5.setObjectName(u"widget_5")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy2)
        self.verticalLayout_6 = QVBoxLayout(self.widget_5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.widget_14 = QWidget(self.widget_5)
        self.widget_14.setObjectName(u"widget_14")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.widget_14.sizePolicy().hasHeightForWidth())
        self.widget_14.setSizePolicy(sizePolicy3)
        self.verticalLayout_18 = QVBoxLayout(self.widget_14)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.textBrowser = QTextBrowser(self.widget_14)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setStyleSheet(u"border-image: url(:/images/logo.jpg);")

        self.horizontalLayout_6.addWidget(self.textBrowser)

        self.textBrowser_2 = QTextBrowser(self.widget_14)
        self.textBrowser_2.setObjectName(u"textBrowser_2")
        self.textBrowser_2.setStyleSheet(u"border-image: url(images/warning.jpg);")

        self.horizontalLayout_6.addWidget(self.textBrowser_2)


        self.verticalLayout_18.addLayout(self.horizontalLayout_6)


        self.verticalLayout_6.addWidget(self.widget_14)

        self.line_2 = QFrame(self.widget_5)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_6.addWidget(self.line_2)

        self.widget_12 = QWidget(self.widget_5)
        self.widget_12.setObjectName(u"widget_12")
        sizePolicy2.setHeightForWidth(self.widget_12.sizePolicy().hasHeightForWidth())
        self.widget_12.setSizePolicy(sizePolicy2)
        self.verticalLayout_17 = QVBoxLayout(self.widget_12)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.FilePathTextEdit = QTextEdit(self.widget_12)
        self.FilePathTextEdit.setObjectName(u"FilePathTextEdit")
        sizePolicy.setHeightForWidth(self.FilePathTextEdit.sizePolicy().hasHeightForWidth())
        self.FilePathTextEdit.setSizePolicy(sizePolicy)
        self.FilePathTextEdit.setStyleSheet(u"border-image: url(:/images/background.jpg);")

        self.verticalLayout_16.addWidget(self.FilePathTextEdit)

        self.label_5 = QLabel(self.widget_12)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"font: 9pt \"Arial Rounded MT Bold\";\n"
"alternate-background-color: rgb(85, 255, 255);")

        self.verticalLayout_16.addWidget(self.label_5)

        self.GoalPathLineEdit = QLineEdit(self.widget_12)
        self.GoalPathLineEdit.setObjectName(u"GoalPathLineEdit")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(10)
        sizePolicy4.setHeightForWidth(self.GoalPathLineEdit.sizePolicy().hasHeightForWidth())
        self.GoalPathLineEdit.setSizePolicy(sizePolicy4)

        self.verticalLayout_16.addWidget(self.GoalPathLineEdit)

        self.label_6 = QLabel(self.widget_12)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_16.addWidget(self.label_6)

        self.SplitLineEdit = QLineEdit(self.widget_12)
        self.SplitLineEdit.setObjectName(u"SplitLineEdit")

        self.verticalLayout_16.addWidget(self.SplitLineEdit)

        self.label_7 = QLabel(self.widget_12)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_16.addWidget(self.label_7)

        self.PasswordLineEdit = QLineEdit(self.widget_12)
        self.PasswordLineEdit.setObjectName(u"PasswordLineEdit")

        self.verticalLayout_16.addWidget(self.PasswordLineEdit)

        self.StartButton = QPushButton(self.widget_12)
        self.StartButton.setObjectName(u"StartButton")

        self.verticalLayout_16.addWidget(self.StartButton)


        self.verticalLayout_17.addLayout(self.verticalLayout_16)


        self.verticalLayout_6.addWidget(self.widget_12)


        self.horizontalLayout_10.addWidget(self.widget_5)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_4.setText("")
        self.LabelPdf.setText("")
        self.PdfToWordButton.setText(QCoreApplication.translate("Form", u"pdf\u2192word", None))
        self.PdfMergeButton.setText(QCoreApplication.translate("Form", u"pdf\u5408\u5e76", None))
        self.PdfSplitButton.setText(QCoreApplication.translate("Form", u"pdf\u5206\u5272", None))
        self.PdfEncrypteButton.setText(QCoreApplication.translate("Form", u"pdf\u52a0\u5bc6", None))
        self.label.setText("")
        self.PptToPdfButton.setText(QCoreApplication.translate("Form", u"ppt\u2192pdf", None))
        self.PptToWordButton.setText(QCoreApplication.translate("Form", u"ppt\u2192word", None))
        self.PptToImageButton.setText(QCoreApplication.translate("Form", u"ppt\u2192image", None))
        self.label_2.setText("")
        self.WordToPdfButton.setText(QCoreApplication.translate("Form", u"word\u2192pdf", None))
        self.WordMergeButton.setText(QCoreApplication.translate("Form", u"word\u5408\u5e76", None))
        self.WordSplitButton.setText(QCoreApplication.translate("Form", u"word\u5206\u5272", None))
        self.label_3.setText("")
        self.FileArrangeButton.setText(QCoreApplication.translate("Form", u"\u6587\u4ef6\u6574\u7406", None))
        self.FileCleanButton.setText(QCoreApplication.translate("Form", u"\u6587\u4ef6\u53bb\u91cd", None))
        self.textBrowser.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#55aaff;\">\u4f7f\u7528\u65b9\u6cd5</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#55aaff;\">1.\u8f93\u5165\u6587\u4ef6\u5939/\u6587\u4ef6\u7684\u7edd\u5bf9\u8def\u5f84\uff0c\u6570\u91cf\u4e0d\u9650\uff1b</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#55aaff;\">2.(\u53ef\u9009)\u8f93\u5165\u76ee\u6807\u6587\u4ef6\u5939\u7edd\u5bf9"
                        "\u8def\u5f84\uff0c\u5426\u5219\u9ed8\u8ba4\u5728\u8f93\u5165\u7684\u7b2c\u4e00\u4e2a\u6587\u4ef6\u76f8\u540c\u6587\u4ef6\u5939\u4e0b\u65b0\u5efa\u4e00\u6587\u4ef6\u5939\u7528\u4e8e\u5b58\u50a8\uff1b</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#55aaff;\">3.(\u53ef\u9009)pdf/word\u5206\u5272\u65f6\u6ce8\u610f\u8f93\u5165\u5206\u5272\u5e8f\u5217\uff0c\u95f4\u9694\u7b26\u4ece{\u7a7a\u683c,\u9017\u53f7,-}\u4efb\u9009\u5176\u4e00\uff1b</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#55aaff;\">4.(\u53ef\u9009)pdf\u52a0\u5bc6\u65f6\uff0c\u5fc5\u987b\u8f93\u5165\u5bc6\u7801\uff0c\u5bc6\u7801\u4efb\u610f\uff0c\u8bf7\u541b\u52ff\u5fd8\uff1b</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#55aaff"
                        ";\">5.\u5b8c\u6210\u4e0a\u8ff0\u6b65\u9aa4\u540e\uff0c\u70b9\u51fb'START'\u5373\u53ef\u5f00\u59cb\u3002</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#55aaff;\"><br /></p></body></html>", None))
        self.textBrowser_2.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ff5500;\">\u6ce8\u610f\u4e8b\u9879\uff1a</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ff5500;\">1.\u8f93\u5165\u6587\u4ef6/\u6587\u4ef6\u5939\uff0c\u4ee5\u53ca\u76ee\u6807\u6587\u4ef6\u5939\uff0c\u5fc5\u987b\u8f93\u5165\u7edd\u5bf9\u8def\u5f84\uff1b</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ff5500;\">2.\u52a0\u5bc6\u6587"
                        "\u4ef6\u65e0\u6cd5\u8fdb\u884c\u6240\u6709\u9009\u9879\uff1b</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ff5500;\">3.\u6587\u4ef6\u6574\u7406\uff1a\u6309\u6587\u4ef6\u540e\u7f00\u540d\u79f0\u6574\u7406\u6587\u4ef6\uff0c\u5747\u50a8\u5b58\u5728\u540e\u7f00\u540d\u79f0\u65b0\u6587\u4ef6\u5939\u4e0b\uff0c\u65e0\u540e\u7f00\u540d\u79f0\u7684\u6587\u4ef6\uff0c\u5747\u50a8\u5b58\u5728'others'\u6587\u4ef6\u5939\u4e0b\uff1b</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ff5500;\">4.\u6587\u4ef6\u53bb\u91cd\uff1a\u6bd4\u8f83\u6587\u4ef6\u5185\u5bb9\uff0c\u54ea\u6015\u6587\u4ef6\u540d\u79f0\u4e0d\u540c\uff0c\u6587\u4ef6\u5185\u5bb9\u76f8\u540c\u7684\u4e5f\u4f1a\u88ab\u6e05\u7406</span>\u3002</p></body></html>", None))
        self.FilePathTextEdit.setPlaceholderText(QCoreApplication.translate("Form", u"\u8bf7\u8f93\u5165\u6587\u4ef6\u5939\u7edd\u5bf9\u8def\u5f84/\u6587\u4ef6\u7edd\u5bf9\u8def\u5f84...", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u5982\u679c\u4e0d\u8f93\u5165\u76ee\u6807\u6587\u4ef6\u5939\u7edd\u5bf9\u8def\u5f84\uff0c\u5c06\u9ed8\u8ba4\u5b58\u653e\u5728\u7b2c\u4e00\u4e2a\u6587\u4ef6\u76ee\u5f55\u4e0b\uff01", None))
        self.GoalPathLineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"\u8bf7\u8f93\u5165\u76ee\u6807\u6587\u4ef6\u5939...", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u4ec5\u5728pdf/word\u5206\u5272\u65f6\u9700\u8981\u8f93\u5165,\u8bf7\u7528{' ',','-'}\u4efb\u9009\u5176\u4e00\u8fdb\u884c\u95f4\u9694!", None))
        self.SplitLineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"\u8bf7\u8f93\u5165\u5206\u5272\u5e8f\u5217...", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"\u4ec5\u5728pdf\u52a0\u5bc6\u65f6\u9700\u8981\u8f93\u5165,\u8bf7\u8f93\u5165\u5408\u9002\u5bc6\u7801\uff01", None))
        self.PasswordLineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"\u8bf7\u8f93\u5165\u52a0\u5bc6\u5bc6\u7801...", None))
        self.StartButton.setText(QCoreApplication.translate("Form", u"START", None))
    # retranslateUi

