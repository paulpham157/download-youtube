# -*- coding: utf-8 -*-
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
    QMessageBox,
    QDialog,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QTextBrowser,
)
from PyQt6.QtCore import Qt, QThread, pyqtSignal
import yt_dlp
from PyQt6.QtGui import QScreen, QFont, QColor, QPalette
import shutil


def check_ffmpeg():
    return shutil.which("ffmpeg") is not None


def get_download_dir():
    home_dir = Path.home()
    download_dir = home_dir / "Downloads" / "YoutubeDownloaderByPaulPham157"
    download_dir.mkdir(parents=True, exist_ok=True)
    return str(download_dir)


class DownloaderThread(QThread):
    progress = pyqtSignal(str)
    finished = pyqtSignal()
    error = pyqtSignal(str)

    def __init__(self, url, ffmpeg_path):
        super().__init__()
        self.url = url
        self.is_cancelled = False
        self.download_dir = get_download_dir()
        self.playlist_title = None
        self.ffmpeg_path = ffmpeg_path

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
            "ffmpeg_location": self.ffmpeg_path,
        }

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(self.url, download=False)
                if "entries" in info:
                    self.playlist_title = info.get("title", "Unknown Playlist")
                    playlist_dir = os.path.join(self.download_dir, self.playlist_title)
                    os.makedirs(playlist_dir, exist_ok=True)
                    self.progress.emit(f"Tạo thư mục: {self.playlist_title}")
                else:
                    self.playlist_title = None

                ydl.download([self.url])

            if not self.is_cancelled:
                self.finished.emit()
        except Exception as e:
            self.error.emit(str(e))

    def progress_hook(self, d):
        if d["status"] == "downloading":
            percent = d["_percent_str"]
            filename = os.path.basename(d["filename"])

            try:
                self.progress.emit(f"Đang kéo webpage {percent}: {filename}")
            except UnicodeEncodeError:
                self.progress.emit(
                    f"Đang kéo webpage {percent}: Có vấn đề với UTF-8 với tên file"
                )
        elif d["status"] == "finished":
            filename = os.path.basename(d["filename"])
            try:
                self.progress.emit(f"Chuẩn bị hoàn tất: {filename}")
            except UnicodeEncodeError:
                self.progress.emit(
                    "Chuẩn bị hoàn tất: Có vấn đề với UTF-8 với tên file"
                )

    def cancel(self):
        self.is_cancelled = True
        self.terminate()


class InstallationGuideDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Hướng dẫn cài đặt ffmpeg")
        self.setMinimumSize(400, 300)

        layout = QVBoxLayout()

        guide_text = """
        Để cài đặt ffmpeg, hãy làm theo hướng dẫn dưới đây tùy theo hệ điều hành của bạn:

        Windows:
        - Sử dụng Chocolatey: choco install ffmpeg
        - Hoặc tải xuống từ trang chủ ffmpeg và thêm vào PATH.

        macOS:
        - Sử dụng Homebrew: brew install ffmpeg

        Linux (Ubuntu/Debian):
        sudo apt update
        sudo apt install ffmpeg

        Linux (Fedora):
        sudo dnf install ffmpeg

        Sau khi cài đặt, hãy khởi động lại ứng dụng.
        """

        guide_browser = QTextBrowser()
        guide_browser.setPlainText(guide_text)
        layout.addWidget(guide_browser)

        close_button = QPushButton("Đóng")
        close_button.clicked.connect(self.close)
        layout.addWidget(close_button)

        self.setLayout(layout)


