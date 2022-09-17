# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'layout.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QToolButton,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 140)
        MainWindow.setMaximumSize(QSize(800, 140))
        MainWindow.setBaseSize(QSize(800, 140))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(800, 140))
        self.centralwidget.setMaximumSize(QSize(800, 140))
        self.centralwidget.setBaseSize(QSize(800, 140))
        self.RootFolder_LineEdit = QLineEdit(self.centralwidget)
        self.RootFolder_LineEdit.setObjectName(u"RootFolder_LineEdit")
        self.RootFolder_LineEdit.setGeometry(QRect(10, 10, 721, 41))
        self.RootFolder_LineEdit.setStyleSheet(u"")
        self.RootFolder_LineEdit.setClearButtonEnabled(True)
        self.ChooseFolderButton = QToolButton(self.centralwidget)
        self.ChooseFolderButton.setObjectName(u"ChooseFolderButton")
        self.ChooseFolderButton.setGeometry(QRect(740, 10, 41, 41))
        self.ChooseFolderButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.ChooseFolderButton.setAutoFillBackground(False)
        self.SaveTemporaryFiles_Checkbox = QCheckBox(self.centralwidget)
        self.SaveTemporaryFiles_Checkbox.setObjectName(u"SaveTemporaryFiles_Checkbox")
        self.SaveTemporaryFiles_Checkbox.setGeometry(QRect(20, 110, 331, 20))
        self.SaveTemporaryFiles_Checkbox.setChecked(True)
        self.Extentions_LineEdit = QLineEdit(self.centralwidget)
        self.Extentions_LineEdit.setObjectName(u"Extentions_LineEdit")
        self.Extentions_LineEdit.setGeometry(QRect(10, 60, 521, 41))
        self.Extentions_LineEdit.setToolTipDuration(-1)
        self.Extentions_LineEdit.setStyleSheet(u"")
        self.Extentions_LineEdit.setClearButtonEnabled(True)
        self.StartDelete_Button = QPushButton(self.centralwidget)
        self.StartDelete_Button.setObjectName(u"StartDelete_Button")
        self.StartDelete_Button.setEnabled(False)
        self.StartDelete_Button.setGeometry(QRect(540, 60, 241, 41))
        font = QFont()
        font.setBold(False)
        font.setStyleStrategy(QFont.PreferDefault)
        self.StartDelete_Button.setFont(font)
        self.StartDelete_Button.setCursor(QCursor(Qt.PointingHandCursor))
        self.StartDelete_Button.setAutoDefault(False)
        self.StartDelete_Button.setFlat(False)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.StartDelete_Button.setDefault(True)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"FileDelAll", None))
#if QT_CONFIG(whatsthis)
        self.RootFolder_LineEdit.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.RootFolder_LineEdit.setText("")
        self.RootFolder_LineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u0440\u043d\u0435\u0432\u043e\u0439 \u043f\u0443\u0442\u044c (\u0422\u043e\u0447\u043a\u0430 \u0441\u0442\u0430\u0440\u0442\u0430 \u043f\u043e\u0438\u0441\u043a\u0430 \u0438 \u0443\u0434\u0430\u043b\u0435\u043d\u0438\u044f \u0444\u0430\u0439\u043b\u043e\u0432)", None))
        self.ChooseFolderButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
#if QT_CONFIG(shortcut)
        self.ChooseFolderButton.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(whatsthis)
        self.SaveTemporaryFiles_Checkbox.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.SaveTemporaryFiles_Checkbox.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u044f\u0442\u044c \u043a\u0435\u0448\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0439 \u0441\u043f\u0438\u0441\u043e\u043a \u043d\u0430\u0439\u0434\u0435\u043d\u043d\u044b\u0445 \u0444\u0430\u0439\u043b\u043e\u0432", None))
#if QT_CONFIG(whatsthis)
        self.Extentions_LineEdit.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.Extentions_LineEdit.setText("")
        self.Extentions_LineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0448\u0438\u0440\u0435\u043d\u0438\u044f \u0434\u043b\u044f \u0443\u0434\u0430\u043b\u0435\u043d\u0438\u044f (*.dll *.exe *.*)", None))
        self.StartDelete_Button.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c!", None))
#if QT_CONFIG(shortcut)
        self.StartDelete_Button.setShortcut(QCoreApplication.translate("MainWindow", u"Return", None))
    # retranslateUi

