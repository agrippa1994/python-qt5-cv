#!/usr/bin/env python

import sys

import cv2
from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import QApplication, QMainWindow, QFileDialog
from helpers import to_QImage
from ui import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.choose.clicked.connect(self.open_file_dialog)

    def open_file_dialog(self):
        file = QFileDialog.getOpenFileName(self, 'Open File', '.')[0]
        if file is None or len(file) == 0:
            return

        img = cv2.imread(file, 0)
        edges = cv2.Canny(img, 100, 200)
        print(file)
        print(img)
        print(edges)

        self.ui.initial.setPixmap(QPixmap.fromImage(to_QImage(img)))
        self.ui.result.setPixmap(QPixmap.fromImage(to_QImage(edges)))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    print(app.style().metaObject().className())

    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