class YouTubeDownloaderApp(QWidget):
    def __init__(self):
        super().__init__()
        self.download_dir = get_download_dir()
        self.ffmpeg_path = self.find_ffmpeg()
        self.initUI()
        self.downloader = None
        self.is_paused = False
        self.center()
        self.check_dependencies()

    def initUI(self):
        self.setWindowTitle("Diu Túp downloader by Paul Pham 157")
        self.setFixedSize(900, 300)

        layout = QVBoxLayout()

        url_layout = QHBoxLayout()
        self.url_input = QLineEdit()
        self.url_input.setPlaceholderText("Địa chỉ URL")
        url_layout.addWidget(self.url_input)

        layout.addLayout(url_layout)

        self.status_label = QLabel("Ô kê, anh nhấn nút start là được...")
        layout.addWidget(self.status_label)

        self.download_location_label = QLabel(
            f"Các file mp3 sẽ lưu tại: {self.download_dir}"
        )
        layout.addWidget(self.download_location_label)

        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 0)
        self.progress_bar.hide()
        layout.addWidget(self.progress_bar)

        button_layout = QHBoxLayout()
        self.start_button = QPushButton("START")
        self.start_button.clicked.connect(self.start_download)

        start_font = QFont()
        start_font.setPointSize(self.font().pointSize() + 2)
        start_font.setBold(True)
        self.start_button.setFont(start_font)

        start_palette = self.start_button.palette()
        start_palette.setColor(QPalette.ColorRole.Button, QColor(0, 255, 0))
        start_palette.setColor(QPalette.ColorRole.ButtonText, Qt.GlobalColor.white)
        self.start_button.setPalette(start_palette)
        self.start_button.setAutoFillBackground(True)
        self.start_button.update()

        button_layout.addWidget(self.start_button)

        self.pause_button = QPushButton("Pause")
        self.pause_button.clicked.connect(self.pause_download)
        self.pause_button.hide()
        button_layout.addWidget(self.pause_button)

        self.continue_button = QPushButton("Continue")
        self.continue_button.clicked.connect(self.continue_download)
        self.continue_button.hide()

        continue_font = QFont()
        continue_font.setPointSize(14)
        continue_font.setBold(True)
        self.continue_button.setFont(continue_font)

        self.continue_button.setMinimumSize(150, 50)

        palette = self.continue_button.palette()
        palette.setColor(QPalette.ColorRole.Button, QColor(0, 128, 255))
        palette.setColor(QPalette.ColorRole.ButtonText, Qt.GlobalColor.white)
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

    def find_ffmpeg(self):
        if getattr(sys, "frozen", False):
            # Nếu đang chạy từ file thực thi đã được đóng gói
            base_path = sys._MEIPASS
        else:
            # Nếu đang chạy từ script
            base_path = os.path.dirname(os.path.abspath(__file__))

        ffmpeg_path = os.path.join(base_path, "ffmpeg")
        if sys.platform == "win32":
            ffmpeg_path += ".exe"

        if os.path.exists(ffmpeg_path):
            return ffmpeg_path
        return None

    def check_dependencies(self):
        if not self.ffmpeg_path:
            QMessageBox.warning(
                self,
                "Thiếu phụ thuộc",
                "Không tìm thấy ffmpeg. Vui lòng đặt file ffmpeg trong cùng thư mục với ứng dụng.",
                QMessageBox.StandardButton.Ok,
            )

    def start_download(self):
        if not self.ffmpeg_path:
            self.set_status(
                "Lỗi: Không tìm thấy ffmpeg. Vui lòng đặt file ffmpeg trong cùng thư mục với ứng dụng."
            )
            return

        url = self.url_input.text().strip()
        if not url:
            self.set_status("Vui lòng nhập URL playlist YouTube hợp lệ")
            return

        self.downloader = DownloaderThread(url, self.ffmpeg_path)
        self.downloader.progress.connect(self.update_progress)
        self.downloader.finished.connect(self.download_finished)
        self.downloader.error.connect(self.download_error)

        self.downloader.start()
        self.start_button.hide()
        self.pause_button.show()
        self.progress_bar.show()
        self.set_status("Đang chuẩn bị...")
        self.is_paused = False

    def pause_download(self):
        if self.downloader and self.downloader.isRunning():
            self.downloader.cancel()
            self.set_status("Đang chờ anh nhấn tiếp tục đấy...")
            self.start_button.setEnabled(False)
            self.pause_button.hide()
            self.continue_button.show()
            self.progress_bar.hide()
            self.is_paused = True

    def continue_download(self):
        if self.is_paused:
            self.start_download()
            self.continue_button.hide()
            self.pause_button.show()

    def update_progress(self, message):
        self.set_status(message)

    def download_finished(self):
        self.set_status(
            "Tải xong hết rồi anh ạ, anh dán URL khác vào để tải tiếp hoặc là thoát nếu đã xong"
        )
        self.start_button.show()
        self.pause_button.hide()
        self.progress_bar.hide()
        self.is_paused = False

    def download_error(self, error_message):
        if "ffprobe and ffmpeg not found" in error_message:
            self.set_status("Lỗi: ffmpeg không được cài đặt hoặc không nằm trong PATH")
            QMessageBox.warning(
                self,
                "Lỗi ffmpeg",
                "Không tìm thấy ffmpeg. Vui lòng cài đặt ffmpeg và đảm bảo nó nằm trong PATH hệ thống.",
                QMessageBox.StandardButton.Ok,
            )
        else:
            self.set_status(f"Lỗi: {error_message}")
        self.start_button.show()  # Hiển thị lại nút Start
        self.pause_button.hide()  # Ẩn nút Pause
        self.progress_bar.hide()
        self.is_paused = False

    def set_status(self, message):
        self.status_label.setText(f"Trạng thái: {message}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = YouTubeDownloaderApp()
    ex.show()
    sys.exit(app.exec())
