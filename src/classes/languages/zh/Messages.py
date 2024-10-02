# -*- coding: utf-8 -*-
from ...Messages import Messages

zh_messages = Messages()
# ------------------------------------------------------------------------------------------------------#
# Start Class SplashScreen
zh_messages.splash_screen_title = "正在启动"
zh_messages.loading_app = "正在打开应用程序..."
zh_messages.switch_language = "切换语言"
zh_messages.open_app = "打开应用程序"
zh_messages.ready_to_start = "准备开始！"
# End Class SplashScreen
# ------------------------------------------------------------------------------------------------------#
# ------------------------------------------------------------------------------------------------------#
# Start Class DiuTupDownloaderApp
zh_messages.app_name = "Diu Túp downloader by Paul Pham 157"
zh_messages.download_location_label = (
    lambda d: f"""MP3, MP4 文件将保存在：{d}
它们将被分类到与播放列表名称相对应的子文件夹中，或者如果是单个视频，则保存在Single文件夹中"""
)
zh_messages.url_input_placeholder = "URL地址"
zh_messages.radio_audio_only = "仅下载音频"
zh_messages.radio_video = "下载视频"
zh_messages.clear_button = "清除"
zh_messages.logs_label = "日志："
zh_messages.copy_button = "复制"
zh_messages.start_button = "开始"
zh_messages.pause_button = "暂停"
zh_messages.continue_button = "继续"
zh_messages.exit_button = "退出"
zh_messages.check_url_input_ok = "好的，请点击下面的开始按钮"
zh_messages.found_ffmpeg = lambda p: f"在以下位置找到ffmpeg：{p}"
zh_messages.not_found_ffmpeg = lambda p: f"在以下位置未找到ffmpeg：{p}"
zh_messages.ffmpeg_warning_title = "缺少依赖项"
zh_messages.ffmpeg_warning_message = (
    "未找到ffmpeg。请将ffmpeg文件放在应用程序的同一文件夹中。"
)
zh_messages.invalid_url_message = "请输入有效的YouTube URL"
zh_messages.scanning_videos = "正在扫描视频信息..."
zh_messages.pause_download_message = "等待您点击继续..."
zh_messages.detached_private_videos = lambda m: f"有{m}个私密视频无法下载"
zh_messages.finished_message = (
    lambda t, o, p: f"已完成下载{t} / {o}\n{p}\n请粘贴其他URL继续下载，或者如果完成了就退出"
)
zh_messages.ffmpeg_error_title = "ffmpeg错误"
zh_messages.ffmpeg_error_message = (
    "错误：ffmpeg未安装或不在PATH中。请安装ffmpeg并确保它在系统PATH中。"
)
zh_messages.error = "错误："
zh_messages.copy_logs_title = "通知"
zh_messages.copy_logs_message = "日志已复制到剪贴板！"
# End Class DiuTupDownloaderApp
# ------------------------------------------------------------------------------------------------------#
# ------------------------------------------------------------------------------------------------------#
# Start Class DownloaderThread
zh_messages.instruction = """请在上面的输入框中粘贴URL地址！
可以粘贴的URL类型：

- 单个视频的URL
例如：https://www.youtube.com/watch?v=_yC7-iR6t3w&list=PLT1rvk7Trkw4nbIcS1czIII8UoioxkI8V
- 视频播放列表的URL
例如：https://www.youtube.com/playlist?list=PLT1rvk7Trkw4nbIcS1czIII8UoioxkI8V
- 频道所有播放列表的汇总URL
例如：https://www.youtube.com/@CoComelon/playlists"""
zh_messages.playlist_in_channel = lambda m: f"在频道中找到{m}个播放列表"
zh_messages.unknown_playlist_name = "未知播放列表名称"
zh_messages.filtering_private_video = (
    lambda m, n: f"在播放列表{n}中找到{m}个视频\n正在过滤私密视频"
)
zh_messages.count_private_video = lambda m: f"有1个私密视频，剩余{m}个视频，继续扫描"
zh_messages.single_video = "单个视频"
zh_messages.total_percent_downloading = (
    lambda m, n, p, f: f"[{m}/{n}]个视频正在下载：{p}\n{f}"
)
zh_messages.percent_downloading = lambda p, f: f"正在下载视频：{p}\n{f}"
zh_messages.converting_to_audio = (
    lambda c, t, f: f"[{c}/{t}]个视频正在转换为音频：\n{f}"
)
zh_messages.signle_converting_to_audio = lambda f: f"正在将视频转换为音频：\n{f}"
# End Class DownloaderThread
# ------------------------------------------------------------------------------------------------------#
