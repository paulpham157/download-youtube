# -*- coding: utf-8 -*-
from ...Messages import Messages

hi_messages = Messages()
# ------------------------------------------------------------------------------------------------------#
# Start Class SplashScreen
hi_messages.splash_screen_title = "प्रारंभ हो रहा है"
hi_messages.loading_app = "एप्लिकेशन खोल रहा है..."
hi_messages.switch_language = "भाषा बदलें"
hi_messages.open_app = "एप्लिकेशन खोलें"
hi_messages.ready_to_start = "शुरू करने के लिए तैयार!"
# End Class SplashScreen
# ------------------------------------------------------------------------------------------------------#
# ------------------------------------------------------------------------------------------------------#
# Start Class DiuTupDownloaderApp
hi_messages.app_name = "Diu Túp downloader by Paul Pham 157"
hi_messages.download_location_label = (
    lambda d: f"""mp3, mp4 फाइलें यहां सहेजी जाएंगी: {d}
वे प्लेलिस्ट नामों के अनुसार उप-फ़ोल्डरों में या यदि यूआरएल एक एकल वीडियो है तो सिंगल के रूप में सहेजी जाती हैं"""
)
hi_messages.url_input_placeholder = "यूआरएल पता"
hi_messages.radio_audio_only = "केवल ऑडियो"
hi_messages.radio_video = "वीडियो डाउनलोड करें"
hi_messages.clear_button = "मिटाएं"
hi_messages.logs_label = "लॉग:"
hi_messages.copy_button = "कॉपी करें"
hi_messages.start_button = "शुरू करें"
hi_messages.pause_button = "रोकें"
hi_messages.continue_button = "जारी रखें"
hi_messages.exit_button = "बाहर निकलें"
hi_messages.check_url_input_ok = "ठीक है, नीचे शुरू करें बटन दबाएं"
hi_messages.found_ffmpeg = lambda p: f"ffmpeg यहां पाया गया: {p}"
hi_messages.not_found_ffmpeg = lambda p: f"ffmpeg यहां नहीं मिला: {p}"
hi_messages.ffmpeg_warning_title = "निर्भरता गायब है"
hi_messages.ffmpeg_warning_message = (
    "ffmpeg नहीं मिला। कृपया ffmpeg फ़ाइल को एप्लिकेशन के साथ समान फ़ोल्डर में रखें।"
)
hi_messages.invalid_url_message = "कृपया एक वैध YouTube URL दर्ज करें"
hi_messages.scanning_videos = "वीडियो जानकारी स्कैन कर रहा है..."
hi_messages.pause_download_message = "आपके जारी रखने की प्रतीक्षा कर रहा है..."
hi_messages.detached_private_videos = (
    lambda m: f"{m} निजी वीडियो हैं जो डाउनलोड नहीं किए जा सकते"
)
hi_messages.finished_message = (
    lambda t, o, p: f"डाउनलोड पूरा हो गया {t} / {o}\n{p}\nआप अन्य URL पेस्ट कर सकते हैं या अगर आप समाप्त हो गए हैं तो बाहर निकल सकते हैं"
)
hi_messages.ffmpeg_error_title = "ffmpeg त्रुटि"
hi_messages.ffmpeg_error_message = "त्रुटि: ffmpeg स्थापित नहीं है या PATH में नहीं है। कृपया ffmpeg स्थापित करें और सुनिश्चित करें कि यह सिस्टम PATH में है।"
hi_messages.error = "त्रुटि: "
hi_messages.copy_logs_title = "सूचना"
hi_messages.copy_logs_message = "लॉग्स क्लिपबोर्ड पर कॉपी किए गए!"
# End Class DiuTupDownloaderApp
# ------------------------------------------------------------------------------------------------------#
# ------------------------------------------------------------------------------------------------------#
# Start Class DownloaderThread
hi_messages.instruction = """कृपया ऊपर दिए गए इनपुट में URL पेस्ट करें!
URL हो सकता है:

- एक एकल वीडियो का URL
उदाहरण: https://www.youtube.com/watch?v=_yC7-iR6t3w&list=PLT1rvk7Trkw4nbIcS1czIII8UoioxkI8V
- एक वीडियो प्लेलिस्ट का URL
उदाहरण: https://www.youtube.com/playlist?list=PLT1rvk7Trkw4nbIcS1czIII8UoioxkI8V
- एक चैनल की प्लेलिस्ट का संग्रह URL
उदाहरण: https://www.youtube.com/@CoComelon/playlists"""
hi_messages.playlist_in_channel = lambda m: f"चैनल में {m} प्लेलिस्ट मिली"
hi_messages.unknown_playlist_name = "अज्ञात प्लेलिस्ट नाम"
hi_messages.filtering_private_video = (
    lambda m, n: f"प्लेलिस्ट {n} में {m} वीडियो मिले\nनिजी वीडियो फ़िल्टर कर रहा है"
)
hi_messages.count_private_video = (
    lambda m: f"1 निजी वीडियो है, {m} वीडियो बचे हैं, स्कैन जारी है"
)
hi_messages.single_video = "एक एकल वीडियो"
hi_messages.total_percent_downloading = (
    lambda m, n, p, f: f"[{m}/{n}] वीडियो डाउनलोड हो रहे हैं: {p}\n{f}"
)
hi_messages.percent_downloading = lambda p, f: f"वीडियो डाउनलोड हो रहा है: {p}\n{f}"
hi_messages.converting_to_audio = (
    lambda c, t, f: f"[{c}/{t}] वीडियो ऑडियो में परिवर्तित हो रहे हैं:\n{f}"
)
hi_messages.signle_converting_to_audio = (
    lambda f: f"वीडियो को ऑडियो में परिवर्तित कर रहा है:\n{f}"
)
# End Class DownloaderThread
# ------------------------------------------------------------------------------------------------------#
