#!/usr/bin/env python

import sys
from PySide2.QtWidgets import QApplication, QLabel, QMainWindow, QFileDialog, QSizePolicy
from PySide2.QtCore import QByteArray, Qt
from PySide2.QtGui import QPixmap
import cv2

from ui import Ui_MainWindow
from helpers import to_QImage

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.choose.clicked.connect(self.openFileDialog)

    def openFileDialog(self):
        file = QFileDialog.getOpenFileName(self, 'Open File', '.')[0]
        if file is None or len(file) == 0:
            return

        img = cv2.imread(file, 0)
        edges = cv2.Canny(img,100,200)
        print(file)
        print(img)
        print(edges)

        self.ui.initial.setPixmap(QPixmap.fromImage(to_QImage(img)))
        self.ui.result.setPixmap(QPixmap.fromImage(to_QImage(edges)))

        # self.ui.initial.setScaledContents(True)
        # self.ui.initial.setSizePolicy( QSizePolicy.Ignored, QSizePolicy.Ignored )
        # self.ui.result.setSizePolicy( QSizePolicy.Ignored, QSizePolicy.Ignored );

if __name__ == "__main__":
    app = QApplication(sys.argv)
    print(app.style().metaObject().className())

    main_window = MainWindow()
    main_window.show()
    """
    label = QLabel()

    img = cv2.imread('picture.jpg',0)
    edges = cv2.Canny(img,100,200)

    label.setPixmap(QPixmap.fromImage(toQImage(edges)))

    label.show()
    """
    sys.exit(app.exec_())
