# -*- coding: utf-8 -*-
from ...Messages import Messages

fr_messages = Messages()
# ------------------------------------------------------------------------------------------------------#
# Start Class SplashScreen
fr_messages.splash_screen_title = "Démarrage"
fr_messages.loading_app = "Ouverture de l'application..."
fr_messages.switch_language = "Changer de langue"
fr_messages.open_app = "Ouvrir l'application"
fr_messages.ready_to_start = "Prêt à commencer !"
# End Class SplashScreen
# ------------------------------------------------------------------------------------------------------#
# ------------------------------------------------------------------------------------------------------#
# Start Class DiuTupDownloaderApp
fr_messages.app_name = "Diu Túp downloader by Paul Pham 157"
fr_messages.download_location_label = (
    lambda d: f"""Les fichiers mp3 seront enregistrés à : {d}
Ils sont répartis dans des sous-dossiers correspondant aux noms des playlists ou Single si l'URL est une vidéo unique"""
)
fr_messages.url_input_placeholder = "Adresse URL"
fr_messages.clear_button = "Effacer"
fr_messages.logs_label = "Journal :"
fr_messages.copy_button = "Copier"
fr_messages.start_button = "DÉMARRER"
fr_messages.pause_button = "Pause"
fr_messages.continue_button = "Continuer"
fr_messages.exit_button = "Quitter"
fr_messages.check_url_input_ok = "OK, appuyez sur le bouton démarrer ci-dessous"
fr_messages.found_ffmpeg = lambda p: f"ffmpeg trouvé à : {p}"
fr_messages.not_found_ffmpeg = lambda p: f"ffmpeg non trouvé à : {p}"
fr_messages.ffmpeg_warning_title = "Dépendance manquante"
fr_messages.ffmpeg_warning_message = "ffmpeg non trouvé. Veuillez placer le fichier ffmpeg dans le même répertoire que l'application."
fr_messages.invalid_url_message = "Veuillez entrer une URL YouTube valide"
fr_messages.scanning_videos = "Analyse des informations vidéo en cours..."
fr_messages.pause_download_message = "En attente que vous appuyiez sur continuer..."
fr_messages.detached_private_videos = (
    lambda m: f"Il y a {m} vidéos privées qui ne peuvent pas être téléchargées"
)
fr_messages.finished_message = (
    lambda t, o, p: f"Téléchargement terminé {t} / {o}\n{p}\nVous pouvez coller une autre URL pour continuer le téléchargement ou quitter si vous avez terminé"
)
fr_messages.ffmpeg_error_title = "Erreur ffmpeg"
fr_messages.ffmpeg_error_message = "Erreur : ffmpeg n'est pas installé ou n'est pas dans le PATH. Veuillez installer ffmpeg et vous assurer qu'il est dans le PATH du système."
fr_messages.error = "Erreur : "
fr_messages.copy_logs_title = "Notification"
fr_messages.copy_logs_message = "Logs copiés dans le presse-papiers !"
# End Class DiuTupDownloaderApp
# ------------------------------------------------------------------------------------------------------#
# ------------------------------------------------------------------------------------------------------#
# Start Class DownloaderThread
fr_messages.instruction = """Veuillez coller l'URL dans l'entrée ci-dessus !
L'URL peut être :

- URL d'une vidéo unique
ex : https://www.youtube.com/watch?v=_yC7-iR6t3w&list=PLT1rvk7Trkw4nbIcS1czIII8UoioxkI8V
- URL d'une playlist vidéo
ex : https://www.youtube.com/playlist?list=PLT1rvk7Trkw4nbIcS1czIII8UoioxkI8V
- URL de compilation des playlists d'une chaîne
ex : https://www.youtube.com/@CoComelon/playlists"""
fr_messages.playlist_in_channel = lambda m: f"Trouvé {m} playlists dans la chaîne"
fr_messages.unknown_playlist_name = "Nom de playlist inconnu"
fr_messages.filtering_private_video = (
    lambda m, n: f"Trouvé {m} vidéos dans la playlist {n}\nFiltrage des vidéos privées"
)
fr_messages.count_private_video = (
    lambda m: f"Il y a 1 vidéo privée, {m} vidéos restantes, poursuite de l'analyse"
)
fr_messages.single_video = "Une vidéo unique"
fr_messages.total_percent_downloading = (
    lambda m, n, p, f: f"[{m}/{n}] vidéos en cours de téléchargement : {p}\n{f}"
)
fr_messages.percent_downloading = lambda p, f: f"Téléchargement de la vidéo : {p}\n{f}"
fr_messages.converting_to_audio = (
    lambda c, t, f: f"[{c}/{t}] vidéos en cours de conversion en audio :\n{f}"
)
fr_messages.signle_converting_to_audio = (
    lambda f: f"Conversion de la vidéo en audio :\n{f}"
)
# End Class DownloaderThread
# ------------------------------------------------------------------------------------------------------#
