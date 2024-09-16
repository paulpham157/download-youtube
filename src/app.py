# -*- coding: utf-8 -*-

import sys
from PyQt6.QtWidgets import (
    QApplication,
)
from classes.DiuTipDownloaderApp import DiuTipDownloaderApp


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = DiuTipDownloaderApp()
    ex.show()
    sys.exit(app.exec())
