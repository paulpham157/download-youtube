# -*- coding: utf-8 -*-
import shutil
import yt_dlp
from pathlib import Path


class Utils:
    def check_ffmpeg():
        ffmpeg_path = Path(__file__).parent.parent / "vendors" / "ffmpeg"
        return ffmpeg_path.exists(), ffmpeg_path

    def get_channel_playlists(channel_url):
        ydl_opts = {
            "extract_flat": True,
            "skip_download": True,
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(channel_url, download=False)
            playlists = []
            if info is not None:
                for entry in info["entries"]:
                    if entry["_type"] == "url":
                        playlists.append(
                            {
                                "title": entry["title"],
                                "url": entry["url"],
                            }
                        )
        return playlists

    def get_download_dir():
        home_dir = Path.home()
        download_dir = home_dir / "Downloads" / "DiuTupDownloaderByPaulPham157"
        download_dir.mkdir(parents=True, exist_ok=True)
        return str(download_dir)

    def get_single_dir():
        home_dir = Path.home()
        single_dir = home_dir / "Downloads" / "DiuTupDownloaderByPaulPham157" / "Single"
        single_dir.mkdir(parents=True, exist_ok=True)
        return str(single_dir)
