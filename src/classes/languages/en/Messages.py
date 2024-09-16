# -*- coding: utf-8 -*-
from ...Messages import Messages

en_messages = Messages()
# ------------------------------------------------------------------------------------------------------#
# Start Class DiuTupDownloaderApp
en_messages.app_name = "YouTube downloader by Paul Pham 157"
en_messages.download_location_label = (
    lambda d: f"""MP3 files will be saved at: {d}
They are organized into subfolders corresponding to playlist names or 'Single' if the URL is a single video"""
)
en_messages.placeholder_url = "URL Address"
en_messages.clear_button = "Clear"
en_messages.logs_label = "Logs:"
en_messages.copy_button = "Copy"
en_messages.start_button = "START"
en_messages.pause_button = "Pause"
en_messages.continue_button = "Continue"
en_messages.exit_button = "Exit"
en_messages.check_url_input_ok = "OK, you can press the start button now"
en_messages.found_ffmpeg = lambda p: f"Found ffmpeg at: {p}"
en_messages.not_found_ffmpeg = lambda p: f"ffmpeg not found at: {p}"
en_messages.ffmpeg_warning_title = "Missing Dependency"
en_messages.ffmpeg_warning_message = "ffmpeg not found. Please place the ffmpeg file in the same directory as the application."
en_messages.invalid_url_message = "Please enter a valid YouTube URL"
en_messages.scanning_videos = "Scanning video information..."
en_messages.pause_download_message = "Waiting for you to press continue..."
en_messages.detached_private_videos = (
    lambda m: f"There are {m} private videos that cannot be downloaded"
)
en_messages.finished_message = (
    lambda t, o, p: f"Download completed {t} / {o}\n{p}\nYou can paste another URL to continue downloading or exit if finished"
)
en_messages.ffmpeg_error_title = "ffmpeg Error"
en_messages.ffmpeg_error_message = "Error: ffmpeg is not installed or not in PATH. Please install ffmpeg and ensure it's in the system PATH."
en_messages.error = "Error: "
en_messages.copy_logs_title = "Notification"
en_messages.copy_logs_message = "Logs copied to clipboard!"
# End Class DiuTupDownloaderApp
# ------------------------------------------------------------------------------------------------------#
# ------------------------------------------------------------------------------------------------------#
# Start Class DownloaderThread
en_messages.instruction = """Please paste the URL into the input above!
The URL can be:

- URL of a single video
e.g.: https://www.youtube.com/watch?v=_yC7-iR6t3w&list=PLT1rvk7Trkw4nbIcS1czIII8UoioxkI8V
- URL of a video playlist
e.g.: https://www.youtube.com/playlist?list=PLT1rvk7Trkw4nbIcS1czIII8UoioxkI8V
- URL of a channel's playlists compilation
e.g.: https://www.youtube.com/@CoComelon/playlists"""
en_messages.playlist_in_channel = lambda m: f"Found {m} playlists in the channel"
en_messages.unknown_playlist_name = "Unknown Playlist Name"
en_messages.filtering_private_video = (
    lambda m, n: f"Found {m} videos in playlist {n}\nFiltering private videos"
)
en_messages.count_private_video = (
    lambda m: f"There is 1 private video, {m} videos remaining, continuing scan"
)
en_messages.single_video = "A single video"
en_messages.total_percent_downloading = (
    lambda m, n, p, f: f"[{m}/{n}] videos downloading: {p}\n{f}"
)
en_messages.percent_downloading = lambda p, f: f"Downloading video: {p}\n{f}"
en_messages.converting_to_audio = (
    lambda c, t, f: f"[{c}/{t}] videos converting to audio:\n{f}"
)
en_messages.signle_converting_to_audio = lambda f: f"Converting video to audio:\n{f}"
# End Class DownloaderThread
# ------------------------------------------------------------------------------------------------------#
