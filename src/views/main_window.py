# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGraphicsView,
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QLayout, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QPushButton, QRadioButton, QSizePolicy,
    QStatusBar, QTabWidget, QVBoxLayout, QWidget)
from src.views.custom_component import VideoGraphicsView
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1103, 721)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.ui_save_all_config_btn = QAction(MainWindow)
        self.ui_save_all_config_btn.setObjectName(u"ui_save_all_config_btn")
        self.ui_save_all_config_btn.setCheckable(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_1 = QWidget()
        self.tab_1.setObjectName(u"tab_1")
        self.verticalLayout_2 = QVBoxLayout(self.tab_1)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(6, 0, 0, 0)
        self.widget = QWidget(self.tab_1)
        self.widget.setObjectName(u"widget")
        self.widget.setMaximumSize(QSize(16777215, 100))
        self.horizontalLayoutWidget_2 = QWidget(self.widget)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(0, 0, 1091, 91))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.groupBox_5 = QGroupBox(self.horizontalLayoutWidget_2)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setMinimumSize(QSize(360, 80))
        self.groupBox_5.setMaximumSize(QSize(16777215, 100))
        font = QFont()
        font.setPointSize(8)
        self.groupBox_5.setFont(font)
        self.verticalLayoutWidget = QWidget(self.groupBox_5)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 20, 341, 70))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(6, 2, 6, 2)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_5 = QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(16777215, 30))
        self.label_5.setFont(font)

        self.horizontalLayout_5.addWidget(self.label_5)

        self.ui_mac_input = QLineEdit(self.verticalLayoutWidget)
        self.ui_mac_input.setObjectName(u"ui_mac_input")
        self.ui_mac_input.setMaximumSize(QSize(260, 30))
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(False)
        font1.setKerning(False)
        self.ui_mac_input.setFont(font1)
        self.ui_mac_input.setStyleSheet(u"background-color: #D6EAF8;   /* T\u00edm \u0111\u1eadm (Indigo) */\n"
"    color: red;                /* Ch\u1eef tr\u1eafng */        /* Ch\u1eef \u0111\u1eadm */\n"
"    border: 1px solid #9370DB;  /* Vi\u1ec1n t\u00edm s\u00e1ng (Medium Purple) */\n"
"    border-radius: 3px;")
        self.ui_mac_input.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.ui_mac_input.setDragEnabled(True)
        self.ui_mac_input.setClearButtonEnabled(False)

        self.horizontalLayout_5.addWidget(self.ui_mac_input)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_7 = QLabel(self.verticalLayoutWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(16777215, 30))
        self.label_7.setFont(font)

        self.horizontalLayout_4.addWidget(self.label_7)

        self.ui_last_mac_input = QLineEdit(self.verticalLayoutWidget)
        self.ui_last_mac_input.setObjectName(u"ui_last_mac_input")
        self.ui_last_mac_input.setEnabled(False)
        self.ui_last_mac_input.setMaximumSize(QSize(260, 30))
        font2 = QFont()
        font2.setPointSize(16)
        self.ui_last_mac_input.setFont(font2)
        self.ui_last_mac_input.setStyleSheet(u"background-color: #FFFFF0;\n"
"border: 1px solid #ccc")
        self.ui_last_mac_input.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.ui_last_mac_input.setClearButtonEnabled(False)

        self.horizontalLayout_4.addWidget(self.ui_last_mac_input)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)

        self.horizontalLayout_2.addWidget(self.groupBox_5)

        self.groupBox_4 = QGroupBox(self.horizontalLayoutWidget_2)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setMinimumSize(QSize(160, 80))
        self.groupBox_4.setMaximumSize(QSize(16777215, 100))
        self.groupBox_4.setFont(font)
        self.groupBox_4.setCursor(QCursor(Qt.CursorShape.SizeVerCursor))
        self.ui_start_camera_btn = QPushButton(self.groupBox_4)
        self.ui_start_camera_btn.setObjectName(u"ui_start_camera_btn")
        self.ui_start_camera_btn.setGeometry(QRect(10, 30, 71, 31))
        font3 = QFont()
        font3.setPointSize(8)
        font3.setBold(False)
        self.ui_start_camera_btn.setFont(font3)
        self.ui_start_camera_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.ui_start_camera_btn.setStyleSheet(u"")
        self.ui_start_camera_btn.setIconSize(QSize(18, 18))
        self.ui_stop_camera_btn = QPushButton(self.groupBox_4)
        self.ui_stop_camera_btn.setObjectName(u"ui_stop_camera_btn")
        self.ui_stop_camera_btn.setGeometry(QRect(80, 30, 71, 31))
        self.ui_stop_camera_btn.setFont(font3)
        self.ui_stop_camera_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.ui_stop_camera_btn.setStyleSheet(u"")
        self.ui_stop_camera_btn.setIconSize(QSize(27, 27))

        self.horizontalLayout_2.addWidget(self.groupBox_4)

        self.groupBox_7 = QGroupBox(self.horizontalLayoutWidget_2)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setMinimumSize(QSize(110, 80))
        self.groupBox_7.setMaximumSize(QSize(110, 100))
        self.groupBox_7.setFont(font)
        self.groupBox_7.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.ui_proces_type_camera_label = QLabel(self.groupBox_7)
        self.ui_proces_type_camera_label.setObjectName(u"ui_proces_type_camera_label")
        self.ui_proces_type_camera_label.setGeometry(QRect(10, 20, 91, 21))
        self.ui_proces_type_camera_label.setStyleSheet(u"")
        self.ui_proces_type_camera_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.ui_process_type_image_label = QLabel(self.groupBox_7)
        self.ui_process_type_image_label.setObjectName(u"ui_process_type_image_label")
        self.ui_process_type_image_label.setGeometry(QRect(10, 50, 91, 21))
        self.ui_process_type_image_label.setStyleSheet(u"")
        self.ui_process_type_image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.groupBox_7)

        self.groupBox_2 = QGroupBox(self.horizontalLayoutWidget_2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMinimumSize(QSize(110, 80))
        self.groupBox_2.setMaximumSize(QSize(110, 100))
        self.groupBox_2.setFont(font)
        self.groupBox_2.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.ui_open_config_file_btn = QPushButton(self.groupBox_2)
        self.ui_open_config_file_btn.setObjectName(u"ui_open_config_file_btn")
        self.ui_open_config_file_btn.setGeometry(QRect(10, 20, 91, 21))
        self.ui_open_config_file_btn.setFont(font3)
        self.ui_open_config_file_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.ui_open_config_file_btn.setStyleSheet(u"background-color: #F0E68C;\n"
"border-radius: 3px;\n"
"border: 1px solid #ccc;\n"
"")
        self.ui_debug_check_box = QCheckBox(self.groupBox_2)
        self.ui_debug_check_box.setObjectName(u"ui_debug_check_box")
        self.ui_debug_check_box.setGeometry(QRect(30, 50, 61, 20))

        self.horizontalLayout_2.addWidget(self.groupBox_2)

        self.groupBox_6 = QGroupBox(self.horizontalLayoutWidget_2)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setMinimumSize(QSize(110, 80))
        self.groupBox_6.setMaximumSize(QSize(110, 100))
        self.groupBox_6.setFont(font)
        self.groupBox_6.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.ui_open_image_btn = QPushButton(self.groupBox_6)
        self.ui_open_image_btn.setObjectName(u"ui_open_image_btn")
        self.ui_open_image_btn.setGeometry(QRect(10, 30, 91, 31))
        self.ui_open_image_btn.setFont(font)
        self.ui_open_image_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.ui_open_image_btn.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.groupBox_6)

        self.groupBox = QGroupBox(self.horizontalLayoutWidget_2)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(110, 80))
        self.groupBox.setMaximumSize(QSize(110, 100))
        self.groupBox.setFont(font)
        self.groupBox.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.ui_heat_map_radio_btn = QRadioButton(self.groupBox)
        self.ui_heat_map_radio_btn.setObjectName(u"ui_heat_map_radio_btn")
        self.ui_heat_map_radio_btn.setGeometry(QRect(20, 20, 82, 17))
        self.ui_heat_map_radio_btn.setIconSize(QSize(16, 16))
        self.ui_segment_radio_btn = QRadioButton(self.groupBox)
        self.ui_segment_radio_btn.setObjectName(u"ui_segment_radio_btn")
        self.ui_segment_radio_btn.setGeometry(QRect(20, 50, 82, 17))

        self.horizontalLayout_2.addWidget(self.groupBox)

        self.groupBox_3 = QGroupBox(self.horizontalLayoutWidget_2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMinimumSize(QSize(110, 80))
        self.groupBox_3.setMaximumSize(QSize(110, 100))
        self.groupBox_3.setFont(font)
        self.groupBox_3.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.ui_model_name_label = QLabel(self.groupBox_3)
        self.ui_model_name_label.setObjectName(u"ui_model_name_label")
        self.ui_model_name_label.setGeometry(QRect(10, 20, 91, 51))
        font4 = QFont()
        font4.setPointSize(12)
        self.ui_model_name_label.setFont(font4)
        self.ui_model_name_label.setStyleSheet(u"background: #D6EAF8;\n"
"padding: 5px")
        self.ui_model_name_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.groupBox_3)


        self.verticalLayout_2.addWidget(self.widget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SizeConstraint.SetNoConstraint)
        self.groupBox_10 = QGroupBox(self.tab_1)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.groupBox_10.setMinimumSize(QSize(150, 0))
        self.groupBox_10.setMaximumSize(QSize(150, 16777215))
        self.groupBox_10.setStyleSheet(u"padding: 0 5px;\n"
"\n"
"")
        self.groupBox_10.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.groupBox_10.setFlat(False)
        self.groupBox_10.setCheckable(False)
        self.ui_logo_info_label = QLabel(self.groupBox_10)
        self.ui_logo_info_label.setObjectName(u"ui_logo_info_label")
        self.ui_logo_info_label.setGeometry(QRect(0, 20, 151, 81))
        self.ui_logo_info_label.setPixmap(QPixmap(r"src\assets\IVIS.png"))
        self.ui_logo_info_label.setScaledContents(True)
        self.ui_process_btn = QPushButton(self.groupBox_10)
        self.ui_process_btn.setObjectName(u"ui_process_btn")
        self.ui_process_btn.setEnabled(True)
        self.ui_process_btn.setGeometry(QRect(10, 130, 131, 41))
        font5 = QFont()
        self.ui_process_btn.setFont(font5)
        self.ui_process_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.ui_process_btn.setStyleSheet(u"")
        self.ui_auto_process_check_box = QCheckBox(self.groupBox_10)
        self.ui_auto_process_check_box.setObjectName(u"ui_auto_process_check_box")
        self.ui_auto_process_check_box.setEnabled(True)
        self.ui_auto_process_check_box.setGeometry(QRect(20, 200, 111, 20))
        font6 = QFont()
        font6.setPointSize(10)
        self.ui_auto_process_check_box.setFont(font6)
        self.ui_auto_process_check_box.setMouseTracking(True)
