# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QRadioButton,
    QSizePolicy, QStatusBar, QVBoxLayout, QWidget)
import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        icon = QIcon()
        icon.addFile(u":/images/icons/dictionary.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.optionLayout = QHBoxLayout()
        self.optionLayout.setObjectName(u"optionLayout")
        self.groupBox_enabledDicts = QGroupBox(self.centralwidget)
        self.groupBox_enabledDicts.setObjectName(u"groupBox_enabledDicts")

        self.optionLayout.addWidget(self.groupBox_enabledDicts)

        self.groupBox_searchMode = QGroupBox(self.centralwidget)
        self.groupBox_searchMode.setObjectName(u"groupBox_searchMode")
        self.horizontalLayout = QHBoxLayout(self.groupBox_searchMode)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.exactSearch = QRadioButton(self.groupBox_searchMode)
        self.exactSearch.setObjectName(u"exactSearch")
        self.exactSearch.setChecked(True)

        self.horizontalLayout.addWidget(self.exactSearch)

        self.fuzzySearch = QRadioButton(self.groupBox_searchMode)
        self.fuzzySearch.setObjectName(u"fuzzySearch")

        self.horizontalLayout.addWidget(self.fuzzySearch)


        self.optionLayout.addWidget(self.groupBox_searchMode)


        self.verticalLayout.addLayout(self.optionLayout)

        self.searchLayout = QHBoxLayout()
        self.searchLayout.setObjectName(u"searchLayout")
        self.labSearch = QLabel(self.centralwidget)
        self.labSearch.setObjectName(u"labSearch")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labSearch.sizePolicy().hasHeightForWidth())
        self.labSearch.setSizePolicy(sizePolicy)
        self.labSearch.setMinimumSize(QSize(18, 0))
        self.labSearch.setStyleSheet(u"image: url(:/images/icons/search.png);")

        self.searchLayout.addWidget(self.labSearch)

        self.searchEdit = QLineEdit(self.centralwidget)
        self.searchEdit.setObjectName(u"searchEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.searchEdit.sizePolicy().hasHeightForWidth())
        self.searchEdit.setSizePolicy(sizePolicy1)

        self.searchLayout.addWidget(self.searchEdit)


        self.verticalLayout.addLayout(self.searchLayout)

        self.resultWidget = QWidget(self.centralwidget)
        self.resultWidget.setObjectName(u"resultWidget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.resultWidget.sizePolicy().hasHeightForWidth())
        self.resultWidget.setSizePolicy(sizePolicy2)
        self.resultWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.resultWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"OI Dictionary", None))
        self.groupBox_enabledDicts.setTitle(QCoreApplication.translate("MainWindow", u"\u542f\u7528\u8bcd\u5178", None))
        self.groupBox_searchMode.setTitle(QCoreApplication.translate("MainWindow", u"\u67e5\u627e\u6a21\u5f0f", None))
#if QT_CONFIG(tooltip)
        self.exactSearch.setToolTip(QCoreApplication.translate("MainWindow", u"\u663e\u793a\u76f8\u4f3c\u5ea6\u8d85\u8fc70.7\u7684\u7ed3\u679c\u3002", None))
#endif // QT_CONFIG(tooltip)
        self.exactSearch.setText(QCoreApplication.translate("MainWindow", u"\u7cbe\u786e\u67e5\u627e\uff08\u9ed8\u8ba4\uff09", None))
#if QT_CONFIG(tooltip)
        self.fuzzySearch.setToolTip(QCoreApplication.translate("MainWindow", u"\u663e\u793a\u76f8\u4f3c\u5ea6\u8d85\u8fc70.5\u7684\u7ed3\u679c\u3002", None))
#endif // QT_CONFIG(tooltip)
        self.fuzzySearch.setText(QCoreApplication.translate("MainWindow", u"\u6a21\u7cca\u67e5\u627e", None))
        self.labSearch.setText("")
        self.searchEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u641c\u7d22\u2026\u2026", None))
    # retranslateUi

