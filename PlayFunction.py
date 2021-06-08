from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPalette
import random
import traceback


class Play:

    def __init__(self, t):
        super().__init__()
        self.t = t

    def initnext(self):  # 下一块显示
        if self.t.x == 1 or self.t.x == 22 or self.t.x == 23 or self.t.x == 24:
            pe = QPalette()
            pe.setColor(QPalette.Window, Qt.blue)
            self.t.slabels[5].setPalette(pe)
            self.t.slabels[6].setPalette(pe)
            self.t.slabels[9].setPalette(pe)
            self.t.slabels[10].setPalette(pe)
            self.t.sposition.append(5)
            self.t.sposition.append(6)
            self.t.sposition.append(9)
            self.t.sposition.append(10)
        elif self.t.x == 2 or self.t.x == 20:
            pe = QPalette()
            pe.setColor(QPalette.Window, Qt.red)
            self.t.slabels[1].setPalette(pe)
            self.t.slabels[5].setPalette(pe)
            self.t.slabels[9].setPalette(pe)
            self.t.slabels[13].setPalette(pe)
            self.t.sposition.append(1)
            self.t.sposition.append(5)
            self.t.sposition.append(9)
            self.t.sposition.append(13)
        elif self.t.x == 3 or self.t.x == 21:
            pe = QPalette()
            pe.setColor(QPalette.Window, Qt.red)
            self.t.slabels[4].setPalette(pe)
            self.t.slabels[5].setPalette(pe)
            self.t.slabels[6].setPalette(pe)
            self.t.slabels[7].setPalette(pe)
            self.t.sposition.append(4)
            self.t.sposition.append(5)
            self.t.sposition.append(6)
            self.t.sposition.append(7)
        elif self.t.x == 4 or self.t.x == 25:
            pe = QPalette()
            pe.setColor(QPalette.Window, Qt.green)
            self.t.slabels[2].setPalette(pe)
            self.t.slabels[6].setPalette(pe)
            self.t.slabels[5].setPalette(pe)
            self.t.slabels[9].setPalette(pe)
            self.t.sposition.append(2)
            self.t.sposition.append(5)
            self.t.sposition.append(6)
            self.t.sposition.append(9)
        elif self.t.x == 5 or self.t.x == 26:
            pe = QPalette()
            pe.setColor(QPalette.Window, Qt.green)
            self.t.slabels[4].setPalette(pe)
            self.t.slabels[5].setPalette(pe)
            self.t.slabels[9].setPalette(pe)
            self.t.slabels[10].setPalette(pe)
            self.t.sposition.append(4)
            self.t.sposition.append(5)
            self.t.sposition.append(9)
            self.t.sposition.append(10)
        elif self.t.x == 6 or self.t.x == 27:
            pe = QPalette()
            pe.setColor(QPalette.Window, Qt.darkGreen)
            self.t.slabels[1].setPalette(pe)
            self.t.slabels[5].setPalette(pe)
            self.t.slabels[6].setPalette(pe)
            self.t.slabels[10].setPalette(pe)
            self.t.sposition.append(1)
            self.t.sposition.append(5)
            self.t.sposition.append(6)
            self.t.sposition.append(10)
        elif self.t.x == 7 or self.t.x == 28:
            pe = QPalette()
            pe.setColor(QPalette.Window, Qt.darkGreen)
            self.t.slabels[8].setPalette(pe)
            self.t.slabels[9].setPalette(pe)
            self.t.slabels[5].setPalette(pe)
            self.t.slabels[6].setPalette(pe)
            self.t.sposition.append(5)
            self.t.sposition.append(6)
            self.t.sposition.append(8)
            self.t.sposition.append(9)
        elif self.t.x == 8:
            pe = QPalette()
            pe.setColor(QPalette.Window, Qt.darkMagenta)
            self.t.slabels[4].setPalette(pe)
            self.t.slabels[5].setPalette(pe)
            self.t.slabels[6].setPalette(pe)
            self.t.slabels[8].setPalette(pe)
            self.t.sposition.append(4)
            self.t.sposition.append(5)
            self.t.sposition.append(6)
            self.t.sposition.append(8)
        elif self.t.x == 9:
            pe = QPalette()
            pe.setColor(QPalette.Window, Qt.darkMagenta)
            self.t.slabels[1].setPalette(pe)
            self.t.slabels[5].setPalette(pe)
            self.t.slabels[9].setPalette(pe)
            self.t.slabels[10].setPalette(pe)
            self.t.sposition.append(1)
            self.t.sposition.append(5)
            self.t.sposition.append(9)
            self.t.sposition.append(10)
        elif self.t.x == 10:
            pe = QPalette()
            pe.setColor(QPalette.Window, Qt.darkMagenta)
            self.t.slabels[6].setPalette(pe)
            self.t.slabels[8].setPalette(pe)
            self.t.slabels[9].setPalette(pe)
            self.t.slabels[10].setPalette(pe)
            self.t.sposition.append(6)
            self.t.sposition.append(8)
            self.t.sposition.append(9)
            self.t.sposition.append(10)
        elif self.t.x == 11:
            pe = QPalette()
            pe.setColor(QPalette.Window, Qt.darkMagenta)
            self.t.slabels[1].setPalette(pe)
            self.t.slabels[2].setPalette(pe)
            self.t.slabels[6].setPalette(pe)
            self.t.slabels[10].setPalette(pe)
            self.t.sposition.append(1)
            self.t.sposition.append(2)
            self.t.sposition.append(6)
            self.t.sposition.append(10)
        elif self.t.x == 12:
            pe = QPalette()
            pe.setColor(QPalette.Window, Qt.magenta)
            self.t.slabels[4].setPalette(pe)
            self.t.slabels[5].setPalette(pe)
            self.t.slabels[6].setPalette(pe)
            self.t.slabels[10].setPalette(pe)
            self.t.sposition.append(4)
            self.t.sposition.append(5)
            self.t.sposition.append(6)
            self.t.sposition.append(10)
        elif self.t.x == 13:
            pe = QPalette()
            pe.setColor(QPalette.Window, Qt.magenta)
            self.t.slabels[1].setPalette(pe)
            self.t.slabels[2].setPalette(pe)
            self.t.slabels[5].setPalette(pe)
            self.t.slabels[9].setPalette(pe)
            self.t.sposition.append(1)
            self.t.sposition.append(2)
            self.t.sposition.append(5)
            self.t.sposition.append(9)
        elif self.t.x == 14:
            pe = QPalette()
            pe.setColor(QPalette.Window, Qt.magenta)
            self.t.slabels[4].setPalette(pe)
            self.t.slabels[8].setPalette(pe)
            self.t.slabels[9].setPalette(pe)
            self.t.slabels[10].setPalette(pe)
            self.t.sposition.append(4)
            self.t.sposition.append(8)
            self.t.sposition.append(9)
            self.t.sposition.append(10)
        elif self.t.x == 15:
            pe = QPalette()
            pe.setColor(QPalette.Window, Qt.magenta)
            self.t.slabels[2].setPalette(pe)
            self.t.slabels[9].setPalette(pe)
            self.t.slabels[6].setPalette(pe)
            self.t.slabels[10].setPalette(pe)
            self.t.sposition.append(2)
            self.t.sposition.append(6)
            self.t.sposition.append(9)
            self.t.sposition.append(10)
        elif self.t.x == 16:
            pe = QPalette()
            pe.setColor(QPalette.Window, Qt.yellow)
            self.t.slabels[5].setPalette(pe)
            self.t.slabels[8].setPalette(pe)
            self.t.slabels[9].setPalette(pe)
            self.t.slabels[10].setPalette(pe)
            self.t.sposition.append(5)
            self.t.sposition.append(8)
            self.t.sposition.append(9)
            self.t.sposition.append(10)
        elif self.t.x == 17:
            pe = QPalette()
            pe.setColor(QPalette.Window, Qt.yellow)
            self.t.slabels[5].setPalette(pe)
            self.t.slabels[2].setPalette(pe)
            self.t.slabels[6].setPalette(pe)
            self.t.slabels[10].setPalette(pe)
            self.t.sposition.append(2)
            self.t.sposition.append(5)
            self.t.sposition.append(6)
            self.t.sposition.append(10)
        elif self.t.x == 18:
            pe = QPalette()
            pe.setColor(QPalette.Window, Qt.yellow)
            self.t.slabels[4].setPalette(pe)
            self.t.slabels[5].setPalette(pe)
            self.t.slabels[6].setPalette(pe)
            self.t.slabels[9].setPalette(pe)
            self.t.sposition.append(4)
            self.t.sposition.append(5)
            self.t.sposition.append(6)
            self.t.sposition.append(9)
        elif self.t.x == 19:
            pe = QPalette()
            pe.setColor(QPalette.Window, Qt.yellow)
            self.t.slabels[1].setPalette(pe)
            self.t.slabels[5].setPalette(pe)
            self.t.slabels[6].setPalette(pe)
            self.t.slabels[9].setPalette(pe)
            self.t.sposition.append(1)
            self.t.sposition.append(5)
            self.t.sposition.append(6)
            self.t.sposition.append(9)

    def init(self, m):  # 游戏区域每次初始块的选择与显示
        if m == 1 or m == 22 or m == 23 or m == 24:
            if self.t.judgelabel[5] == 0 and self.t.judgelabel[6] == 0 \
                    and self.t.judgelabel[17] == 0 and self.t.judgelabel[18] == 0:
                pe = QPalette()
                pe.setColor(QPalette.Window, Qt.blue)
                self.t.position.append(5)
                self.t.position.append(6)
                self.t.position.append(17)
                self.t.position.append(18)
                self.t.judgelabel[5] = 1
                self.t.judgelabel[6] = 1
                self.t.judgelabel[17] = 1
                self.t.judgelabel[18] = 1
                self.t.labels[5].setPalette(pe)
                self.t.labels[6].setPalette(pe)
                self.t.labels[17].setPalette(pe)
                self.t.labels[18].setPalette(pe)
                  # 存每块的颜色
                self.t.pe.setColor(QPalette.Window, Qt.blue)
            else:
                self.t.showresult()
        elif m == 2 or m == 20:
            if self.t.judgelabel[5] == 0 and self.t.judgelabel[17] == 0 \
                    and self.t.judgelabel[29] == 0 and self.t.judgelabel[41] == 0:
                pe = QPalette()
                pe.setColor(QPalette.Window, Qt.red)
                self.t.labels[5].setPalette(pe)
                self.t.labels[17].setPalette(pe)
                self.t.labels[29].setPalette(pe)
                self.t.labels[41].setPalette(pe)
                self.t.judgelabel[5] = 1
                self.t.judgelabel[17] = 1
                self.t.judgelabel[29] = 1
                self.t.judgelabel[41] = 1
                self.t.position.append(5)
                self.t.position.append(17)
                self.t.position.append(29)
                self.t.position.append(41)
                self.t.flagsticks = True
                
                self.t.pe.setColor(QPalette.Window, Qt.red)
        elif m == 3 or m == 21:
            if self.t.judgelabel[5] == 0 and self.t.judgelabel[6] == 0 \
                    and self.t.judgelabel[7] == 0 and self.t.judgelabel[8] == 0:
                pe = QPalette()
                pe.setColor(QPalette.Window, Qt.red)
                self.t.labels[5].setPalette(pe)
                self.t.labels[6].setPalette(pe)
                self.t.labels[7].setPalette(pe)
                self.t.labels[8].setPalette(pe)
                self.t.judgelabel[5] = 1
                self.t.judgelabel[6] = 1
                self.t.judgelabel[7] = 1
                self.t.judgelabel[8] = 1
                self.t.position.append(5)
                self.t.position.append(6)
                self.t.position.append(7)
                self.t.position.append(8)
                self.t.flagsticks = True
                
                self.t.pe.setColor(QPalette.Window, Qt.red)
            else:
                self.t.showresult()
        elif m == 4 or m == 25:
            if self.t.judgelabel[6] == 0 and self.t.judgelabel[17] == 0 \
                    and self.t.judgelabel[29] == 0 and self.t.judgelabel[18] == 0:
                pe = QPalette()
                pe.setColor(QPalette.Window, Qt.green)
                self.t.labels[6].setPalette(pe)
                self.t.labels[18].setPalette(pe)
                self.t.labels[17].setPalette(pe)
                self.t.labels[29].setPalette(pe)
                self.t.judgelabel[6] = 1
                self.t.judgelabel[17] = 1
                self.t.judgelabel[18] = 1
                self.t.judgelabel[29] = 1
                self.t.position.append(6)
                self.t.position.append(17)
                self.t.position.append(18)
                self.t.position.append(29)
                
                self.t.pe.setColor(QPalette.Window, Qt.green)
            else:
                self.t.showresult()
        elif m == 5 or m == 26:
            if self.t.judgelabel[5] == 0 and self.t.judgelabel[4] == 0 \
                    and self.t.judgelabel[17] == 0 and self.t.judgelabel[18] == 0:
                pe = QPalette()
                pe.setColor(QPalette.Window, Qt.green)
                self.t.labels[4].setPalette(pe)
                self.t.labels[5].setPalette(pe)
                self.t.labels[17].setPalette(pe)
                self.t.labels[18].setPalette(pe)
                self.t.judgelabel[4] = 1
                self.t.judgelabel[5] = 1
                self.t.judgelabel[17] = 1
                self.t.judgelabel[18] = 1
                self.t.position.append(4)
                self.t.position.append(5)
                self.t.position.append(17)
                self.t.position.append(18)
                
                self.t.pe.setColor(QPalette.Window, Qt.green)
            else:
                self.t.showresult()
        elif m == 6 or m == 27:
            if self.t.judgelabel[5] == 0 and self.t.judgelabel[17] == 0 \
                    and self.t.judgelabel[18] == 0 and self.t.judgelabel[30] == 0:
                pe = QPalette()
                pe.setColor(QPalette.Window, Qt.darkGreen)
                self.t.labels[5].setPalette(pe)
                self.t.labels[17].setPalette(pe)
                self.t.labels[18].setPalette(pe)
                self.t.labels[30].setPalette(pe)
                self.t.judgelabel[5] = 1
                self.t.judgelabel[17] = 1
                self.t.judgelabel[18] = 1
                self.t.judgelabel[30] = 1
                self.t.position.append(5)
                self.t.position.append(17)
                self.t.position.append(18)
                self.t.position.append(30)
                self.t.pe.setColor(QPalette.Window, Qt.darkGreen)
            else:
                self.t.showresult()
        elif m == 7 or m == 28:
            if self.t.judgelabel[5] == 0 and self.t.judgelabel[17] == 0 \
                    and self.t.judgelabel[6] == 0 and self.t.judgelabel[16] == 0:
                pe = QPalette()
                pe.setColor(QPalette.Window, Qt.darkGreen)
                self.t.labels[5].setPalette(pe)
                self.t.labels[6].setPalette(pe)
                self.t.labels[17].setPalette(pe)
                self.t.labels[16].setPalette(pe)
                self.t.judgelabel[5] = 1
                self.t.judgelabel[6] = 1
                self.t.judgelabel[17] = 1
                self.t.judgelabel[16] = 1
                self.t.position.append(5)
                self.t.position.append(6)
                self.t.position.append(16)
                self.t.position.append(17)
                
                self.t.pe.setColor(QPalette.Window, Qt.darkGreen)
            else:
                self.t.showresult()
        elif m == 8:
            if self.t.judgelabel[5] == 0 and self.t.judgelabel[4] == 0 \
                    and self.t.judgelabel[6] == 0 and self.t.judgelabel[16] == 0:
                pe = QPalette()
                pe.setColor(QPalette.Window, Qt.darkMagenta)
                self.t.labels[4].setPalette(pe)
                self.t.labels[5].setPalette(pe)
                self.t.labels[6].setPalette(pe)
                self.t.labels[16].setPalette(pe)
                self.t.judgelabel[4] = 1
                self.t.judgelabel[5] = 1
                self.t.judgelabel[6] = 1
                self.t.judgelabel[16] = 1
                self.t.position.append(4)
                self.t.position.append(5)
                self.t.position.append(6)
                self.t.position.append(16)
                
                self.t.pe.setColor(QPalette.Window, Qt.darkMagenta)
            else:
                self.t.showresult()
        elif m == 9:
            if self.t.judgelabel[5] == 0 and self.t.judgelabel[17] == 0 \
                    and self.t.judgelabel[29] == 0 and self.t.judgelabel[30] == 0:
                pe = QPalette()
                pe.setColor(QPalette.Window, Qt.darkMagenta)
                self.t.labels[5].setPalette(pe)
                self.t.labels[17].setPalette(pe)
                self.t.labels[29].setPalette(pe)
                self.t.labels[30].setPalette(pe)
                self.t.judgelabel[5] = 1
                self.t.judgelabel[17] = 1
                self.t.judgelabel[29] = 1
                self.t.judgelabel[30] = 1
                self.t.position.append(5)
                self.t.position.append(17)
                self.t.position.append(29)
                self.t.position.append(30)
                
                self.t.pe.setColor(QPalette.Window, Qt.darkMagenta)
            else:
                self.t.showresult()
        elif m == 10:
            if self.t.judgelabel[6] == 0 and self.t.judgelabel[17] == 0 \
                    and self.t.judgelabel[16] == 0 and self.t.judgelabel[18] == 0:
                pe = QPalette()
                pe.setColor(QPalette.Window, Qt.darkMagenta)
                self.t.labels[6].setPalette(pe)
                self.t.labels[16].setPalette(pe)
                self.t.labels[17].setPalette(pe)
                self.t.labels[18].setPalette(pe)
                self.t.judgelabel[6] = 1
                self.t.judgelabel[16] = 1
                self.t.judgelabel[17] = 1
                self.t.judgelabel[18] = 1
                self.t.position.append(6)
                self.t.position.append(16)
                self.t.position.append(17)
                self.t.position.append(18)
                
                self.t.pe.setColor(QPalette.Window, Qt.darkMagenta)
            else:
                self.t.showresult()
        elif m == 11:
            if self.t.judgelabel[5] == 0 and self.t.judgelabel[6] == 0 \
                    and self.t.judgelabel[18] == 0 and self.t.judgelabel[30] == 0:
                pe = QPalette()
                pe.setColor(QPalette.Window, Qt.darkMagenta)
                self.t.labels[5].setPalette(pe)
                self.t.labels[6].setPalette(pe)
                self.t.labels[18].setPalette(pe)
                self.t.labels[30].setPalette(pe)
                self.t.judgelabel[5] = 1
                self.t.judgelabel[6] = 1
                self.t.judgelabel[18] = 1
                self.t.judgelabel[30] = 1
                self.t.position.append(5)
                self.t.position.append(6)
                self.t.position.append(18)
                self.t.position.append(30)
                
                self.t.pe.setColor(QPalette.Window, Qt.darkMagenta)
            else:
                self.t.showresult()
        elif m == 12:
            if self.t.judgelabel[5] == 0 and self.t.judgelabel[4] == 0 \
                    and self.t.judgelabel[6] == 0 and self.t.judgelabel[18] == 0:
                pe = QPalette()
                pe.setColor(QPalette.Window, Qt.magenta)
                self.t.labels[4].setPalette(pe)
                self.t.labels[5].setPalette(pe)
                self.t.labels[6].setPalette(pe)
                self.t.labels[18].setPalette(pe)
                self.t.judgelabel[4] = 1
                self.t.judgelabel[5] = 1
                self.t.judgelabel[6] = 1
                self.t.judgelabel[18] = 1
                self.t.position.append(4)
                self.t.position.append(5)
                self.t.position.append(6)
                self.t.position.append(18)
                
                self.t.pe.setColor(QPalette.Window, Qt.magenta)
        elif m == 13:
            if self.t.judgelabel[5] == 0 and self.t.judgelabel[17] == 0 \
                    and self.t.judgelabel[29] == 0 and self.t.judgelabel[6] == 0:
                pe = QPalette()
                pe.setColor(QPalette.Window, Qt.magenta)
                self.t.labels[5].setPalette(pe)
                self.t.labels[6].setPalette(pe)
                self.t.labels[17].setPalette(pe)
                self.t.labels[29].setPalette(pe)
                self.t.judgelabel[5] = 1
                self.t.judgelabel[6] = 1
                self.t.judgelabel[17] = 1
                self.t.judgelabel[29] = 1
                self.t.position.append(5)
                self.t.position.append(6)
                self.t.position.append(17)
                self.t.position.append(29)
                
                self.t.pe.setColor(QPalette.Window, Qt.magenta)
            else:
                self.t.showresult()
        elif m == 14:
            if self.t.judgelabel[5] == 0 and self.t.judgelabel[17] == 0 \
                    and self.t.judgelabel[18] == 0 and self.t.judgelabel[19] == 0:
                pe = QPalette()
                pe.setColor(QPalette.Window, Qt.magenta)
                self.t.labels[5].setPalette(pe)
                self.t.labels[17].setPalette(pe)
                self.t.labels[18].setPalette(pe)
                self.t.labels[19].setPalette(pe)
                self.t.judgelabel[5] = 1
                self.t.judgelabel[17] = 1
                self.t.judgelabel[18] = 1
                self.t.judgelabel[19] = 1
                self.t.position.append(5)
                self.t.position.append(17)
                self.t.position.append(18)
                self.t.position.append(19)
                
                self.t.pe.setColor(QPalette.Window, Qt.magenta)
            else:
                self.t.showresult()
        elif m == 15:
            if self.t.judgelabel[5] == 0 and self.t.judgelabel[17] == 0 \
                    and self.t.judgelabel[29] == 0 and self.t.judgelabel[28] == 0:
                pe = QPalette()
                pe.setColor(QPalette.Window, Qt.magenta)
                self.t.labels[5].setPalette(pe)
                self.t.labels[17].setPalette(pe)
                self.t.labels[28].setPalette(pe)
                self.t.labels[29].setPalette(pe)
                self.t.judgelabel[5] = 1
                self.t.judgelabel[17] = 1
                self.t.judgelabel[28] = 1
                self.t.judgelabel[29] = 1
                self.t.position.append(5)
                self.t.position.append(17)
                self.t.position.append(28)
                self.t.position.append(29)
                
                self.t.pe.setColor(QPalette.Window, Qt.magenta)
            else:
                self.t.showresult()
        elif m == 16:
            if self.t.judgelabel[5] == 0 and self.t.judgelabel[17] == 0 \
                    and self.t.judgelabel[18] == 0 and self.t.judgelabel[16] == 0:
                pe = QPalette()
                pe.setColor(QPalette.Window, Qt.yellow)
                self.t.labels[5].setPalette(pe)
                self.t.labels[17].setPalette(pe)
                self.t.labels[18].setPalette(pe)
                self.t.labels[16].setPalette(pe)
                self.t.judgelabel[5] = 1
                self.t.judgelabel[17] = 1
                self.t.judgelabel[18] = 1
                self.t.judgelabel[16] = 1
                self.t.position.append(5)
                self.t.position.append(16)
                self.t.position.append(17)
                self.t.position.append(18)
                
                self.t.pe.setColor(QPalette.Window, Qt.yellow)
            else:
                self.t.showresult()
        elif m == 17:
            if self.t.judgelabel[5] == 0 and self.t.judgelabel[17] == 0 \
                    and self.t.judgelabel[29] == 0 and self.t.judgelabel[16] == 0:
                pe = QPalette()
                pe.setColor(QPalette.Window, Qt.yellow)
                self.t.labels[5].setPalette(pe)
                self.t.labels[17].setPalette(pe)
                self.t.labels[16].setPalette(pe)
                self.t.labels[29].setPalette(pe)
                self.t.judgelabel[5] = 1
                self.t.judgelabel[17] = 1
                self.t.judgelabel[16] = 1
                self.t.judgelabel[29] = 1
                self.t.position.append(5)
                self.t.position.append(16)
                self.t.position.append(17)
                self.t.position.append(29)
                
                self.t.pe.setColor(QPalette.Window, Qt.yellow)
            else:
                self.t.showresult()
        elif m == 18:
            if self.t.judgelabel[5] == 0 and self.t.judgelabel[17] == 0 \
                    and self.t.judgelabel[4] == 0 and self.t.judgelabel[6] == 0:
                pe = QPalette()
                pe.setColor(QPalette.Window, Qt.yellow)
                self.t.labels[4].setPalette(pe)
                self.t.labels[5].setPalette(pe)
                self.t.labels[6].setPalette(pe)
                self.t.labels[17].setPalette(pe)
                self.t.judgelabel[4] = 1
                self.t.judgelabel[5] = 1
                self.t.judgelabel[6] = 1
                self.t.judgelabel[17] = 1
                self.t.position.append(4)
                self.t.position.append(5)
                self.t.position.append(6)
                self.t.position.append(17)
                
                self.t.pe.setColor(QPalette.Window, Qt.yellow)
            else:
                self.t.showresult()
        elif m == 19:
            if self.t.judgelabel[5] == 0 and self.t.judgelabel[17] == 0 \
                    and self.t.judgelabel[29] == 0 and self.t.judgelabel[18] == 0:
                pe = QPalette()
                pe.setColor(QPalette.Window, Qt.yellow)
                self.t.labels[5].setPalette(pe)
                self.t.labels[17].setPalette(pe)
                self.t.labels[18].setPalette(pe)
                self.t.labels[29].setPalette(pe)
                self.t.judgelabel[5] = 1
                self.t.judgelabel[17] = 1
                self.t.judgelabel[18] = 1
                self.t.judgelabel[29] = 1
                self.t.position.append(5)
                self.t.position.append(17)
                self.t.position.append(18)
                self.t.position.append(29)
                
                self.t.pe.setColor(QPalette.Window, Qt.yellow)
            else:
                self.t.showresult()

    def downfunction(self):
        try:
            self.t.mutex.acquire()
            flag = True
            # 找最下块
            positionDown = []  # 存一个块最下单元的坐标
            for i in range(4):
                self.t.columnPosition.append(divmod(self.t.position[i], 12)[1])
            positionDown.append(self.t.position[3])
            if self.t.columnPosition[3] != self.t.columnPosition[2]:
                positionDown.append(self.t.position[2])
            if self.t.columnPosition[1] != self.t.columnPosition[2] and self.t.columnPosition[1] != self.t.columnPosition[
                3]:
                positionDown.append(self.t.position[1])
            if self.t.columnPosition[0] != self.t.columnPosition[1] and self.t.columnPosition[0] != self.t.columnPosition[2] \
                    and self.t.columnPosition[0] != self.t.columnPosition[3]:
                positionDown.append(self.t.position[0])
            self.t.columnPosition = []
            # 判定是否可以下落
            for i in range(len(positionDown)):
                if positionDown[i] / 12 < 24:  # 所有最下块下方存在区域
                    if self.t.judgelabel[positionDown[i] + 12] != 0:  # 所有最下块下方为空区域
                        flag = False
                        break
                else:
                    flag = False
                    break
            if flag:  # 下落逻辑
                self.t.flagnext = False
                pe = QPalette()
                pe.setColor(QPalette.Window, Qt.gray)
                for i in range(4):
                    self.t.labels[self.t.position[i]].setPalette(pe)
                    self.t.judgelabel[self.t.position[i]] = 0
                    self.t.position[i] += 12
                for i in range(4):
                    self.t.labels[self.t.position[i]].setPalette(self.t.pe)
                    self.t.judgelabel[self.t.position[i]] = 1
            self.t.mutex.release()
        except:
            self.t.mutex.release()

    def spacefunction(self):
        self.t.runspeed = 10

    def leftfunction(self):
        try:
            self.t.mutex.acquire()
            flag = True
            positionLeft = []  # 存一个块的最左单元的坐标
            for i in range(4):
                self.t.rowPosition.append(divmod(self.t.position[i], 12)[0] + 1)
            positionLeft.append(self.t.position[0])  # position值最小的那一块一定是最左块
            if self.t.rowPosition[0] != self.t.rowPosition[1]:
                positionLeft.append(self.t.position[1])
            if self.t.rowPosition[0] != self.t.rowPosition[2] and self.t.rowPosition[1] != self.t.rowPosition[2]:
                positionLeft.append(self.t.position[2])
            if self.t.rowPosition[0] != self.t.rowPosition[3] and self.t.rowPosition[1] != self.t.rowPosition[3]\
                    and self.t.rowPosition[2] != self.t.rowPosition[3]:
                positionLeft.append(self.t.position[3])
            self.t.rowPosition = []
            # 判定是否可左移
            for i in range(len(positionLeft)):
                if positionLeft[i] % 12 > 0:  # 所有最左块左方存在区域
                    if self.t.judgelabel[positionLeft[i] - 1] != 0:  # 所有最左块左方为空区域
                        flag = False
                        break
                else:
                    flag = False
                    break
            if flag:  # 可以左移
                # 左移并更新区域与区域标志
                for i in range(4):
                    pe = QPalette()
                    pe.setColor(QPalette.Window, Qt.gray)
                    self.t.labels[self.t.position[i]].setPalette(pe)  # 原区域涂灰
                    self.t.judgelabel[self.t.position[i]] = 0  # 原区域判定为可行区
                    self.t.position[i] -= 1  # 存此块当前所有坐标
                for i in range(4):
                    self.t.labels[self.t.position[i]].setPalette(self.t.pe)  # 新区域涂成该块的颜色
                    self.t.judgelabel[self.t.position[i]] = 1  # 新区域判定为占用区
            self.t.mutex.release()
        except:
            self.t.mutex.release()
        # 否则什么都不做

    def rightfunction(self):
        try:
            self.t.mutex.acquire()
            flag = True
            positionRight = []  # 存一个块最右单元的坐标
            for i in range(4):
                self.t.rowPosition.append(divmod(self.t.position[i], 12)[0] + 1)
            positionRight.append(self.t.position[3])  # position值最大的那一块一定是最右块
            if self.t.rowPosition[2] != self.t.rowPosition[3]:
                positionRight.append(self.t.position[2])
            if self.t.rowPosition[1] != self.t.rowPosition[3] and self.t.rowPosition[1] != self.t.rowPosition[2]:
                positionRight.append(self.t.position[1])
            if self.t.rowPosition[0] != self.t.rowPosition[1] and self.t.rowPosition[0] != self.t.rowPosition[2]\
                    and self.t.rowPosition[0] != self.t.rowPosition[3]:
                positionRight.append(self.t.position[0])
            self.t.rowPosition = []
            # 判定是否可右移
            for i in range(len(positionRight)):
                if positionRight[i] % 12 < 11:  # 所有最右块右方存在区域
                    if self.t.judgelabel[positionRight[i] + 1] != 0:  # 所有最右块右方为空区域
                        flag = False
                        break
                else:
                    flag = False
                    break
            if flag:  # 可以右移
                # 右移并更新区域与区域标志
                for i in range(4):
                    pe = QPalette()
                    pe.setColor(QPalette.Window, Qt.gray)
                    self.t.labels[self.t.position[i]].setPalette(pe)  # 原区域涂灰
                    self.t.judgelabel[self.t.position[i]] = 0  # 原区域判定为可行区
                    self.t.position[i] += 1  # 存此块当前所有坐标
                for i in range(4):  # 原区域变灰与新区域更新不能交叉执行，因为可能存在重叠
                    self.t.labels[self.t.position[i]].setPalette(self.t.pe)  # 新区域涂成该块的颜色
                    self.t.judgelabel[self.t.position[i]] = 1  # 新区域判定为占用区
            self.t.mutex.release()
        except:
            self.t.mutex.release()
        # 否则什么都不做

    def upfunction(self):
        try:
            self.t.mutex.acquire()
            flag = True
            if self.t.flagsticks:  # 木棒的判定与平移与众不同
                upleft = self.t.position[0]
                if 2 < divmod(upleft+3, 12)[1] <= 11 and divmod(upleft+36, 12)[0] <= 24:  # 区域存在
                    for i in range(4):
                        for j in range(4):
                            if self.t.judgelabel[upleft+j+12*i] != 1:  # 区域无块的单元存在
                                continue
                            elif upleft+j+12*i == self.t.position[0] or upleft+j+12*i == self.t.position[1]\
                                    or upleft+j+12*i == self.t.position[2] or upleft+j+12*i == self.t.position[3]:
                                continue
                            else:  # 区域有别的块的单元存在
                                flag = False
                else:
                    flag = False
                if flag:
                    pe = QPalette()
                    pe.setColor(QPalette.Window, Qt.gray)
                    if self.t.position[0] + 1 == self.t.position[1]:  # 横4️单元
                        for i in range(1, 4):  # 木棒旋转区域不重叠所以可以交叉执行
                            self.t.judgelabel[self.t.position[i]] = 0
                            self.t.labels[self.t.position[i]].setPalette(pe)
                            self.t.judgelabel[self.t.position[0]+12*i] = 1
                            self.t.labels[self.t.position[0]+12*i].setPalette(self.t.pe)
                            self.t.position[i] = self.t.position[0] + i*12
                    else:  # 竖4单元
                        for i in range(1, 4):
                            self.t.judgelabel[self.t.position[i]] = 0
                            self.t.labels[self.t.position[i]].setPalette(pe)
                            self.t.judgelabel[self.t.position[0]+i] = 1
                            self.t.labels[self.t.position[0]+i].setPalette(self.t.pe)
                            self.t.position[i] = self.t.position[0] + i
                self.t.mutex.release()
            else:  # 其他所有块的判定
                for i in range(len(self.t.position)):
                    self.t.rowPosition.append(divmod(self.t.position[i], 12)[0])
                    self.t.columnPosition.append(divmod(self.t.position[i], 12)[1])
                upleft = self.t.rowPosition[self.t.rowPosition.index(min(self.t.rowPosition))] * 12 \
                    + self.t.columnPosition[self.t.columnPosition.index(min(self.t.columnPosition))]
                self.t.columnPosition = []
                self.t.rowPosition = []
                if 1 < divmod(upleft+2, 12)[1] <= 11 and divmod(upleft+24, 12)[0] <= 24:  # 区域存在
                    for i in range(3):
                        for j in range(3):
                            if self.t.judgelabel[upleft+j+12*i] != 1:  # 区域无块单元存在
                                continue
                            elif upleft+j+12*i == self.t.position[0] or upleft+j+12*i == self.t.position[1]\
                                    or upleft+j+12*i == self.t.position[2] or upleft+j+12*i == self.t.position[3]:
                                continue
                            else:  # 区域有别的块的单元存在
                                flag = False
                else:
                    flag = False
                if flag:  # 可以旋转
                    pe = QPalette()
                    pe.setColor(QPalette.Window, Qt.gray)
                    rotatevalue = [24, 11, -2, 13, 0, -13, 2, -11, -24]
                    k = 0
                    m = 0
                    for i in range(3):  # 原始区域已重置完毕且新区域位置坐标已经存储
                        for j in range(3):
                            if self.t.judgelabel[upleft+i*12+j] == 1:
                                self.t.position[m] += rotatevalue[k]
                                self.t.judgelabel[upleft+i*12+j] = 0
                                self.t.labels[upleft+i*12+j].setPalette(pe)
                                k += 1
                                m += 1
                            else:
                                k += 1
                    self.t.position.sort()
                    for i in range(4):
                        self.t.labels[self.t.position[i]].setPalette(self.t.pe)
                        self.t.judgelabel[self.t.position[i]] = 1
                self.t.mutex.release()
        except:
            traceback.print_exc()
            self.t.mutex.release()

    def calscore(self, t):
        self.t.score1 += 100 * t * t
        self.t.score.setText(str(self.t.score1))

    def gameprocess(self):  # 游戏主过程
        try:
            flag = True
            subposition = []
            if self.t.flagnext:  # 一次下落过程结束，下一块到来
                self.t.flagnext = False
                if self.t.first:
                    m = random.randint(1, 28)
                    self.init(m)
                    self.t.first = False
                    self.t.x = random.randint(1, 28)
                    self.initnext()
                else:
                    self.init(self.t.x)
                    self.t.x = random.randint(1, 28)
                    pe = QPalette()
                    pe.setColor(QPalette.Window, Qt.gray)
                    for i in range(4):
                        self.t.slabels[self.t.sposition[i]].setPalette(pe)
                    self.t.sposition = []
                    self.initnext()
            if self.t.flagOver:
                QTimer.singleShot(self.t.runspeed, self.gameprocess)
                self.t.mutex.acquire()
            # 找最下块
            positionDown = []  # 存一个块最下单元的坐标
            for i in range(4):
                self.t.columnPosition.append(divmod(self.t.position[i], 12)[1])
            positionDown.append(self.t.position[3])
            if self.t.columnPosition[3] != self.t.columnPosition[2]:
                positionDown.append(self.t.position[2])
            if self.t.columnPosition[1] != self.t.columnPosition[2] and self.t.columnPosition[1] != self.t.columnPosition[3]:
                positionDown.append(self.t.position[1])
            if self.t.columnPosition[0] != self.t.columnPosition[1] and self.t.columnPosition[0] != self.t.columnPosition[2]\
                    and self.t.columnPosition[0] != self.t.columnPosition[3]:
                positionDown.append(self.t.position[0])
            self.t.columnPosition = []
            # 判定是否可以下落
            for i in range(len(positionDown)):
                if positionDown[i]/12 < 24:  # 所有最下块下方存在区域
                    if self.t.judgelabel[positionDown[i] + 12] != 0:  # 所有最下块下方为空区域
                        flag = False
                        break
                else:
                    flag = False
                    break
            if flag:  # 下落逻辑
                self.t.flagnext = False
                pe = QPalette()
                pe.setColor(QPalette.Window, Qt.gray)
                for i in range(4):
                    self.t.labels[self.t.position[i]].setPalette(pe)
                    self.t.judgelabel[self.t.position[i]] = 0
                    self.t.position[i] += 12
                for i in range(4):
                    self.t.labels[self.t.position[i]].setPalette(self.t.pe)
                    self.t.judgelabel[self.t.position[i]] = 1
                self.t.mutex.release()
            else:  # 不能继续下落， 减行判断，游戏是否结束的判断
                for i in range(25):
                    for j in range(12):
                        if self.t.judgelabel[j+i*12] == 0:
                            self.t.flagsub = False
                    if self.t.flagsub:
                        subposition.append(i)  # i代表要减的行
                    self.t.flagsub = True
                if subposition:  # 列表不为空减行
                    # 减行后更新区域并计算得分
                    position = []
                    pe = QPalette()
                    pe.setColor(QPalette.Window, Qt.gray)
                    self.calscore(len(subposition))
                    for i in range(len(subposition)):  # 所有减掉行上方的占有区向下平移
                        for j in range(subposition[i]*12):
                            if self.t.judgelabel[j] == 1:
                                position.append(j+12)
                                self.t.judgelabel[j] = 0
                                self.t.labels[j].setPalette(pe)
                        for j in range(subposition[i]*12, subposition[i]*12+12):  # 被减行区域重置
                            self.t.judgelabel[j] = 0
                            self.t.labels[j].setPalette(pe)
                        pe.setColor(QPalette.Window, Qt.darkBlue)
                        for j in range(len(position)):
                            self.t.labels[position[j]].setPalette(pe)
                            self.t.judgelabel[position[j]] = 1
                        pe.setColor(QPalette.Window, Qt.gray)
                        position = []
                    self.t.flagsticks = False
                    self.t.flagnext = True
                    self.t.position = []
                    if self.t.score1 < 2500:
                        self.t.runspeed = 500
                    elif self.t.score1 < 5000:
                        self.t.runspeed = 400
                    elif self.t.score1 < 7500:
                        self.t.runspeed = 300
                    elif self.t.score1 < 10000:
                        self.t.runspeed = 200
                    elif self.t.score1 < 15000:
                        self.t.runspeed = 100
                    else:
                        self.t.runspeed = 50
                    if self.t.flagOver:
                        self.t.mutex.release()
                else:  # 判断游戏是否结束并修改颜色
                    pe = QPalette()
                    pe.setColor(QPalette.Window, Qt.darkBlue)
                    for i in range(300):
                        if self.t.judgelabel[i] == 1:
                            self.t.labels[i].setPalette(pe)
                    self.t.flagnext = True
                    self.t.position = []
                    self.t.flagsticks = False
                    if self.t.score1 < 2500:
                        self.t.runspeed = 500
                    elif self.t.score1 < 5000:
                        self.t.runspeed = 400
                    elif self.t.score1 < 7500:
                        self.t.runspeed = 300
                    elif self.t.score1 < 10000:
                        self.t.runspeed = 200
                    elif self.t.score1 < 15000:
                        self.t.runspeed = 100
                    else:
                        self.t.runspeed = 50
                    if self.t.flagOver:
                        self.t.mutex.release()
        except:
            traceback.print_exc()
            self.t.flagOver = False
            self.t.showresult()


# 减行逻辑有问题；right键和空格在右方区域狂按时会出错，left键无此问题；pause按钮有问题；游戏结束提示框功能未做














