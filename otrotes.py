#!/usr/bin/python
# -*- coding: Utf-8 -*-

import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class Widget(QWidget):
       def __init__(self):
               QWidget.__init__(self)

               hbox=QHBoxLayout()
               self.combo = combo = QComboBox()
               lst=[("a",7),("b",8),("c",5),("d",3),("e",4)]
               for i in lst:
                       combo.addItem(i[0],QVariant(i[1]))
               hbox.addWidget(combo)
               self.connect(combo,SIGNAL("activated(int)"),self.changeItem)
               self.setLayout(hbox)

       def changeItem(self,i):
	       print i
               print self.combo.itemData(i).toInt()[0]

app = QApplication(sys.argv)
main = Widget()
main.show()
sys.exit(app.exec_())
