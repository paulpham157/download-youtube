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
    QVBoxLayout,
    QLabel,
    QPushButton,
    QTextEdit,
)
from PyQt6.QtCore import Qt, QThread, pyqtSignal
from PyQt6.QtGui import QFont, QColor, QPalette, QClipboard
import yt_dlp
import shutil


def check_ffmpeg():
    return shutil.which("ffmpeg") is not None


def get_download_dir():
    home_dir = Path.home()
    download_dir = home_dir / "Downloads" / "YoutubeDownloaderByPaulPham157"
    download_dir.mkdir(parents=True, exist_ok=True)
    return str(download_dir)


def get_single_dir():
    home_dir = Path.home()
    single_dir = home_dir / "Downloads" / "YoutubeDownloaderByPaulPham157" / "Single"
    single_dir.mkdir(parents=True, exist_ok=True)
    return str(single_dir)


def get_channel_playlists(channel_url):
    ydl_opts = {
        "extract_flat": True,
        "skip_download": True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(channel_url, download=False)
        playlists = []
        for entry in info["entries"]:
            if entry["_type"] == "url":
                playlists.append(
                    {
                        "title": entry["title"],
                        "url": entry["url"],
                    }
                )
    return playlists


class DownloaderThread(QThread):
    progress = pyqtSignal(str)
    playlist_progress = pyqtSignal(str)
    finished = pyqtSignal()
    error = pyqtSignal(str)

    def __init__(self, url, ffmpeg_path):
        super().__init__()
        self.url = url
        self.is_cancelled = False
        self.download_dir = get_download_dir()
        self.original_total_videos = 0
        self.single_list = get_single_dir()
        self.playlist_title = None
        self.ffmpeg_path = ffmpeg_path
        self.total_videos = 0
        self.current_video = 0
        self.playlists = []
        self.current_playlist = 0
        self.current_playlist_name = ""

    def run(self):
        try:
            if "/playlists" in self.url:
                self.playlists = get_channel_playlists(self.url)
                self.progress.emit(
                    f"Tìm thấy {len(self.playlists)} playlist trong kênh"
                )
                for playlist in self.playlists:
                    if self.is_cancelled:
                        break
                    self.download_playlist(playlist["url"])
                    self.current_playlist += 1
            else:
                self.download_playlist(self.url)

            if not self.is_cancelled:
                self.finished.emit()
        except Exception as e:
            self.error.emit(str(e))

    def download_playlist(self, playlist_url):
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
            "extract_flat": True,
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(playlist_url, download=False)
            if "entries" in info:
                self.playlist_title = info.get("title", "Unknown Playlist Name")
                self.current_playlist_name = self.playlist_title
                self.playlist_progress.emit(
                    f"Đang tải playlist: {self.current_playlist_name}"
                )
                self.original_total_videos = len(info["entries"])
                self.total_videos = self.original_total_videos
                self.progress.emit(
                    f"Tìm thấy {self.total_videos} video trong playlist {self.playlist_title}\nĐang lọc các video private"
                )
                playlist_dir = os.path.join(self.download_dir, self.playlist_title)
                os.makedirs(playlist_dir, exist_ok=True)
                for entry in info["entries"]:
                    if self.is_cancelled:
                        break
                    title = entry.get("title")
                    views = entry.get("view_count")
                    is_private = title == "[Private video]" or views is None
                    if is_private:
                        self.total_videos -= 1
                        self.progress.emit(
                            f"Có 1 video private, còn lại {self.total_videos} video, tiếp tục quét"
                        )
                        continue
                    else:
                        entry_url = entry.get("url")
                        if entry_url:
                            pass
                            # ydl.download([entry_url])
                            # self.move_file_to_playlist(playlist_dir)
            else:
                self.total_videos = 1
                self.original_total_videos = 1
                self.progress.emit("Một video đơn")
                pass
                # ydl.download([playlist_url])
                # self.move_file_to_playlist(self.single_list)

    def move_file_to_playlist(self, destination_dir):
        for file in os.listdir(self.download_dir):
            if file.endswith(".mp3"):
                source_path = os.path.join(self.download_dir, file)
                destination_path = os.path.join(destination_dir, file)
                shutil.move(source_path, destination_path)

    def progress_hook(self, d):
        if d["status"] == "downloading":
            percent = d["_percent_str"]
            filename = os.path.basename(d["filename"])

            if self.total_videos > 1:
                self.progress.emit(
                    f"[{self.current_video + 1}/{self.total_videos}] Đang tải video: {percent}\n{filename}"
                )
            else:
                self.progress.emit(f"Đang tải video: {percent}\n{filename}")

        elif d["status"] == "finished":
            self.current_video += 1
            filename = os.path.basename(d["filename"])
            if self.total_videos > 1:
                self.progress.emit(
                    f"[{self.current_video}/{self.total_videos}] Đang chuyển đổi video sang audio:\n{filename}"
                )
            else:
                self.progress.emit(f"Đang chuyển đổi video sang audio:\n{filename}")

    def cancel(self):
        self.is_cancelled = True
        self.terminate()


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
        self.setFixedSize(900, 450)

        layout = QVBoxLayout()

        self.download_location_label = QLabel(
            f"Các file mp3 sẽ lưu tại: {self.download_dir}"
        )
        self.download_location_label.setWordWrap(True)
        self.download_location_label.setFixedHeight(40)
        layout.addWidget(self.download_location_label)

        url_layout = QHBoxLayout()
        self.url_input = QLineEdit()
        self.url_input.setPlaceholderText("Địa chỉ URL")
        url_layout.addWidget(self.url_input)

        self.clear_button = QPushButton("Clear")
        self.clear_button.clicked.connect(self.clear_url)
        url_layout.addWidget(self.clear_button)

        layout.addLayout(url_layout)

        self.status_label = QLabel("Ô kê, anh nhấn nút start là được...")
        self.status_label.setWordWrap(True)
        layout.addWidget(self.status_label)

        self.playlist_progress_label = QLabel("")
        self.playlist_progress_label.setWordWrap(True)
        layout.addWidget(self.playlist_progress_label)

        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 0)
        self.progress_bar.hide()
        layout.addWidget(self.progress_bar)

        logs_layout = QHBoxLayout()
        self.logs_label = QLabel("Logs:")
        logs_layout.addWidget(self.logs_label)

        self.copy_button = QPushButton("Copy")
        self.copy_button.clicked.connect(self.copy_logs)
        self.copy_button.setFixedWidth(80)
        logs_layout.addWidget(self.copy_button)
        logs_layout.addStretch()

        layout.addLayout(logs_layout)

        self.logs_area = QTextEdit()
        self.logs_area.setReadOnly(True)
        self.logs_area.setFixedHeight(100)
        layout.addWidget(self.logs_area)

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
            base_path = sys._MEIPASS
        else:
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
        if (not url) or ("youtube.com" not in url):
            self.set_status("Vui lòng nhập URL YouTube hợp lệ")
            return

        self.url_input.setEnabled(False)
        self.clear_button.setEnabled(False)
        self.downloader = DownloaderThread(url, self.ffmpeg_path)
        self.downloader.progress.connect(self.update_progress)
        self.downloader.playlist_progress.connect(self.update_playlist_progress)
        self.downloader.finished.connect(self.download_finished)
        self.downloader.error.connect(self.download_error)

        self.downloader.start()
        self.start_button.hide()
        self.pause_button.show()
        self.progress_bar.show()
        self.playlist_progress_label.show()
        self.set_status("Đang quét thông tin các video...")
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
        self.logs_area.append(message)
        if self.downloader.playlists:
            progress = f"Đang tải playlist {self.downloader.current_playlist + 1}/{len(self.downloader.playlists)}"
            self.playlist_progress_label.setText(progress)

    def update_playlist_progress(self, message):
        current_status = self.status_label.text()
        new_status = f"{message}\n{current_status}"
        self.status_label.setText(new_status)
        self.logs_area.append(message)

    def download_finished(self):
        total_videos = self.downloader.total_videos
        original_total_videos = self.downloader.original_total_videos
        private_videos = original_total_videos - total_videos
        if private_videos > 0:
            self.set_status(
                f"Tải xong {total_videos} public video trên tổng số {original_total_videos} video rồi anh ạ\nCó {private_videos} video private không tải được\nAnh dán URL khác vào để tải tiếp hoặc là thoát nếu đã xong"
            )
        else:
            self.set_status(
                f"Tải xong {total_videos} public video trên tổng số {original_total_videos} video rồi anh ạ\nAnh dán URL khác vào để tải tiếp hoặc là thoát nếu đã xong"
            )
        self.start_button.show()
        self.pause_button.hide()
        self.progress_bar.hide()
        self.is_paused = False
        self.url_input.setEnabled(True)
        self.clear_button.setEnabled(True)

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
        self.start_button.show()
        self.pause_button.hide()
        self.progress_bar.hide()
        self.is_paused = False
        self.url_input.setEnabled(True)

    def set_status(self, message):
        current_playlist_progress = (
            self.status_label.text().split("\n")[0]
            if "\n" in self.status_label.text()
            else ""
        )
        new_status = (
            f"{current_playlist_progress}\nTrạng thái:\n{message}"
            if current_playlist_progress
            else f"Trạng thái:\n{message}"
        )
        self.status_label.setText(new_status)
        self.logs_area.append(message)

    def clear_url(self):
        self.url_input.clear()

    def copy_logs(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(self.logs_area.toPlainText())
        QMessageBox.information(self, "Thông báo", "Đã sao chép logs vào clipboard!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = YouTubeDownloaderApp()
    ex.show()
    sys.exit(app.exec())

    sys.exit(app.exec())
