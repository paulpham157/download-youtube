# -*- coding: utf-8 -*-
from ...Messages import Messages

de_messages = Messages()
# ------------------------------------------------------------------------------------------------------#
# Start Class SplashScreen
de_messages.splash_screen_title = "Wird gestartet"
de_messages.loading_app = "Anwendung wird geöffnet..."
de_messages.switch_language = "Sprache wechseln"
de_messages.open_app = "Anwendung öffnen"
de_messages.ready_to_start = "Bereit zum Start!"
# End Class SplashScreen
# ------------------------------------------------------------------------------------------------------#
# ------------------------------------------------------------------------------------------------------#
# Start Class DiuTupDownloaderApp
de_messages.app_name = "Diu Túp downloader by Paul Pham 157"
de_messages.download_location_label = (
    lambda d: f"""Die MP3, MP4 -Dateien werden hier gespeichert: {d}
Sie werden in Unterordnern entsprechend den Playlist-Namen oder als Single gespeichert, wenn die URL ein einzelnes Video ist"""
)
de_messages.url_input_placeholder = "URL-Adresse"
de_messages.radio_audio_only = "Nur Audio"
de_messages.radio_video = "Video herunterladen"
de_messages.clear_button = "Löschen"
de_messages.logs_label = "Protokoll:"
de_messages.copy_button = "Kopieren"
de_messages.start_button = "START"
de_messages.pause_button = "Pause"
de_messages.continue_button = "Fortsetzen"
de_messages.exit_button = "Beenden"
de_messages.check_url_input_ok = "OK, drücken Sie den Start-Button unten"
de_messages.found_ffmpeg = lambda p: f"ffmpeg gefunden unter: {p}"
de_messages.not_found_ffmpeg = lambda p: f"ffmpeg nicht gefunden unter: {p}"
de_messages.ffmpeg_warning_title = "Fehlende Abhängigkeit"
de_messages.ffmpeg_warning_message = "ffmpeg nicht gefunden. Bitte legen Sie die ffmpeg-Datei im selben Verzeichnis wie die Anwendung ab."
de_messages.invalid_url_message = "Bitte geben Sie eine gültige YouTube-URL ein"
de_messages.scanning_videos = "Scanne Video-Informationen..."
de_messages.pause_download_message = "Warte darauf, dass Sie fortsetzen..."
de_messages.detached_private_videos = (
    lambda m: f"Es gibt {m} private Videos, die nicht heruntergeladen werden können"
)
de_messages.finished_message = (
    lambda t, o, p: f"Download abgeschlossen {t} / {o}\n{p}\nSie können eine andere URL einfügen, um den Download fortzusetzen, oder beenden, wenn Sie fertig sind"
)
de_messages.ffmpeg_error_title = "ffmpeg-Fehler"
de_messages.ffmpeg_error_message = "Fehler: ffmpeg ist nicht installiert oder nicht im PATH. Bitte installieren Sie ffmpeg und stellen Sie sicher, dass es sich im Systempfad befindet."
de_messages.error = "Fehler: "
de_messages.copy_logs_title = "Benachrichtigung"
de_messages.copy_logs_message = "Logs in die Zwischenablage kopiert!"
# End Class DiuTupDownloaderApp
# ------------------------------------------------------------------------------------------------------#
# ------------------------------------------------------------------------------------------------------#
# Start Class DownloaderThread
de_messages.instruction = """Bitte fügen Sie die URL in das obige Eingabefeld ein!
Die URL kann sein:

- URL eines einzelnen Videos
z.B.: https://www.youtube.com/watch?v=_yC7-iR6t3w&list=PLT1rvk7Trkw4nbIcS1czIII8UoioxkI8V
- URL einer Video-Playlist
z.B.: https://www.youtube.com/playlist?list=PLT1rvk7Trkw4nbIcS1czIII8UoioxkI8V
- URL der Zusammenstellung von Playlists eines Kanals
z.B.: https://www.youtube.com/@CoComelon/playlists"""
de_messages.playlist_in_channel = lambda m: f"{m} Playlists im Kanal gefunden"
de_messages.unknown_playlist_name = "Unbekannter Playlist-Name"
de_messages.filtering_private_video = (
    lambda m, n: f"{m} Videos in der Playlist {n} gefunden\nFiltere private Videos"
)
de_messages.count_private_video = (
    lambda m: f"Es gibt 1 privates Video, {m} Videos verbleiben, Scan wird fortgesetzt"
)
de_messages.single_video = "Ein einzelnes Video"
de_messages.total_percent_downloading = (
    lambda m, n, p, f: f"[{m}/{n}] Videos werden heruntergeladen: {p}\n{f}"
)
de_messages.percent_downloading = lambda p, f: f"Video wird heruntergeladen: {p}\n{f}"
de_messages.converting_to_audio = (
    lambda c, t, f: f"[{c}/{t}] Videos werden in Audio konvertiert:\n{f}"
)
de_messages.signle_converting_to_audio = (
    lambda f: f"Video wird in Audio konvertiert:\n{f}"
)
# End Class DownloaderThread
# ------------------------------------------------------------------------------------------------------#
