# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_test.ui'
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
    QLayout, QLineEdit, QMainWindow, QPushButton,
    QRadioButton, QSizePolicy, QStatusBar, QVBoxLayout,
    QWidget)
from src.views.custom_component import VideoGraphicsView

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1062, 619)
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
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(2)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SizeConstraint.SetNoConstraint)
        self.groupBox_9 = QGroupBox(self.widget)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.groupBox_9.setStyleSheet(u"background-color:white;")
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox_9)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.groupBox_10 = QGroupBox(self.groupBox_9)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.groupBox_10.setMinimumSize(QSize(100, 0))
        self.groupBox_10.setMaximumSize(QSize(100, 16777215))
        self.groupBox_10.setStyleSheet(u"padding: 0 5px;\n"
"\n"
"")
        self.groupBox_10.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.groupBox_10.setFlat(False)
        self.groupBox_10.setCheckable(False)
        self.ui_process_btn = QPushButton(self.groupBox_10)
        self.ui_process_btn.setObjectName(u"ui_process_btn")
        self.ui_process_btn.setEnabled(True)
        self.ui_process_btn.setGeometry(QRect(10, 20, 81, 31))
        font = QFont()
        self.ui_process_btn.setFont(font)
        self.ui_process_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.ui_process_btn.setStyleSheet(u"")
        self.ui_auto_process_check_box = QCheckBox(self.groupBox_10)
        self.ui_auto_process_check_box.setObjectName(u"ui_auto_process_check_box")
        self.ui_auto_process_check_box.setEnabled(True)
        self.ui_auto_process_check_box.setGeometry(QRect(20, 60, 71, 20))
        font1 = QFont()
        font1.setPointSize(8)
        self.ui_auto_process_check_box.setFont(font1)
        self.ui_auto_process_check_box.setMouseTracking(True)
#if QT_CONFIG(shortcut)
        self.ui_auto_process_check_box.setShortcut(u"")
