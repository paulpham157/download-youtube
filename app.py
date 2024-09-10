import sys
import os
from pathlib import Path
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
from PyQt6.QtGui import QScreen, QFont, QColor, QPalette  # Thêm import này ở đây


def get_download_dir():
    home_dir = Path.home()
    download_dir = home_dir / "Downloads" / "YouTubeDownloader"
    download_dir.mkdir(parents=True, exist_ok=True)
    return str(download_dir)


class DownloaderThread(QThread):
    progress = pyqtSignal(str)
    finished = pyqtSignal()
    error = pyqtSignal(str)

    def __init__(self, url):
        super().__init__()
        self.url = url
        self.is_cancelled = False
        self.download_dir = get_download_dir()

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
            "outtmpl": os.path.join(self.download_dir, "%(title)s.%(ext)s"),
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
        self.download_dir = get_download_dir()
        self.initUI()
        self.downloader = None
        self.is_paused = False
        self.center()

    def initUI(self):
        self.setWindowTitle("YouTube Playlist Downloader")
        self.setFixedSize(800, 200)  # Tăng độ rộng từ 500 lên 800

        layout = QVBoxLayout()

        url_layout = QHBoxLayout()
        self.url_input = QLineEdit()
        self.url_input.setPlaceholderText("Enter YouTube playlist URL")
        url_layout.addWidget(self.url_input)

        layout.addLayout(url_layout)

        self.status_label = QLabel("Status: Ready")
        layout.addWidget(self.status_label)

        self.download_location_label = QLabel(
            f"Your mp3 will be saved in: {self.download_dir}"
        )
        layout.addWidget(self.download_location_label)

        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 0)
        self.progress_bar.hide()
        layout.addWidget(self.progress_bar)

        button_layout = QHBoxLayout()
        self.start_button = QPushButton("START")
        self.start_button.clicked.connect(self.start_download)

        # Tùy chỉnh nút Start
        start_font = QFont()
        start_font.setPointSize(self.font().pointSize() + 2)  # Tăng cỡ chữ thêm 2px
        start_font.setBold(True)  # In đậm
        self.start_button.setFont(start_font)

        # Đặt màu nền và màu chữ
        start_palette = self.start_button.palette()
        start_palette.setColor(
            QPalette.ColorRole.Button, QColor(0, 255, 0)
        )  # Màu xanh lá cây
        start_palette.setColor(
            QPalette.ColorRole.ButtonText, Qt.GlobalColor.white
        )  # Chữ màu trắng
        self.start_button.setPalette(start_palette)
        self.start_button.setAutoFillBackground(True)
        self.start_button.update()

        button_layout.addWidget(self.start_button)

        self.pause_button = QPushButton("Pause")
        self.pause_button.clicked.connect(self.pause_download)
        self.pause_button.hide()  # Ẩn nút Pause ban đầu
        button_layout.addWidget(self.pause_button)

        self.continue_button = QPushButton("Continue")
        self.continue_button.clicked.connect(self.continue_download)
        self.continue_button.hide()  # Ẩn nút Continue ban đầu

        # Tạo font lớn hơn cho nút Continue
        continue_font = QFont()
        continue_font.setPointSize(14)  # Tăng kích thước font
        continue_font.setBold(True)  # Đặt font in đậm
        self.continue_button.setFont(continue_font)

        # Tăng kích thước nút Continue
        self.continue_button.setMinimumSize(150, 50)  # Đặt kích thước tối thiểu

        # Tạo màu nền nổi bật cho nút Continue
        palette = self.continue_button.palette()
        palette.setColor(
            QPalette.ColorRole.Button, QColor(0, 128, 255)
        )  # Màu xanh dương
        palette.setColor(
            QPalette.ColorRole.ButtonText, Qt.GlobalColor.white
        )  # Chữ màu trắng
        self.continue_button.setPalette(palette)
        self.continue_button.setAutoFillBackground(True)
        self.continue_button.update()

        button_layout.addWidget(self.continue_button)

        self.exit_button = QPushButton("Exit")
        self.exit_button.clicked.connect(self.close)
        button_layout.addWidget(self.exit_button)

        layout.addLayout(button_layout)

        self.setLayout(layout)

    def center(self):
        qr = self.frameGeometry()
        screen = QApplication.primaryScreen()
        screen_geometry = screen.geometry()
        cp = screen_geometry.center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def start_download(self):
        url = self.url_input.text().strip()
        if not url:
            self.set_status("Please enter a valid YouTube playlist URL")
            return

        self.downloader = DownloaderThread(url)
        self.downloader.progress.connect(self.update_progress)
        self.downloader.finished.connect(self.download_finished)
        self.downloader.error.connect(self.download_error)

        self.downloader.start()
        self.start_button.hide()  # Ẩn nút Start
        self.pause_button.show()  # Hiển thị nút Pause
        self.progress_bar.show()
        self.set_status("Downloading...")
        self.is_paused = False

    def pause_download(self):
        if self.downloader and self.downloader.isRunning():
            self.downloader.cancel()
            self.set_status("Waiting for you...")
            self.start_button.setEnabled(False)
            self.pause_button.hide()  # Ẩn nút Pause
            self.continue_button.show()  # Hiển thị nút Continue
            self.progress_bar.hide()
            self.is_paused = True

    def continue_download(self):
        if self.is_paused:
            self.start_download()
            self.continue_button.hide()  # Ẩn nút Continue
            self.pause_button.show()  # Hiển thị lại nút Pause

    def update_progress(self, message):
        self.set_status(message)

    def download_finished(self):
        self.set_status("Download completed")
        self.start_button.show()  # Hiển thị lại nút Start
        self.pause_button.hide()  # Ẩn nút Pause
        self.progress_bar.hide()
        self.is_paused = False

    def download_error(self, error_message):
        self.set_status(f"Error: {error_message}")
        self.start_button.show()  # Hiển thị lại nút Start
        self.pause_button.hide()  # Ẩn nút Pause
        self.progress_bar.hide()
        self.is_paused = False

    def set_status(self, message):
        self.status_label.setText(f"Status: {message}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = YouTubeDownloaderApp()
    ex.show()
    sys.exit(app.exec())
