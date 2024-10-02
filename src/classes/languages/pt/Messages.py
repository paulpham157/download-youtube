# -*- coding: utf-8 -*-
from ...Messages import Messages

pt_messages = Messages()
# ------------------------------------------------------------------------------------------------------#
# Start Class SplashScreen
pt_messages.splash_screen_title = "Iniciando"
pt_messages.loading_app = "Abrindo o aplicativo..."
pt_messages.switch_language = "Mudar idioma"
pt_messages.open_app = "Abrir aplicativo"
pt_messages.ready_to_start = "Pronto para começar!"
# End Class SplashScreen
# ------------------------------------------------------------------------------------------------------#
# ------------------------------------------------------------------------------------------------------#
# Start Class DiuTupDownloaderApp
pt_messages.app_name = "Diu Túp downloader by Paul Pham 157"
pt_messages.download_location_label = (
    lambda d: f"""Os arquivos mp3, mp4 serão salvos em: {d}
Eles são divididos em subpastas correspondentes aos nomes das playlists ou Single se o URL for um vídeo único"""
)
pt_messages.url_input_placeholder = "Endereço URL"
pt_messages.radio_audio_only = "Somente áudio"
pt_messages.radio_video = "Baixar vídeo"
pt_messages.clear_button = "Limpar"
pt_messages.logs_label = "Registros:"
pt_messages.copy_button = "Copiar"
pt_messages.start_button = "INICIAR"
pt_messages.pause_button = "Pausar"
pt_messages.continue_button = "Continuar"
pt_messages.exit_button = "Sair"
pt_messages.check_url_input_ok = "Ok, clique no botão iniciar abaixo"
pt_messages.found_ffmpeg = lambda p: f"FFmpeg encontrado em: {p}"
pt_messages.not_found_ffmpeg = lambda p: f"FFmpeg não encontrado em: {p}"
pt_messages.ffmpeg_warning_title = "Dependência ausente"
pt_messages.ffmpeg_warning_message = "FFmpeg não encontrado. Por favor, coloque o arquivo ffmpeg na mesma pasta do aplicativo."
pt_messages.invalid_url_message = "Por favor, insira um URL do YouTube válido"
pt_messages.scanning_videos = "Escaneando informações dos vídeos..."
pt_messages.pause_download_message = "Aguardando você clicar em continuar..."
pt_messages.detached_private_videos = (
    lambda m: f"Há {m} vídeos privados que não podem ser baixados"
)
pt_messages.finished_message = (
    lambda t, o, p: f"Download concluído {t} / {o}\n{p}\nVocê pode colar outro URL para continuar baixando ou sair se tiver terminado"
)
pt_messages.ffmpeg_error_title = "Erro do FFmpeg"
pt_messages.ffmpeg_error_message = "Erro: FFmpeg não está instalado ou não está no PATH. Por favor, instale o FFmpeg e certifique-se de que ele esteja no PATH do sistema."
pt_messages.error = "Erro: "
pt_messages.copy_logs_title = "Aviso"
pt_messages.copy_logs_message = "Logs copiados para a área de transferência!"
# End Class DiuTupDownloaderApp
# ------------------------------------------------------------------------------------------------------#
# ------------------------------------------------------------------------------------------------------#
# Start Class DownloaderThread
pt_messages.instruction = """Cole o endereço URL na entrada acima!
O URL pode ser:

- URL de um único vídeo
ex: https://www.youtube.com/watch?v=_yC7-iR6t3w&list=PLT1rvk7Trkw4nbIcS1czIII8UoioxkI8V
- URL de uma playlist de vídeos
ex: https://www.youtube.com/playlist?list=PLT1rvk7Trkw4nbIcS1czIII8UoioxkI8V
- URL de compilação de playlists de um canal
ex: https://www.youtube.com/@CoComelon/playlists"""
pt_messages.playlist_in_channel = lambda m: f"Encontradas {m} playlists no canal"
pt_messages.unknown_playlist_name = "Nome da Playlist desconhecido"
pt_messages.filtering_private_video = (
    lambda m, n: f"Encontrados {m} vídeos na playlist {n}\nFiltrando vídeos privados"
)
pt_messages.count_private_video = (
    lambda m: f"Há 1 vídeo privado, restam {m} vídeos, continuando a escanear"
)
pt_messages.single_video = "Um único vídeo"
pt_messages.total_percent_downloading = (
    lambda m, n, p, f: f"[{m}/{n}] vídeos baixando: {p}\n{f}"
)
pt_messages.percent_downloading = lambda p, f: f"Baixando vídeo: {p}\n{f}"
pt_messages.converting_to_audio = (
    lambda c, t, f: f"[{c}/{t}] vídeos convertendo para áudio:\n{f}"
)
pt_messages.signle_converting_to_audio = lambda f: f"Convertendo vídeo para áudio:\n{f}"
# End Class DownloaderThread
# ------------------------------------------------------------------------------------------------------#
