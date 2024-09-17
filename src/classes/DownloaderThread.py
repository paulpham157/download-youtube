# -*- coding: utf-8 -*-
import os
from PyQt6.QtCore import QThread, pyqtSignal
import yt_dlp
import shutil
from .Utils import Utils
from .languages import get_messages


class DownloaderThread(QThread):
    progress = pyqtSignal(str)
    playlist_progress = pyqtSignal(str)
    finished = pyqtSignal()
    error = pyqtSignal(str)

    def __init__(self, url, ffmpeg_path, messages, app):
        super().__init__()
        self.messages = messages
        self.app = app
        self.app.splash_screen.language_changed.connect(self.update_language)
        self.url = url
        self.is_cancelled = False
        self.download_dir = str(Utils.get_download_dir())
        self.original_total_videos = 0
        self.single_list = str(Utils.get_single_dir())
        self.ffmpeg_path = str(ffmpeg_path)
        self.total_videos = 0
        self.current_video = 0
        self.playlists = []
        self.current_playlist = 0
        self.current_playlist_name = ""

    def run(self):
        try:
            if "/playlists" in self.url:
                self.playlists = Utils.get_channel_playlists(self.url)
                self.progress.emit(
                    self.messages.playlist_in_channel(len(self.playlists))
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
            "outtmpl": os.path.join(str(self.download_dir), "%(title)s.%(ext)s"),
            "progress_hooks": [self.progress_hook],
            "ffmpeg_location": self.ffmpeg_path,
            "extract_flat": True,
            "no_color": True,
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(playlist_url, download=False)
            if info is not None:
                if "entries" in info:
                    self.playlist_title = info.get(
                        "title", self.messages.unknown_playlist_name
                    )
                    self.current_playlist_name = self.playlist_title
                    self.original_total_videos = len(info["entries"])
                    self.total_videos = self.original_total_videos
                    self.progress.emit(
                        self.messages.filtering_private_video(
                            self.total_videos, self.playlist_title
                        )
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
                                self.messages.count_private_video(self.total_videos)
                            )
                            continue
                        else:
                            entry_url = entry.get("url")
                            if entry_url:
                                ydl.download([str(entry_url)])
                                self.move_file_to_playlist(playlist_dir)
                else:
                    self.total_videos = 1
                    self.original_total_videos = 1
                    self.progress.emit(self.messages.single_video)
                    ydl.download([str(playlist_url)])
                    self.move_file_to_playlist(self.single_list)

    def move_file_to_playlist(self, destination_dir):
        for file in os.listdir(self.download_dir):
            if file.endswith(".mp3"):
                source_path = os.path.join(str(self.download_dir), file)
                destination_path = os.path.join(str(destination_dir), file)
                shutil.move(source_path, destination_path)

    def progress_hook(self, d):
        if d["status"] == "downloading":
            percent = d["_percent_str"]
            filename = os.path.basename(d["filename"])
            if self.total_videos > 1:
                self.progress.emit(
                    self.messages.total_percent_downloading(
                        self.current_video + 1,
                        self.total_videos,
                        percent,
                        filename,
                    )
                )
            else:
                self.progress.emit(self.messages.percent_downloading(percent, filename))
        elif d["status"] == "finished":
            self.current_video += 1
            filename = os.path.basename(d["filename"])
            if self.total_videos > 1:
                self.progress.emit(
                    self.messages.converting_to_audio(
                        self.current_video, self.total_videos, filename
                    )
                )
            else:
                self.progress.emit(self.messages.signle_converting_to_audio(filename))

    def cancel(self):
        self.is_cancelled = True
        self.terminate()

    def update_language(self, lang):
        self.messages = get_messages(lang)
