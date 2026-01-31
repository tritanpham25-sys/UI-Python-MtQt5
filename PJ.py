# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import random
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import imagee

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 800) 
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # --- LAYOUT TỔNG ---
        self.mainLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.mainLayout.setContentsMargins(30, 20, 30, 20) 
        self.mainLayout.setSpacing(15) 

        # --- HEADER ---
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(26) 
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setText("HỆ THỐNG GIÁM SÁT MÔI TRƯỜNG VÀ ĐIỀU KHIỂN THIẾT BỊ")
        self.label_3.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        self.mainLayout.addWidget(self.label_3)

        self.mainLayout.addSpacing(10) 

        # --- LOGO & TÊN ---
        self.infoLayout = QtWidgets.QHBoxLayout()
        self.infoLayout.addStretch(1)

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setMinimumSize(100, 100)  
        self.label_2.setMaximumSize(300, 300) 
        self.label_2.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.label_2.setStyleSheet("image: url(:/ảnh/Image/Logo HCM-UTE_ 1.png);")
        self.label_2.setScaledContents(True)
        self.infoLayout.addWidget(self.label_2)

        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(22) 
        font.setBold(True)
        self.label.setFont(font)
        self.label.setText("PHẠM TRÍ TÂN - 23119104")
        self.label.setStyleSheet("margin-left: 20px; color: #1f4e79;") 
        self.label.setAlignment(QtCore.Qt.AlignVCenter)
        self.infoLayout.addWidget(self.label)

        self.infoLayout.addStretch(1)
        self.mainLayout.addLayout(self.infoLayout, 1) # Chiếm 1 phần

        self.mainLayout.addSpacing(10)

        # --- PHẦN 3: ĐIỀU KHIỂN (Controls) ---
        self.controlsLayout = QtWidgets.QHBoxLayout()
        self.controlsLayout.setSpacing(40) 
        self.controlsLayout.addStretch(1) 

        # >> Cụm 1: ĐÈN
        self.lightLayout = QtWidgets.QVBoxLayout()
        
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        # [THUỐC MẠNH] Dùng Ignored để ép nó giãn hết cỡ bất chấp kích thước ảnh
        self.label_4.setSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        self.label_4.setScaledContents(True) 
        self.label_4.setStyleSheet("image: url(:/ảnh/Image/bulb_off.png);")
        
        # Cho icon chiếm 8 phần chiều cao của cụm này
        self.lightLayout.addWidget(self.label_4, 8)

        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setMaximum(2)
        self.horizontalSlider.setMinimumWidth(200) 
        self.horizontalSlider.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        self.horizontalSlider.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        
        slider_style = """
            QSlider::groove:horizontal {
                border: 1px solid #999999;
                height: 20px;
                background: #e0e0e0;
                margin: 2px 0;
                border-radius: 10px;
            }
            QSlider::handle:horizontal {
                background: #3498db;
                border: 1px solid #3498db;
                width: 40px; 
                height: 40px;
                margin: -10px 0;
                border-radius: 20px;
            }
        """
        self.horizontalSlider.setStyleSheet(slider_style)
        # Slider chiếm 1 phần chiều cao
        self.lightLayout.addWidget(self.horizontalSlider, 1, QtCore.Qt.AlignHCenter)
        
        self.controlsLayout.addLayout(self.lightLayout, 1)

        # >> Cụm 2: CỬA
        self.doorLayout = QtWidgets.QVBoxLayout()
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        
        # [THUỐC MẠNH] Ignored
        self.label_5.setSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        self.label_5.setScaledContents(True)
        self.label_5.setStyleSheet("image: url(:/ảnh/Image/door_lock1.png);")
        self.doorLayout.addWidget(self.label_5, 8)

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setMinimumSize(220, 65)
        self.pushButton.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setText("LOCK / UNLOCK")
        self.doorLayout.addWidget(self.pushButton, 1, QtCore.Qt.AlignHCenter)
        
        self.controlsLayout.addLayout(self.doorLayout, 1)

        # >> Cụm 3: QUẠT
        self.fanLayout = QtWidgets.QVBoxLayout()
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        
        # [THUỐC MẠNH] Ignored
        self.label_6.setSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        self.label_6.setScaledContents(True)
        self.label_6.setStyleSheet("image: url(:/ảnh/Image/fan_off.png);")
        self.fanLayout.addWidget(self.label_6, 8)

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setMinimumSize(220, 65)
        self.pushButton_2.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setText("ON / OFF")
        self.fanLayout.addWidget(self.pushButton_2, 1, QtCore.Qt.AlignHCenter)
        
        self.controlsLayout.addLayout(self.fanLayout, 1)
        self.controlsLayout.addStretch(1) 

        # [TỶ LỆ] Controls chiếm 5 phần (để Icon có đất diễn), Biểu đồ chiếm 3 phần
        self.mainLayout.addLayout(self.controlsLayout, 5)

        self.mainLayout.addStretch(1)

        # --- BIỂU ĐỒ ---
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.canvas.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.canvas.setMinimumHeight(250) 
        
        self.mainLayout.addWidget(self.canvas, 3)

        # Subplots
        self.ax1 = self.figure.add_subplot(131)
        self.ax2 = self.figure.add_subplot(132)
        self.ax3 = self.figure.add_subplot(133)
        self.figure.subplots_adjust(left=0.06, right=0.96, top=0.88, bottom=0.15, wspace=0.3)

        # --- SETUP CHUNG ---
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)
        MainWindow.setWindowTitle("Hệ Thống Giám Sát IoT")

        # Data & Timer
        self.temp_data = []
        self.hum_data = []
        self.AQI_data = []

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_chart)
        self.timer.start(1500)

        # Stylesheet Nút bấm
        btn_style = """
            QPushButton {
                background-color: #f0f0f0; 
                border-radius: 12px;
                border: 2px solid #bdc3c7;
                font-weight: bold;
                color: #2c3e50;
                font-size: 18px; 
            }
            QPushButton:hover {
                background-color: #e0e0e0;
            }
            QPushButton:checked {
                background-color: #3498db;
                color: white;
                border: 2px solid #2980b9;
            }
        """
        self.pushButton.setStyleSheet(btn_style)
        self.pushButton.setCheckable(True)
        self.pushButton_2.setStyleSheet(btn_style)
        self.pushButton_2.setCheckable(True)

        # Connect
        self.horizontalSlider.valueChanged[int].connect(self.den)
        self.pushButton.clicked.connect(self.door)
        self.pushButton_2.clicked.connect(self.fan)
        
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # --- LOGIC ---
    def den(self, value):   
        if value == 0:
            self.label_4.setStyleSheet("image: url(:/ảnh/Image/bulb_off.png);") 
        elif value ==1:
            self.label_4.setStyleSheet("image: url(:/ảnh/Image/light_on1.png);") 
        elif value ==2:
            self.label_4.setStyleSheet("image: url(:/ảnh/Image/light_on2.png);") 

    def door(self):
        if self.pushButton.isChecked():
            self.label_5.setStyleSheet("image: url(:/ảnh/Image/door_unlock.png);")
        else: 
            self.label_5.setStyleSheet("image: url(:/ảnh/Image/door_lock1.png);")        

    def fan(self):
        if self.pushButton_2.isChecked():
            self.label_6.setStyleSheet("image: url(:/ảnh/Image/fan_on.png);")
        else: 
            self.label_6.setStyleSheet("image: url(:/ảnh/Image/fan_off.png);")        

    def update_chart(self):
        temp = random.randint(20, 35)
        hum = random.randint(60, 90)
        AQI = random.randint(50, 150)
        
        self.temp_data.append(temp) 
        self.hum_data.append(hum)
        self.AQI_data.append(AQI)
    
        if len(self.temp_data) > 10:
             self.temp_data.pop(0)
             self.hum_data.pop(0)
             self.AQI_data.pop(0)

        t_font = {'size': 11, 'weight': 'bold'}
        
        self.ax1.clear()
        self.ax1.plot(self.temp_data, color='#e74c3c', marker='o', linewidth=2)
        self.ax1.set_title("NHIỆT ĐỘ (°C)", fontdict=t_font)
        self.ax1.set_ylim(15, 45)
        self.ax1.grid(True, linestyle='--', alpha=0.5)

        self.ax2.clear()
        self.ax2.plot(self.hum_data, color='#3498db', marker='o', linewidth=2)
        self.ax2.set_title("ĐỘ ẨM (%)", fontdict=t_font)
        self.ax2.set_ylim(0, 100)
        self.ax2.grid(True, linestyle='--', alpha=0.5)

        self.ax3.clear()
        self.ax3.plot(self.AQI_data, color='#2ecc71', marker='o', linewidth=2)
        self.ax3.set_title("KHÔNG KHÍ (AQI)", fontdict=t_font)
        self.ax3.grid(True, linestyle='--', alpha=0.5)

        self.canvas.draw()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())