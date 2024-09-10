import sys
import os
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLineEdit,
    QPushButton,
    QLabel,
    QProgressBar,
)
from PyQt6.QtCore import Qt, QThread, pyqtSignal
import yt_dlp


class DownloaderThread(QThread):
    progress = pyqtSignal(str)
    finished = pyqtSignal()
    error = pyqtSignal(str)

    def __init__(self, url):
        super().__init__()
        self.url = url
        self.is_cancelled = False

    def run(self):
        ydl_opts = {
            "format": "bestaudio/best",
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "192",
                }
            ],
            "outtmpl": "%(title)s.%(ext)s",
            "progress_hooks": [self.progress_hook],
        }

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([self.url])
            if not self.is_cancelled:
                self.finished.emit()
        except Exception as e:
            self.error.emit(str(e))

    def progress_hook(self, d):
        if d["status"] == "downloading":
            percent = d["_percent_str"]
            filename = d["filename"]
            self.progress.emit(f"Downloading: {filename} - {percent}")
        elif d["status"] == "finished":
            filename = d["filename"]
            self.progress.emit(f"Downloaded: {filename}")

    def cancel(self):
        self.is_cancelled = True
        self.terminate()


class YouTubeDownloaderApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.downloader = None

    def initUI(self):
        self.setWindowTitle("YouTube Playlist Downloader")
        self.setGeometry(300, 300, 500, 150)

        layout = QVBoxLayout()

        url_layout = QHBoxLayout()
        self.url_input = QLineEdit()
        self.url_input.setPlaceholderText("Enter YouTube playlist URL")
        url_layout.addWidget(self.url_input)

        self.start_button = QPushButton("Start")
        self.start_button.clicked.connect(self.start_download)
        url_layout.addWidget(self.start_button)

        layout.addLayout(url_layout)

        self.status_label = QLabel("Ready")
        layout.addWidget(self.status_label)

        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 0)
        self.progress_bar.hide()
        layout.addWidget(self.progress_bar)

        button_layout = QHBoxLayout()
        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.clicked.connect(self.cancel_download)
        self.cancel_button.setEnabled(False)
        button_layout.addWidget(self.cancel_button)

        self.exit_button = QPushButton("Exit")
        self.exit_button.clicked.connect(self.close)
        button_layout.addWidget(self.exit_button)

        layout.addLayout(button_layout)

        self.setLayout(layout)

    def start_download(self):
        url = self.url_input.text().strip()
        if not url:
            self.status_label.setText("Please enter a valid YouTube playlist URL")
            return

        self.downloader = DownloaderThread(url)
        self.downloader.progress.connect(self.update_progress)
        self.downloader.finished.connect(self.download_finished)
        self.downloader.error.connect(self.download_error)

        self.downloader.start()
        self.start_button.setEnabled(False)
        self.cancel_button.setEnabled(True)
        self.progress_bar.show()
        self.status_label.setText("Downloading...")

    def cancel_download(self):
        if self.downloader and self.downloader.isRunning():
            self.downloader.cancel()
            self.status_label.setText("Download cancelled")
            self.start_button.setEnabled(True)
            self.cancel_button.setEnabled(False)
            self.progress_bar.hide()

    def update_progress(self, message):
        self.status_label.setText(message)

    def download_finished(self):
        self.status_label.setText("Download completed")
        self.start_button.setEnabled(True)
        self.cancel_button.setEnabled(False)
        self.progress_bar.hide()

    def download_error(self, error_message):
        self.status_label.setText(f"Error: {error_message}")
        self.start_button.setEnabled(True)
        self.cancel_button.setEnabled(False)
        self.progress_bar.hide()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = YouTubeDownloaderApp()
    ex.show()
    sys.exit(app.exec())
