# -*- coding: utf-8 -*-

import sys
from PyQt6.QtWidgets import QApplication
from classes.SplashScreen import SplashScreen
from classes.DiuTupDownloaderApp import DiuTupDownloaderApp


class App(QApplication):
    def __init__(self, argv):
        super().__init__(argv)
        self.splash = SplashScreen()
        self.messages = self.splash.messages
        self.main_app = None

    def start(self):
        self.splash.show()
        self.processEvents()
        self.main_app = DiuTupDownloaderApp(
            messages=self.messages, splash_screen=self.splash
        )

        # Kiểm tra các phụ thuộc
        if self.main_app.check_dependencies():
            self.splash.show_start_button()
            self.splash.ready_signal.connect(self.show_main_app)

    def show_main_app(self):
        self.splash.close()
        self.main_app.show()


if __name__ == "__main__":
    app = App(sys.argv)
    app.start()
    sys.exit(app.exec())
