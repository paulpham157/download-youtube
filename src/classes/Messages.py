# -*- coding: utf-8 -*-
class Messages:
    def __init__(self):
        # ------------------------------------------------------------------------------------------------------#
        # Start Class SplashScreen
        self.splash_screen_title = "Đang khởi động"
        self.loading_app = "Đang mở ứng dụng..."
        self.switch_language = "Chuyển ngôn ngữ"
        self.open_app = "Mở ứng dụng"
        self.ready_to_start = "Sẵn sàng để bắt đầu!"
        # End Class SplashScreen
        # ------------------------------------------------------------------------------------------------------#
        # ------------------------------------------------------------------------------------------------------#
        # Start Class DiuTupDownloaderApp
        self.app_name = "Diu Túp downloader by Paul Pham 157"
        self.download_location_label = (
            lambda d: f"""Các file mp3 sẽ lưu tại: {d}
Chúng được chia vào các thư mục con tương ứng với tên của playlist hoặc Single nếu url là video đơn lẻ"""
        )
        self.placeholder_url = "Địa chỉ URL"
        self.clear_button = "Clear"
        self.logs_label = "Logs:"
        self.copy_button = "Copy"
        self.start_button = "START"
        self.pause_button = "Pause"
        self.continue_button = "Continue"
        self.exit_button = "Exit"
        self.check_url_input_ok = "Ô kê, anh nhấn nút start là được"
        self.found_ffmpeg = lambda p: f"Đã tìm thấy ffmpeg tại: {p}"
        self.not_found_ffmpeg = lambda p: f"Không tìm thấy ffmpeg tại: {p}"
        self.ffmpeg_warning_title = "Thiếu phụ thuộc"
        self.ffmpeg_warning_message = "Không tìm thấy ffmpeg. Vui lòng đặt file ffmpeg trong cùng thư mục với ứng dụng."
        self.invalid_url_message = "Vui lòng nhập URL YouTube hợp lệ"
        self.scanning_videos = "Đang quét thông tin các video..."
        self.pause_download_message = "Đang chờ anh nhấn tiếp tục đấy..."
        self.detached_private_videos = lambda m: f"Có {m} video private không tải được"
        self.finished_message = (
            lambda t, o, p: f"Tải xong {t} / {o} rồi anh ạ\n{p}\nAnh dán URL khác vào để tải tiếp hoặc là thoát nếu đã xong"
        )
        self.ffmpeg_error_title = "Lỗi ffmpeg"
        self.ffmpeg_error_message = "Lỗi: ffmpeg không được cài đặt hoặc không nằm trong PATH. Vui lòng cài đặt ffmpeg và đảm bảo nó nằm trong PATH hệ thống."
        self.error = "Lỗi: "
        self.copy_logs_title = "Thông báo"
        self.copy_logs_message = "Đã sao chép logs vào clipboard!"
        # End Class DiuTupDownloaderApp
        # ------------------------------------------------------------------------------------------------------#
        # ------------------------------------------------------------------------------------------------------#
        # Start Class DownloaderThread
        self.instruction = """Anh dán địa chỉ URL vào input phía trên nhé!
URL có thể dán là:

- URL của 1 video đơn lẻ
vd: https://www.youtube.com/watch?v=_yC7-iR6t3w&list=PLT1rvk7Trkw4nbIcS1czIII8UoioxkI8V
- URL của 1 playlist các video
vd: https://www.youtube.com/playlist?list=PLT1rvk7Trkw4nbIcS1czIII8UoioxkI8V
- URL tổng hợp các playlists của 1 kênh
vd: https://www.youtube.com/@CoComelon/playlists"""
        self.playlist_in_channel = lambda m: f"Tìm thấy {m} playlist trong kênh"
        self.unknown_playlist_name = "Unknown Playlist Name"
        self.filtering_private_video = (
            lambda m, n: f"Tìm thấy {m} video trong playlist {n}\nĐang lọc các video private"
        )
        self.count_private_video = (
            lambda m: f"Có 1 video private, còn lại {m} video, tiếp tục quét"
        )
        self.single_video = "Một video đơn"
        self.total_percent_downloading = (
            lambda m, n, p, f: f"[{m}/{n}] videos đang tải: {p}\n{f}"
        )
        self.percent_downloading = lambda p, f: f"Đang tải video: {p}\n{f}"
        self.converting_to_audio = (
            lambda c, t, f: f"[{c}/{t}] videos đang chuyển đổi sang audio:\n{f}"
        )
        self.signle_converting_to_audio = (
            lambda f: f"Đang chuyển đổi video sang audio:\n{f}"
        )
        # End Class DownloaderThread
        # ------------------------------------------------------------------------------------------------------#
