# -*- coding: utf-8 -*-
from ...Messages import Messages

es_messages = Messages()
# ------------------------------------------------------------------------------------------------------#
# Start Class SplashScreen
es_messages.splash_screen_title = "Iniciando"
es_messages.loading_app = "Abriendo la aplicación..."
es_messages.switch_language = "Cambiar idioma"
es_messages.open_app = "Abrir aplicación"
es_messages.ready_to_start = "¡Listo para comenzar!"
# End Class SplashScreen
# ------------------------------------------------------------------------------------------------------#
# ------------------------------------------------------------------------------------------------------#
# Start Class DiuTupDownloaderApp
es_messages.app_name = "Diu Túp downloader by Paul Pham 157"
es_messages.download_location_label = (
    lambda d: f"""Los archivos MP3, MP4 se guardarán en: {d}
Se dividen en subcarpetas correspondientes a los nombres de las listas de reproducción o Single si la URL es un video individual"""
)
es_messages.url_input_placeholder = "Dirección URL"
es_messages.radio_audio_only = "Sólo audio"
es_messages.radio_video = "Descargar video"
es_messages.clear_button = "Borrar"
es_messages.logs_label = "Registros:"
es_messages.copy_button = "Copiar"
es_messages.start_button = "INICIAR"
es_messages.pause_button = "Pausar"
es_messages.continue_button = "Continuar"
es_messages.exit_button = "Salir"
es_messages.check_url_input_ok = "Ok, presiona el botón de inicio abajo"
es_messages.found_ffmpeg = lambda p: f"Se encontró ffmpeg en: {p}"
es_messages.not_found_ffmpeg = lambda p: f"No se encontró ffmpeg en: {p}"
es_messages.ffmpeg_warning_title = "Dependencia faltante"
es_messages.ffmpeg_warning_message = "No se encontró ffmpeg. Por favor, coloca el archivo ffmpeg en la misma carpeta que la aplicación."
es_messages.invalid_url_message = "Por favor, ingresa una URL de YouTube válida"
es_messages.scanning_videos = "Escaneando información de los videos..."
es_messages.pause_download_message = "Esperando a que presiones continuar..."
es_messages.detached_private_videos = (
    lambda m: f"Hay {m} videos privados que no se pueden descargar"
)
es_messages.finished_message = (
    lambda t, o, p: f"Descarga completada {t} / {o}\n{p}\nPuedes pegar otra URL para continuar descargando o salir si has terminado"
)
es_messages.ffmpeg_error_title = "Error de ffmpeg"
es_messages.ffmpeg_error_message = "Error: ffmpeg no está instalado o no está en el PATH. Por favor, instala ffmpeg y asegúrate de que esté en el PATH del sistema."
es_messages.error = "Error: "
es_messages.copy_logs_title = "Aviso"
es_messages.copy_logs_message = "¡Se han copiado los registros al portapapeles!"
# End Class DiuTupDownloaderApp
# ------------------------------------------------------------------------------------------------------#
# ------------------------------------------------------------------------------------------------------#
# Start Class DownloaderThread
es_messages.instruction = """¡Por favor, pega la URL en el campo de entrada de arriba!
La URL puede ser:

- URL de un video individual
ej: https://www.youtube.com/watch?v=_yC7-iR6t3w&list=PLT1rvk7Trkw4nbIcS1czIII8UoioxkI8V
- URL de una lista de reproducción de videos
ej: https://www.youtube.com/playlist?list=PLT1rvk7Trkw4nbIcS1czIII8UoioxkI8V
- URL de una colección de listas de reproducción de un canal
ej: https://www.youtube.com/@CoComelon/playlists"""
es_messages.playlist_in_channel = (
    lambda m: f"Se encontraron {m} listas de reproducción en el canal"
)
es_messages.unknown_playlist_name = "Nombre de lista de reproducción desconocido"
es_messages.filtering_private_video = (
    lambda m, n: f"Se encontraron {m} videos en la lista de reproducción {n}\nFiltrando videos privados"
)
es_messages.count_private_video = (
    lambda m: f"Hay 1 video privado, quedan {m} videos, continuando el escaneo"
)
es_messages.single_video = "Un video individual"
es_messages.total_percent_downloading = (
    lambda m, n, p, f: f"[{m}/{n}] videos descargando: {p}\n{f}"
)
es_messages.percent_downloading = lambda p, f: f"Descargando video: {p}\n{f}"
es_messages.converting_to_audio = (
    lambda c, t, f: f"[{c}/{t}] videos convirtiéndose a audio:\n{f}"
)
es_messages.signle_converting_to_audio = lambda f: f"Convirtiendo video a audio:\n{f}"
# End Class DownloaderThread
# ------------------------------------------------------------------------------------------------------#