#endif // QT_CONFIG(shortcut)
        self.ui_auto_process_check_box.setCheckable(True)
        self.ui_auto_process_check_box.setAutoRepeatDelay(10)
        self.ui_status_label = QLabel(self.groupBox_10)
        self.ui_status_label.setObjectName(u"ui_status_label")
        self.ui_status_label.setGeometry(QRect(10, 100, 81, 51))
        font2 = QFont()
        font2.setPointSize(12)
        self.ui_status_label.setFont(font2)
        self.ui_status_label.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.ui_status_label.setStyleSheet(u"border: 1px solid #ccc;\n"
"border-radius: 3px;\n"
"\n"
"")
        self.ui_status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.ui_sum_ok_label = QLabel(self.groupBox_10)
        self.ui_sum_ok_label.setObjectName(u"ui_sum_ok_label")
        self.ui_sum_ok_label.setGeometry(QRect(10, 160, 81, 31))
        font3 = QFont()
        font3.setPointSize(8)
        font3.setBold(True)
        self.ui_sum_ok_label.setFont(font3)
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
        self.ui_sum_ng_label.setGeometry(QRect(10, 210, 81, 31))
        self.ui_sum_ng_label.setFont(font3)
        self.ui_sum_ng_label.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.ui_sum_ng_label.setStyleSheet(u"background-color:#ccc;\n"
"border-radius: 3px;\n"
"color:red;\n"
"font-weight:bold\n"
"")
        self.ui_sum_ng_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.ui_start_camera_btn = QPushButton(self.groupBox_10)
        self.ui_start_camera_btn.setObjectName(u"ui_start_camera_btn")
        self.ui_start_camera_btn.setGeometry(QRect(10, 270, 81, 31))
        font4 = QFont()
        font4.setPointSize(8)
        font4.setBold(False)
        self.ui_start_camera_btn.setFont(font4)
        self.ui_start_camera_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.ui_start_camera_btn.setStyleSheet(u"")
        self.ui_start_camera_btn.setIconSize(QSize(18, 18))
        self.ui_stop_camera_btn = QPushButton(self.groupBox_10)
        self.ui_stop_camera_btn.setObjectName(u"ui_stop_camera_btn")
        self.ui_stop_camera_btn.setGeometry(QRect(10, 310, 81, 31))
        self.ui_stop_camera_btn.setFont(font4)
        self.ui_stop_camera_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.ui_stop_camera_btn.setStyleSheet(u"")
        self.ui_stop_camera_btn.setIconSize(QSize(27, 27))
        self.ui_heat_map_radio_btn = QRadioButton(self.groupBox_10)
        self.ui_heat_map_radio_btn.setObjectName(u"ui_heat_map_radio_btn")
        self.ui_heat_map_radio_btn.setGeometry(QRect(10, 390, 81, 17))
        font5 = QFont()
        font5.setPointSize(7)
        self.ui_heat_map_radio_btn.setFont(font5)
        self.ui_heat_map_radio_btn.setIconSize(QSize(16, 16))
        self.ui_segment_radio_btn = QRadioButton(self.groupBox_10)
        self.ui_segment_radio_btn.setObjectName(u"ui_segment_radio_btn")
        self.ui_segment_radio_btn.setGeometry(QRect(10, 420, 81, 17))
        self.ui_segment_radio_btn.setFont(font5)
        self.line = QFrame(self.groupBox_10)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(10, 370, 81, 20))
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_2 = QFrame(self.groupBox_10)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(10, 250, 81, 20))
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_3 = QFrame(self.groupBox_10)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(10, 80, 81, 20))
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)
        self.ui_open_image_btn = QPushButton(self.groupBox_10)
        self.ui_open_image_btn.setObjectName(u"ui_open_image_btn")
        self.ui_open_image_btn.setGeometry(QRect(10, 460, 75, 24))
        self.line_4 = QFrame(self.groupBox_10)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setGeometry(QRect(10, 440, 81, 20))
        self.line_4.setFrameShape(QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)
        self.ui_debug_check_box = QCheckBox(self.groupBox_10)
        self.ui_debug_check_box.setObjectName(u"ui_debug_check_box")
        self.ui_debug_check_box.setGeometry(QRect(10, 350, 81, 20))
        self.ui_debug_check_box.setMouseTracking(True)

        self.horizontalLayout_3.addWidget(self.groupBox_10)

        self.ui_label_display_video = VideoGraphicsView(self.groupBox_9)
        self.ui_label_display_video.setObjectName(u"ui_label_display_video")

        self.horizontalLayout_3.addWidget(self.ui_label_display_video)


        self.horizontalLayout.addWidget(self.groupBox_9)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(0, 20))
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(30, 16777215))
        font6 = QFont()
        font6.setBold(True)
        self.label.setFont(font6)

        self.horizontalLayout_2.addWidget(self.label)

        self.ui_mac_input = QLineEdit(self.widget_2)
        self.ui_mac_input.setObjectName(u"ui_mac_input")
        self.ui_mac_input.setMinimumSize(QSize(0, 20))
        self.ui_mac_input.setMaximumSize(QSize(260, 30))
        self.ui_mac_input.setStyleSheet(u"background-color: #D6EAF8;   /* T\u00edm \u0111\u1eadm (Indigo) */\n"
"    color: red;                /* Ch\u1eef tr\u1eafng */        /* Ch\u1eef \u0111\u1eadm */\n"
"    border: 1px solid #9370DB;  /* Vi\u1ec1n t\u00edm s\u00e1ng (Medium Purple) */\n"
"    border-radius: 3px;")

        self.horizontalLayout_2.addWidget(self.ui_mac_input)

        self.ui_system_message_label = QLabel(self.widget_2)
        self.ui_system_message_label.setObjectName(u"ui_system_message_label")
        self.ui_system_message_label.setMinimumSize(QSize(0, 20))
        font7 = QFont()
        font7.setPointSize(12)
        font7.setBold(True)
        self.ui_system_message_label.setFont(font7)
        self.ui_system_message_label.setStyleSheet(u"border: 1px dot #ccc")
        self.ui_system_message_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.ui_system_message_label)


        self.verticalLayout.addWidget(self.widget_2)


        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.ui_save_all_config_btn.setText(QCoreApplication.translate("MainWindow", u"Save all config", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("MainWindow", u"Camera", None))
        self.groupBox_10.setTitle(QCoreApplication.translate("MainWindow", u"Info", None))
        self.ui_process_btn.setText(QCoreApplication.translate("MainWindow", u"Process", None))
        self.ui_auto_process_check_box.setText(QCoreApplication.translate("MainWindow", u"Auto", None))
        self.ui_status_label.setText(QCoreApplication.translate("MainWindow", u"STATUS: ...", None))
        self.ui_sum_ok_label.setText(QCoreApplication.translate("MainWindow", u"N OK:", None))
        self.ui_sum_ng_label.setText(QCoreApplication.translate("MainWindow", u"N NG:", None))
        self.ui_start_camera_btn.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.ui_stop_camera_btn.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.ui_heat_map_radio_btn.setText(QCoreApplication.translate("MainWindow", u"Heat map", None))
        self.ui_segment_radio_btn.setText(QCoreApplication.translate("MainWindow", u"Segment", None))
        self.ui_open_image_btn.setText(QCoreApplication.translate("MainWindow", u"Open Image", None))
        self.ui_debug_check_box.setText(QCoreApplication.translate("MainWindow", u"Debug", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"SN", None))
        self.ui_system_message_label.setText(QCoreApplication.translate("MainWindow", u"This is System Message", None))
    # retranslateUi

