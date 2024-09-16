# -*- coding: utf-8 -*-
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
    QMessageBox,
    QTextEdit,
)
from PyQt6.QtGui import QFont
from .Utils import Utils
from .DownloaderThread import DownloaderThread
from .Messages import Messages
from pathlib import Path

messages = Messages()


class DiuTipDownloaderApp(QWidget):
    def __init__(self):
        super().__init__()
        self.download_dir = Utils.get_download_dir()
        self.ffmpeg_path = self.find_ffmpeg()
        self.initUI()
        self.downloader = None
        self.is_paused = False
        self.center()
        self.check_dependencies()

    def initUI(self):
        self.setWindowTitle("Diu Túp downloader by Paul Pham 157")

        layout = QVBoxLayout()

        self.download_location_label = QLabel(
            f"""Các file mp3 sẽ lưu tại: {self.download_dir}
Chúng được chia vào các thư mục con tương ứng với tên của playlist hoặc Single nếu url là video đơn lẻ"""
        )
        self.download_location_label.setWordWrap(True)
        layout.addWidget(self.download_location_label)

        url_layout = QHBoxLayout()
        self.url_input = QLineEdit()
        self.url_input.setPlaceholderText("Địa chỉ URL")
        url_layout.addWidget(self.url_input)

        self.clear_button = QPushButton("Clear")
        self.clear_button.clicked.connect(self.clear_url)
        url_layout.addWidget(self.clear_button)

        layout.addLayout(url_layout)

        self.status_label = QLabel(messages.instruction)
        self.status_label.setWordWrap(True)
        layout.addWidget(self.status_label)
        self.url_input.textChanged.connect(self.check_url_input)

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

        button_layout.addWidget(self.continue_button)

        self.exit_button = QPushButton("Exit")
        self.exit_button.clicked.connect(self.close)
        button_layout.addWidget(self.exit_button)

        layout.addLayout(button_layout)

        self.setLayout(layout)

    def center(self):
        qr = self.frameGeometry()
        screen = QApplication.primaryScreen()
        if screen is not None:
            screen_geometry = screen.geometry()
            cp = screen_geometry.center()
            qr.moveCenter(cp)
            self.move(qr.topLeft())

    def check_url_input(self):
        url = self.url_input.text().strip()
        if url:
            self.status_label.setText("Ô kê, anh nhấn nút start là được")
        else:
            self.status_label.setText(messages.instruction)

    def find_ffmpeg(self):
        is_ffmpeg_vendors_exists, ffmpeg_vendors_path = Utils.check_ffmpeg()
        if not is_ffmpeg_vendors_exists:
            ffmpeg_vendors_path.mkdir(parents=True, exist_ok=True)
        ffmpeg_path = ffmpeg_vendors_path / "ffmpeg"
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
        txt_playlist_progress = ""
        if self.downloader is not None:
            if self.downloader.playlists:
                txt_playlist_progress = f"[{self.downloader.current_playlist + 1}/{len(self.downloader.playlists)}]"
            progress = f"Playlist: {txt_playlist_progress} {self.downloader.current_playlist_name}"
            self.playlist_progress_label.setText(progress)
            self.set_status(message)
            self.logs_area.append(message)

    def update_playlist_progress(self, message):
        current_status = self.status_label.text()
        new_status = f"{message}\n{current_status}"
        self.status_label.setText(new_status)
        self.logs_area.append(message)

    # TODO: update hiển thị mess báo thành công khi tải xong cả kênh playlists
    def download_finished(self):
        if self.downloader is not None:
            total_videos = self.downloader.total_videos
            original_total_videos = self.downloader.original_total_videos
            private_videos = original_total_videos - total_videos
            private_detached_message = ""
            if private_videos > 0:
                private_detached_message = (
                    f"Có {private_videos} video private không tải được"
                )
            finished_message = f"""Tải xong {total_videos} / {original_total_videos} rồi anh ạ
    {private_detached_message}
    Anh dán URL khác vào để tải tiếp hoặc là thoát nếu đã xong"""
            self.set_status(finished_message)
            self.start_button.show()
            self.pause_button.hide()
            self.progress_bar.hide()
            self.playlist_progress_label.hide()
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
        new_status = f"{current_playlist_progress}\n{message}"
        self.status_label.setText(new_status)
        self.logs_area.append(message)

    def clear_url(self):
        self.url_input.clear()

    def copy_logs(self):
        clipboard = QApplication.clipboard()
        if clipboard is not None:
            clipboard.setText(self.logs_area.toPlainText())
            QMessageBox.information(
                self, "Thông báo", "Đã sao chép logs vào clipboard!"
            )
