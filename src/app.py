# -*- coding: utf-8 -*-

import sys
from PyQt6.QtWidgets import (
    QApplication,
)
from classes.DiuTupDownloaderApp import DiuTupDownloaderApp


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = DiuTupDownloaderApp()
    ex.show()
    sys.exit(app.exec())