#if QT_CONFIG(shortcut)
        self.ui_auto_process_check_box.setShortcut(u"")
#endif // QT_CONFIG(shortcut)
        self.ui_auto_process_check_box.setCheckable(True)
        self.ui_auto_process_check_box.setAutoRepeatDelay(10)
        self.ui_status_label = QLabel(self.groupBox_10)
        self.ui_status_label.setObjectName(u"ui_status_label")
        self.ui_status_label.setGeometry(QRect(10, 250, 131, 91))
        font7 = QFont()
        font7.setPointSize(18)
        self.ui_status_label.setFont(font7)
        self.ui_status_label.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.ui_status_label.setStyleSheet(u"border: 1px solid #ccc;\n"
"border-radius: 3px;\n"
"\n"
"")
        self.ui_status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.ui_sum_ok_label = QLabel(self.groupBox_10)
        self.ui_sum_ok_label.setObjectName(u"ui_sum_ok_label")
        self.ui_sum_ok_label.setGeometry(QRect(10, 360, 131, 51))
        font8 = QFont()
        font8.setPointSize(11)
        font8.setBold(True)
        self.ui_sum_ok_label.setFont(font8)
        self.ui_sum_ok_label.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.ui_sum_ok_label.setStyleSheet(u"background-color:#ccc;\n"
"border-radius: 3px;\n"
"color:blue;\n"
"font-weight:bold\n"
"\n"
"")
        self.ui_sum_ok_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.ui_sum_ng_label = QLabel(self.groupBox_10)
        self.ui_sum_ng_label.setObjectName(u"ui_sum_ng_label")
        self.ui_sum_ng_label.setGeometry(QRect(10, 430, 131, 51))
        self.ui_sum_ng_label.setFont(font8)
        self.ui_sum_ng_label.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.ui_sum_ng_label.setStyleSheet(u"background-color:#ccc;\n"
"border-radius: 3px;\n"
"color:red;\n"
"font-weight:bold\n"
"")
        self.ui_sum_ng_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.line = QFrame(self.groupBox_10)
        self.line.setObjectName(u"line")
        self.line.setEnabled(False)
        self.line.setGeometry(QRect(0, 240, 151, 16))
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout.addWidget(self.groupBox_10)

        self.groupBox_9 = QGroupBox(self.tab_1)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.groupBox_9.setStyleSheet(u"background-color:white;")
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox_9)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.ui_label_display_video = VideoGraphicsView(self.groupBox_9)
        self.ui_label_display_video.setObjectName(u"ui_label_display_video")

        self.horizontalLayout_3.addWidget(self.ui_label_display_video)


        self.horizontalLayout.addWidget(self.groupBox_9)

        self.groupBox_8 = QGroupBox(self.tab_1)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.groupBox_8.setMinimumSize(QSize(120, 0))
        self.groupBox_8.setMaximumSize(QSize(120, 16777215))
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_8)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupBox_11 = QGroupBox(self.groupBox_8)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.groupBox_11.setStyleSheet(u"border: 3px solid red")

        self.verticalLayout_3.addWidget(self.groupBox_11)

        self.groupBox_12 = QGroupBox(self.groupBox_8)
        self.groupBox_12.setObjectName(u"groupBox_12")
        self.groupBox_12.setStyleSheet(u"border: 3px solid green")

        self.verticalLayout_3.addWidget(self.groupBox_12)


        self.horizontalLayout.addWidget(self.groupBox_8)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.ui_system_message_label = QLabel(self.tab_1)
        self.ui_system_message_label.setObjectName(u"ui_system_message_label")
        self.ui_system_message_label.setMinimumSize(QSize(0, 35))
        font9 = QFont()
        font9.setPointSize(14)
        font9.setBold(True)
        self.ui_system_message_label.setFont(font9)
        self.ui_system_message_label.setStyleSheet(u"border: 1px dot #ccc")
        self.ui_system_message_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.ui_system_message_label)

        self.verticalLayout_2.setStretch(0, 4)
        self.verticalLayout_2.setStretch(1, 22)
        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1103, 33))
        self.menuParameters = QMenu(self.menubar)
        self.menuParameters.setObjectName(u"menuParameters")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuParameters.menuAction())
        self.menuParameters.addAction(self.ui_save_all_config_btn)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.ui_save_all_config_btn.setText(QCoreApplication.translate("MainWindow", u"Save all config", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"QR/Bar code", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Scan MAC", None))
        self.ui_mac_input.setPlaceholderText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Last MAC", None))
        self.ui_last_mac_input.setText("")
        self.ui_last_mac_input.setPlaceholderText("")
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Camera/Image", None))
        self.ui_start_camera_btn.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.ui_stop_camera_btn.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"Process Type", None))
        self.ui_proces_type_camera_label.setText(QCoreApplication.translate("MainWindow", u"Camera", None))
        self.ui_process_type_image_label.setText(QCoreApplication.translate("MainWindow", u"Image", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Options", None))
        self.ui_open_config_file_btn.setText(QCoreApplication.translate("MainWindow", u"Open Config", None))
        self.ui_debug_check_box.setText(QCoreApplication.translate("MainWindow", u"Debug", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Image Predict", None))
        self.ui_open_image_btn.setText(QCoreApplication.translate("MainWindow", u"Open Image", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"View Type", None))
        self.ui_heat_map_radio_btn.setText(QCoreApplication.translate("MainWindow", u"Heat map", None))
        self.ui_segment_radio_btn.setText(QCoreApplication.translate("MainWindow", u"Segment", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Model Name", None))
        self.ui_model_name_label.setText(QCoreApplication.translate("MainWindow", u"Model.xml", None))
        self.groupBox_10.setTitle(QCoreApplication.translate("MainWindow", u"Info", None))
        self.ui_logo_info_label.setText("")
        self.ui_process_btn.setText(QCoreApplication.translate("MainWindow", u"Process", None))
        self.ui_auto_process_check_box.setText(QCoreApplication.translate("MainWindow", u"Auto Process", None))
        self.ui_status_label.setText(QCoreApplication.translate("MainWindow", u"STATUS: ...", None))
        self.ui_sum_ok_label.setText(QCoreApplication.translate("MainWindow", u"N OK:", None))
        self.ui_sum_ng_label.setText(QCoreApplication.translate("MainWindow", u"N NG:", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("MainWindow", u"Camera", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("MainWindow", u"Message", None))
        self.groupBox_11.setTitle(QCoreApplication.translate("MainWindow", u"System", None))
        self.groupBox_12.setTitle(QCoreApplication.translate("MainWindow", u"SFIS", None))
        self.ui_system_message_label.setText(QCoreApplication.translate("MainWindow", u"This is System Message", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), QCoreApplication.translate("MainWindow", u"---Visual Inspection System---", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"---Choosing Model---", None))
        self.menuParameters.setTitle(QCoreApplication.translate("MainWindow", u"Config", None))
    # retranslateUi

