# -*- coding: utf-8 -*-
from ...Messages import Messages

ar_messages = Messages()
# ------------------------------------------------------------------------------------------------------#
# Start Class SplashScreen
ar_messages.splash_screen_title = "جاري التشغيل"
ar_messages.loading_app = "جاري فتح التطبيق..."
ar_messages.switch_language = "تغيير اللغة"
ar_messages.open_app = "فتح التطبيق"
ar_messages.ready_to_start = "جاهز للبدء!"
# End Class SplashScreen
# ------------------------------------------------------------------------------------------------------#
# ------------------------------------------------------------------------------------------------------#
# Start Class DiuTupDownloaderApp
ar_messages.app_name = "Diu Túp downloader by Paul Pham 157"
ar_messages.download_location_label = (
    lambda d: f"""سيتم حفظ ملفات MP3, MP4 في: {d}
يتم تقسيمها إلى مجلدات فرعية تتوافق مع أسماء قوائم التشغيل أو Single إذا كان عنوان URL لفيديو واحد"""
)
ar_messages.url_input_placeholder = "عنوان URL"
ar_messages.radio_audio_only = "صوت فقط"
ar_messages.radio_video = "تنزيل الفيديو"
ar_messages.clear_button = "مسح"
ar_messages.logs_label = "السجلات:"
ar_messages.copy_button = "نسخ"
ar_messages.start_button = "بدء"
ar_messages.pause_button = "إيقاف مؤقت"
ar_messages.continue_button = "استمرار"
ar_messages.exit_button = "خروج"
ar_messages.check_url_input_ok = "حسنًا، اضغط على زر البدء أدناه"
ar_messages.found_ffmpeg = lambda p: f"تم العثور على ffmpeg في: {p}"
ar_messages.not_found_ffmpeg = lambda p: f"لم يتم العثور على ffmpeg في: {p}"
ar_messages.ffmpeg_warning_title = "تبعية مفقودة"
ar_messages.ffmpeg_warning_message = (
    "لم يتم العثور على ffmpeg. يرجى وضع ملف ffmpeg في نفس المجلد مع التطبيق."
)
ar_messages.invalid_url_message = "يرجى إدخال عنوان URL صالح لـ YouTube"
ar_messages.scanning_videos = "جارٍ مسح معلومات الفيديوهات..."
ar_messages.pause_download_message = "في انتظار الضغط على استمرار..."
ar_messages.detached_private_videos = lambda m: f"هناك {m} فيديو خاص لا يمكن تنزيله"
ar_messages.finished_message = (
    lambda t, o, p: f"اكتمل التنزيل {t} / {o}\n{p}\nيمكنك لصق عنوان URL آخر للاستمرار في التنزيل أو الخروج إذا انتهيت"
)
ar_messages.ffmpeg_error_title = "خطأ في ffmpeg"
ar_messages.ffmpeg_error_message = "خطأ: لم يتم تثبيت ffmpeg أو غير موجود في PATH. يرجى تثبيت ffmpeg والتأكد من وجوده في PATH النظام."
ar_messages.error = "خطأ: "
ar_messages.copy_logs_title = "إشعار"
ar_messages.copy_logs_message = "تم نسخ السجلات إلى الحافظة!"
# End Class DiuTupDownloaderApp
# ------------------------------------------------------------------------------------------------------#
# ------------------------------------------------------------------------------------------------------#
# Start Class DownloaderThread
ar_messages.instruction = """يرجى لصق عنوان URL في حقل الإدخال أعلاه!
يمكن أن يكون عنوان URL:

- عنوان URL لفيديو واحد
مثال: https://www.youtube.com/watch?v=_yC7-iR6t3w&list=PLT1rvk7Trkw4nbIcS1czIII8UoioxkI8V
- عنوان URL لقائمة تشغيل الفيديوهات
مثال: https://www.youtube.com/playlist?list=PLT1rvk7Trkw4nbIcS1czIII8UoioxkI8V
- عنوان URL لمجموعة قوائم التشغيل لقناة
مثال: https://www.youtube.com/@CoComelon/playlists"""
ar_messages.playlist_in_channel = lambda m: f"تم العثور على {m} قائمة تشغيل في القناة"
ar_messages.unknown_playlist_name = "اسم قائمة التشغيل غير معروف"
ar_messages.filtering_private_video = (
    lambda m, n: f"تم العثور على {m} فيديو في قائمة التشغيل {n}\nجارٍ تصفية الفيديوهات الخاصة"
)
ar_messages.count_private_video = (
    lambda m: f"هناك فيديو خاص واحد، بقي {m} فيديو، جارٍ متابعة المسح"
)
ar_messages.single_video = "فيديو واحد"
ar_messages.total_percent_downloading = (
    lambda m, n, p, f: f"[{m}/{n}] فيديوهات قيد التنزيل: {p}\n{f}"
)
ar_messages.percent_downloading = lambda p, f: f"جارٍ تنزيل الفيديو: {p}\n{f}"
ar_messages.converting_to_audio = (
    lambda c, t, f: f"[{c}/{t}] فيديوهات قيد التحويل إلى صوت:\n{f}"
)
ar_messages.signle_converting_to_audio = lambda f: f"جارٍ تحويل الفيديو إلى صوت:\n{f}"
# End Class DownloaderThread
# ------------------------------------------------------------------------------------------------------#
