import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QHBoxLayout,
                             QVBoxLayout, QGridLayout, QApplication, QLabel, QDesktopWidget)
from PyQt5.QtGui import QPalette, QFont, QKeyEvent
from PyQt5.QtCore import *
from PyQt5 import QtCore
from threading import Timer
import threading


class Tlayout(QWidget):
    def __init__(self):
        super().__init__()
        self.x = 1
        self.first = True
        self.position = []  # 存各种块的初始下标
        self.slabels = []
        self.flagsticks = False  # 木棒比较特殊,一次落下过程后要重置值
        self.flagsub = True  # 某行可减标志
        self.flagnext = True
        self.rowPosition = []  # 存块内每个单元的所在行
        self.columnPosition = []  # 存块内每个单元的所在列
        self.score1 = 0
        self.pe = QPalette()
        self.mutex = threading.Lock()
        self.flagOver = True
        self.runspeed = 500
        self.sposition = []
        self.labels = []
        self.judgelabel = []
        self.second = 0
        self.minute = 0
        self.hour = 0
        self.time = QLabel('00:00:00')
        self.lasttime = '0'
        self.score = QLabel('0')
        self.start = QPushButton('Start')
        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        grid = QGridLayout()
        hbox.addLayout(vbox)
        hbox.addLayout(grid)
        Next = QLabel('Next')
        Next.setFont(QFont("隶书", 40, QFont.Fantasy))
        pe = QPalette()
        pe.setColor(QPalette.Window, Qt.white)
        self.time.setAutoFillBackground(True)  # 设置背景充满，为设置背景颜色的必要条件
        self.time.setPalette(pe)
        smallgrid = QGridLayout()
        smallgrid.setSpacing(1)
        pe = QPalette()
        pe.setColor(QPalette.Window, Qt.gray)  # 设置背景颜色
        for i in range(4):
            for j in range(4):
                label = QLabel('')
                label.setAutoFillBackground(True)  # 设置背景充满，为设置背景颜色的必要条件
                label.setPalette(pe)
                smallgrid.addWidget(label, i, j)
                self.slabels.append(label)
        Time = QLabel('  Time：')
        Time.setFont(QFont("宋体", 25, QFont.Black))
        self.time.setFont(QFont("隶书", 20, QFont.Fantasy))
        self.time.setAlignment(Qt.AlignCenter)
        Score = QLabel(' Score：')
        Score.setFont(QFont("宋体", 20, QFont.Black))
        self.score.setAlignment(Qt.AlignCenter)
        pe = QPalette()
        pe.setColor(QPalette.Window, Qt.white)
        self.score.setAutoFillBackground(True)
        self.score.setFont(QFont("隶书", 30, QFont.Fantasy))
        self.score.setPalette(pe)
        blank = QLabel()
        vbox.setSpacing(2)
        vbox.addWidget(Next)
        vbox.addLayout(smallgrid)
        vbox.addWidget(self.start)
        vbox.addWidget(Time)
        vbox.addWidget(self.time)
        vbox.addWidget(Score)
        vbox.addWidget(self.score)
        vbox.addWidget(blank)
        pe = QPalette()
        pe.setColor(QPalette.Window, Qt.gray)  # 设置背景颜色
        for i in range(25):
            for j in range(12):
                label = QLabel('        ')
                label.setAutoFillBackground(True)  # 设置背景充满，为设置背景颜色的必要条件
                label.setPalette(pe)
                grid.addWidget(label, i, j)
                self.labels.append(label)
                self.judgelabel.append(0)
        grid.setSpacing(1)
        self.start.clicked.connect(self.playing)
        self.setLayout(hbox)
        self.center()
        self.resize(510, 750)
        self.setFixedSize(self.width(), self.height())
        self.setWindowFlags(Qt.WindowMinimizeButtonHint)
        self.setWindowTitle('Tetris')
        self.show()

    def keyPressEvent(self, event):
        keyevent = QKeyEvent(event)
        if keyevent.key() == QtCore.Qt.Key_Up:
            play.upfunction()
        if keyevent.key() == QtCore.Qt.Key_Space:
            play.spacefunction()
        if keyevent.key() == QtCore.Qt.Key_Down:
             play.downfunction()
        if keyevent.key() == QtCore.Qt.Key_Left:
            play.leftfunction()
        if keyevent.key() == QtCore.Qt.Key_Right:
            play.rightfunction()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def count(self):
        self.second += 1
        if self.flagOver:
            t1 = Timer(1.0, self.count)
            t1.start()
        self.start.setEnabled(False)
        if self.second > 59:
            self.second = 0
            self.minute += 1
        if self.minute > 59:
            self.hour += 1
            self.minute = 0
        if self.second < 10 and self.minute < 10:
            self.time.setText('0' + str(self.hour) + ':0' + str(self.minute) + ':0' + str(self.second))
            self.lasttime = str(self.hour) + '小时' + str(self.minute) + '分钟' + str(self.second) + '秒'
        elif self.minute < 10 <= self.second:
            self.time.setText('0' + str(self.hour) + ':0' + str(self.minute) + ':' + str(self.second))
            self.lasttime = str(self.hour) + '小时' + str(self.minute) + '分钟' + str(self.second) + '秒'
        elif self.second < 10 <= self.minute:
            self.time.setText('0' + str(self.hour) + ':' + str(self.minute) + ':0' + str(self.second))
            self.lasttime = str(self.hour) + '小时' + str(self.minute) + '分钟' + str(self.second) + '秒'
        elif self.second >= 10 and self.minute >= 10:
            self.time.setText('0' + str(self.hour) + ':' + str(self.minute) + ':' + str(self.second))
            self.lasttime = str(self.hour) + '小时' + str(self.minute) + '分钟' + str(self.second) + '秒'
        if not self.flagOver:
            self.flagOver = False

    def showresult(self):  # 游戏结束，显示结果
        overshow.initUI(self.score1)

    def playing(self):
        threads = []
        timer = threading.Thread(target=play.gameprocess(), args=self)
        threads.append(timer)
        timer = threading.Thread(target=self.count(), args=self)
        threads.append(timer)
        for self.t in threads:
            self.t.setDaemon(True)
            self.t.start()
            self.t.join()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    tlayout = Tlayout()
    from PlayFunction import Play
    from OverLayout import Over
    play = Play(tlayout)
    overshow = Over(tlayout)
    sys.exit(app.exec_())
