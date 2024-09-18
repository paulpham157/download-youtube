# -*- coding: utf-8 -*-
import shutil
import yt_dlp
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup


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

    def get_shorts_links(channel):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(channel)
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, "html.parser")
        driver.execute_script(
            """
            var scroll = setInterval(function(){
                window.scrollBy(0, 1000);
            }, 1000);
        """
        )
        updated_page_source = driver.page_source
        driver.quit()
        soup = BeautifulSoup(updated_page_source, "html.parser")
        video_tags = soup.find_all(
            "a",
            {
                "class": "reel-item-endpoint",
            },
        )
        shorts_links = []
        for video_tag in video_tags:
            href = video_tag.get("href", "N/A")
            if "shorts" in href:
                video_url = "https://www.youtube.com" + href
                shorts_links.append(video_url)
        total_shorts = len(shorts_links)
        return total_shorts, shorts_links
