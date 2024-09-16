# -*- coding: utf-8 -*-
from ...Messages import Messages

vi_messages = Messages()
# ------------------------------------------------------------------------------------------------------#
# Start Class SplashScreen
vi_messages.splash_screen_title = "Đang khởi động"
vi_messages.loading_app = "Đang mở ứng dụng..."
vi_messages.switch_language = "Chuyển ngôn ngữ"
vi_messages.open_app = "Mở ứng dụng"
vi_messages.ready_to_start = "Sẵn sàng để bắt đầu!"
# End Class SplashScreen
# ------------------------------------------------------------------------------------------------------#
# ------------------------------------------------------------------------------------------------------#
# Start Class DiuTupDownloaderApp
vi_messages.app_name = "Diu Túp downloader by Paul Pham 157"
vi_messages.download_location_label = (
    lambda d: f"""Các file mp3 sẽ lưu tại: {d}
Chúng được chia vào các thư mục con tương ứng với tên của playlist hoặc Single nếu url là video đơn lẻ"""
)
vi_messages.url_input_placeholder = "Địa chỉ URL"
vi_messages.clear_button = "Xoá"
vi_messages.logs_label = "Nhật ký:"
vi_messages.copy_button = "Sao chép"
vi_messages.start_button = "BẮT ĐẦU"
vi_messages.pause_button = "Dừng"
vi_messages.continue_button = "Tiếp tục"
vi_messages.exit_button = "Thoát"
vi_messages.check_url_input_ok = "Ô kê, anh nhấn nút bắt đầu bên dưới là được"
vi_messages.found_ffmpeg = lambda p: f"Đã tìm thấy ffmpeg tại: {p}"
vi_messages.not_found_ffmpeg = lambda p: f"Không tìm thấy ffmpeg tại: {p}"
vi_messages.ffmpeg_warning_title = "Thiếu phụ thuộc"
vi_messages.ffmpeg_warning_message = (
    "Không tìm thấy ffmpeg. Vui lòng đặt file ffmpeg trong cùng thư mục với ứng dụng."
)
vi_messages.invalid_url_message = "Vui lòng nhập URL YouTube hợp lệ"
vi_messages.scanning_videos = "Đang quét thông tin các video..."
vi_messages.pause_download_message = "Đang chờ anh nhấn tiếp tục đấy..."
vi_messages.detached_private_videos = lambda m: f"Có {m} video private không tải được"
vi_messages.finished_message = (
    lambda t, o, p: f"Tải xong {t} / {o} rồi anh ạ\n{p}\nAnh dán URL khác vào để tải tiếp hoặc là thoát nếu đã xong"
)
vi_messages.ffmpeg_error_title = "Lỗi ffmpeg"
vi_messages.ffmpeg_error_message = "Lỗi: ffmpeg không được cài đặt hoặc không nằm trong PATH. Vui lòng cài đặt ffmpeg và đảm bảo nó nằm trong PATH hệ thống."
vi_messages.error = "Lỗi: "
vi_messages.copy_logs_title = "Thông báo"
vi_messages.copy_logs_message = "Đã sao chép logs vào clipboard!"
# End Class DiuTupDownloaderApp
# ------------------------------------------------------------------------------------------------------#
# ------------------------------------------------------------------------------------------------------#
# Start Class DownloaderThread
vi_messages.instruction = """Anh dán địa chỉ URL vào input phía trên nhé!
URL có thể dán là:

- URL của 1 video đơn lẻ
vd: https://www.youtube.com/watch?v=_yC7-iR6t3w&list=PLT1rvk7Trkw4nbIcS1czIII8UoioxkI8V
- URL của 1 playlist các video
vd: https://www.youtube.com/playlist?list=PLT1rvk7Trkw4nbIcS1czIII8UoioxkI8V
- URL tổng hợp các playlists của 1 kênh
vd: https://www.youtube.com/@CoComelon/playlists"""
vi_messages.playlist_in_channel = lambda m: f"Tìm thấy {m} playlist trong kênh"
vi_messages.unknown_playlist_name = "Tên Playlist không xác định"
vi_messages.filtering_private_video = (
    lambda m, n: f"Tìm thấy {m} video trong playlist {n}\nĐang lọc các video private"
)
vi_messages.count_private_video = (
    lambda m: f"Có 1 video private, còn lại {m} video, tiếp tục quét"
)
vi_messages.single_video = "Một video đơn"
vi_messages.total_percent_downloading = (
    lambda m, n, p, f: f"[{m}/{n}] videos đang tải: {p}\n{f}"
)
vi_messages.percent_downloading = lambda p, f: f"Đang tải video: {p}\n{f}"
vi_messages.converting_to_audio = (
    lambda c, t, f: f"[{c}/{t}] videos đang chuyển đổi sang audio:\n{f}"
)
vi_messages.signle_converting_to_audio = (
    lambda f: f"Đang chuyển đổi video sang audio:\n{f}"
)
# End Class DownloaderThread
# ------------------------------------------------------------------------------------------------------#
