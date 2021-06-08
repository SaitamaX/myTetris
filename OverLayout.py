from PyQt5.QtWidgets import (QWidget, QPushButton, QVBoxLayout, QLabel, QDesktopWidget)
from PyQt5.QtGui import QPalette
import threading
from PyQt5.QtCore import *


class Over(QWidget):

    def __init__(self, m):
        super().__init__()
        self.m = m
        self.time = QLabel('用时：')
        self.score = QLabel('得分：')

    def initUI(self, k):
        self.time.setText('用时：' + self.m.lasttime)
        self.score.setText('得分：' + str(k))
        qbtn = QPushButton('Ok')
        qbtn.clicked.connect(self.restart)
        qbtn.resize(qbtn.sizeHint())
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addWidget(self.time)
        vbox.addWidget(self.score)
        vbox.addWidget(qbtn)
        self.resize(200, 150)
        self.setLayout(vbox)
        self.center()
        self.setWindowTitle('Game Over')
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def restart(self):
        self.m.second = 0
        self.m.minute = 0
        self.m.hour = 0
        self.m.flag = False
        self.m.flagOver = True
        self.m.time.setText('00:00:00')
        self.m.score.setText('0')
        self.m.lasttime = '0'
        self.m.x = 1
        self.m.first = True
        self.m.position = []  # 存各种块的初始下标
        self.m.flagsticks = False  # 木棒比较特殊,一次落下过程后要重置值
        self.m.flagsub = True  # 某行可减标志
        self.m.flagnext = True
        self.m.rowPosition = []  # 存块内每个单元的所在行
        self.m.columnPosition = []  # 存块内每个单元的所在列
        self.m.score1 = 0
        self.m.pe = QPalette()
        self.m.mutex = threading.Lock()
        self.m.flagOver = True
        self.m.runspeed = 500
        self.m.sposition = []
        self.m.start.setEnabled(True)
        pe = QPalette()
        pe.setColor(QPalette.Window, Qt.gray)  # 设置背景颜色
        for i in range(25):
            for j in range(12):
                self.m.labels[i*12+j].setPalette(pe)
                self.m.judgelabel[i*12+j] = 0
        for i in range(4):
            for j in range(4):
                self.m.slabels[i*4+j].setPalette(pe)
        self.close()



