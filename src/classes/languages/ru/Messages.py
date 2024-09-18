# -*- coding: utf-8 -*-
from ...Messages import Messages

ru_messages = Messages()
# ------------------------------------------------------------------------------------------------------#
# Start Class SplashScreen
ru_messages.splash_screen_title = "Запуск"
ru_messages.loading_app = "Открытие приложения..."
ru_messages.switch_language = "Сменить язык"
ru_messages.open_app = "Открыть приложение"
ru_messages.ready_to_start = "Готово к запуску!"
# End Class SplashScreen
# ------------------------------------------------------------------------------------------------------#
# ------------------------------------------------------------------------------------------------------#
# Start Class DiuTupDownloaderApp
ru_messages.app_name = "Diu Túp downloader by Paul Pham 157"
ru_messages.download_location_label = (
    lambda d: f"""MP3-файлы будут сохранены в: {d}
Они разделены на подпапки, соответствующие названиям плейлистов, или Single, если URL-адрес является отдельным видео"""
)
ru_messages.url_input_placeholder = "URL-адрес"
ru_messages.clear_button = "Очистить"
ru_messages.logs_label = "Журнал:"
ru_messages.copy_button = "Копировать"
ru_messages.start_button = "НАЧАТЬ"
ru_messages.pause_button = "Пауза"
ru_messages.continue_button = "Продолжить"
ru_messages.exit_button = "Выход"
ru_messages.check_url_input_ok = "Хорошо, нажмите кнопку начать ниже"
ru_messages.found_ffmpeg = lambda p: f"FFmpeg найден в: {p}"
ru_messages.not_found_ffmpeg = lambda p: f"FFmpeg не найден в: {p}"
ru_messages.ffmpeg_warning_title = "Отсутствует зависимость"
ru_messages.ffmpeg_warning_message = "FFmpeg не найден. Пожалуйста, поместите файл ffmpeg в ту же папку, что и приложение."
ru_messages.invalid_url_message = "Пожалуйста, введите действительный URL-адрес YouTube"
ru_messages.scanning_videos = "Сканирование информации о видео..."
ru_messages.pause_download_message = "Ожидание нажатия кнопки продолжить..."
ru_messages.detached_private_videos = (
    lambda m: f"Есть {m} приватных видео, которые нельзя загрузить"
)
ru_messages.finished_message = (
    lambda t, o, p: f"Загрузка завершена {t} / {o}\n{p}\nВы можете вставить другой URL для продолжения загрузки или выйти, если закончили"
)
ru_messages.ffmpeg_error_title = "Ошибка FFmpeg"
ru_messages.ffmpeg_error_message = "Ошибка: FFmpeg не установлен или отсутствует в PATH. Пожалуйста, установите FFmpeg и убедитесь, что он находится в системном PATH."
ru_messages.error = "Ошибка: "
ru_messages.copy_logs_title = "Уведомление"
ru_messages.copy_logs_message = "Журналы скопированы в буфер обмена!"
# End Class DiuTupDownloaderApp
# ------------------------------------------------------------------------------------------------------#
# ------------------------------------------------------------------------------------------------------#
# Start Class DownloaderThread
ru_messages.instruction = """Вставьте URL-адрес в поле ввода выше!
URL может быть:

- URL отдельного видео
например: https://www.youtube.com/watch?v=_yC7-iR6t3w&list=PLT1rvk7Trkw4nbIcS1czIII8UoioxkI8V
- URL плейлиста видео
например: https://www.youtube.com/playlist?list=PLT1rvk7Trkw4nbIcS1czIII8UoioxkI8V
- URL сборника плейлистов канала
например: https://www.youtube.com/@CoComelon/playlists"""
ru_messages.playlist_in_channel = lambda m: f"Найдено {m} плейлистов на канале"
ru_messages.unknown_playlist_name = "Неизвестное название плейлиста"
ru_messages.filtering_private_video = (
    lambda m, n: f"Найдено {m} видео в плейлисте {n}\nФильтрация приватных видео"
)
ru_messages.count_private_video = (
    lambda m: f"Есть 1 приватное видео, осталось {m} видео, продолжаем сканирование"
)
ru_messages.single_video = "Одно видео"
ru_messages.total_percent_downloading = (
    lambda m, n, p, f: f"[{m}/{n}] видео загружается: {p}\n{f}"
)
ru_messages.percent_downloading = lambda p, f: f"Загрузка видео: {p}\n{f}"
ru_messages.converting_to_audio = (
    lambda c, t, f: f"[{c}/{t}] видео конвертируется в аудио:\n{f}"
)
ru_messages.signle_converting_to_audio = lambda f: f"Конвертация видео в аудио:\n{f}"
# End Class DownloaderThread
# ------------------------------------------------------------------------------------------------------#
