# -*- coding: utf-8 -*-
from ...Messages import Messages

bn_messages = Messages()
# ------------------------------------------------------------------------------------------------------#
# Start Class SplashScreen
bn_messages.splash_screen_title = "শুরু হচ্ছে"
bn_messages.loading_app = "অ্যাপ্লিকেশন খোলা হচ্ছে..."
bn_messages.switch_language = "ভাষা পরিবর্তন করুন"
bn_messages.open_app = "অ্যাপ্লিকেশন খুলুন"
bn_messages.ready_to_start = "শুরু করতে প্রস্তুত!"
# End Class SplashScreen
# ------------------------------------------------------------------------------------------------------#
# ------------------------------------------------------------------------------------------------------#
# Start Class DiuTupDownloaderApp
bn_messages.app_name = "পল ফাম ১৫৭ দ্বারা ডিউ টুপ ডাউনলোডার"
bn_messages.download_location_label = (
    lambda d: f"""এমপি৩ ফাইলগুলি এখানে সংরক্ষিত হবে: {d}
এগুলি প্লেলিস্টের নাম অনুযায়ী সাব-ফোল্ডারে বিভক্ত হবে অথবা একক ভিডিওর ক্ষেত্রে সিঙ্গেল ফোল্ডারে থাকবে"""
)
bn_messages.url_input_placeholder = "URL ঠিকানা"
bn_messages.clear_button = "মুছুন"
bn_messages.logs_label = "লগ:"
bn_messages.copy_button = "কপি করুন"
bn_messages.start_button = "শুরু করুন"
bn_messages.pause_button = "বিরতি"
bn_messages.continue_button = "চালিয়ে যান"
bn_messages.exit_button = "প্রস্থান"
bn_messages.check_url_input_ok = "ঠিক আছে, নিচের শুরু বোতামে ক্লিক করুন"
bn_messages.found_ffmpeg = lambda p: f"ffmpeg পাওয়া গেছে: {p}"
bn_messages.not_found_ffmpeg = lambda p: f"ffmpeg পাওয়া যায়নি: {p}"
bn_messages.ffmpeg_warning_title = "নির্ভরতা অনুপস্থিত"
bn_messages.ffmpeg_warning_message = (
    "ffmpeg পাওয়া যায়নি। অনুগ্রহ করে অ্যাপ্লিকেশনের ফোল্ডারে ffmpeg ফাইল রাখুন।"
)
bn_messages.invalid_url_message = "অনুগ্রহ করে একটি বৈধ YouTube URL লিখুন"
bn_messages.scanning_videos = "ভিডিও তথ্য স্ক্যান করা হচ্ছে..."
bn_messages.pause_download_message = "আপনার চালিয়ে যাওয়ার জন্য অপেক্ষা করছি..."
bn_messages.detached_private_videos = lambda m: f"{m}টি ব্যক্তিগত ভিডিও ডাউনলোড করা যায়নি"
bn_messages.finished_message = (
    lambda t, o, p: f"{o}টির মধ্যে {t}টি ডাউনলোড সম্পন্ন হয়েছে\n{p}\nআরও ডাউনলোড করতে অন্য URL পেস্ট করুন অথবা শেষ হলে প্রস্থান করুন"
)
bn_messages.ffmpeg_error_title = "ffmpeg ত্রুটি"
bn_messages.ffmpeg_error_message = "ত্রুটি: ffmpeg ইনস্টল করা নেই বা PATH-এ নেই। অনুগ্রহ করে ffmpeg ইনস্টল করুন এবং নিশ্চিত করুন যে এটি সিস্টেম PATH-এ আছে।"
bn_messages.error = "ত্রুটি: "
bn_messages.copy_logs_title = "বিজ্ঞপ্তি"
bn_messages.copy_logs_message = "লগ ক্লিপবোর্ডে কপি করা হয়েছে!"
# End Class DiuTupDownloaderApp
# ------------------------------------------------------------------------------------------------------#
# ------------------------------------------------------------------------------------------------------#
# Start Class DownloaderThread
bn_messages.instruction = """উপরের ইনপুটে URL ঠিকানা পেস্ট করুন!
নিম্নলিখিত URL গুলি পেস্ট করা যেতে পারে:

- একটি একক ভিডিওর URL
উদাহরণ: https://www.youtube.com/watch?v=_yC7-iR6t3w&list=PLT1rvk7Trkw4nbIcS1czIII8UoioxkI8V
- একটি ভিডিও প্লেলিস্টের URL
উদাহরণ: https://www.youtube.com/playlist?list=PLT1rvk7Trkw4nbIcS1czIII8UoioxkI8V
- একটি চ্যানেলের সমস্ত প্লেলিস্টের সংকলন URL
উদাহরণ: https://www.youtube.com/@CoComelon/playlists"""
bn_messages.playlist_in_channel = lambda m: f"চ্যানেলে {m}টি প্লেলিস্ট পাওয়া গেছে"
bn_messages.unknown_playlist_name = "অজানা প্লেলিস্টের নাম"
bn_messages.filtering_private_video = (
    lambda m, n: f"{n} প্লেলিস্টে {m}টি ভিডিও পাওয়া গেছে\nব্যক্তিগত ভিডিও ফিল্টার করা হচ্ছে"
)
bn_messages.count_private_video = (
    lambda m: f"একটি ব্যক্তিগত ভিডিও আছে, {m}টি ভিডিও বাকি আছে, স্ক্যান চলছে"
)
bn_messages.single_video = "একটি একক ভিডিও"
bn_messages.total_percent_downloading = (
    lambda m, n, p, f: f"[{m}/{n}] ভিডিও ডাউনলোড হচ্ছে: {p}\n{f}"
)
bn_messages.percent_downloading = lambda p, f: f"ভিডিও ডাউনলোড হচ্ছে: {p}\n{f}"
bn_messages.converting_to_audio = (
    lambda c, t, f: f"[{c}/{t}] ভিডিও অডিওতে রূপান্তর করা হচ্ছে:\n{f}"
)
bn_messages.signle_converting_to_audio = lambda f: f"ভিডিও অডিওতে রূপান্তর করা হচ্ছে:\n{f}"
# End Class DownloaderThread
# ------------------------------------------------------------------------------------------------------#
