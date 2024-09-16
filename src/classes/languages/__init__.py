from .vi.Messages import vi_messages
from .en.Messages import en_messages

lang_code = {
    "vi": {"name": "Tiếng Việt", "messages": vi_messages},
    "en": {"name": "English", "messages": en_messages},
}


def get_messages(lang="vi"):
    if lang in lang_code:
        return lang_code[lang]["messages"]
    else:
        return en_messages


__all__ = ["get_messages", "lang_code"]
