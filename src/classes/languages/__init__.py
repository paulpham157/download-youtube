from .vi.Messages import vi_messages
from .en.Messages import en_messages
from .bn.Messages import bn_messages
from .zh.Messages import zh_messages
from .fr.Messages import fr_messages
from .de.Messages import de_messages
from .hi.Messages import hi_messages
from .pt.Messages import pt_messages
from .ru.Messages import ru_messages
from .ar.Messages import ar_messages
from .es.Messages import es_messages

lang_code = {
    "vi": {
        "name": "Tiếng Việt",
        "messages": vi_messages,
        "icon": "src/assets/images/Vietnam_Flag.svg",
    },
    "en": {
        "name": "English",
        "messages": en_messages,
        "icon": "src/assets/images/United_Kingdom_Flag.svg",
    },
    "bn": {
        "name": "বাংলা",
        "messages": bn_messages,
        "icon": "src/assets/images/Bangladesh_Flag.svg",
    },
    "zh": {
        "name": "中文",
        "messages": zh_messages,
        "icon": "src/assets/images/China_Flag.svg",
    },
    "fr": {
        "name": "Français",
        "messages": fr_messages,
        "icon": "src/assets/images/France_Flag.svg",
    },
    "de": {
        "name": "Deutsch",
        "messages": de_messages,
        "icon": "src/assets/images/Germany_Flag.svg",
    },
    "hi": {
        "name": "हिंदी",
        "messages": hi_messages,
        "icon": "src/assets/images/India_Flag.svg",
    },
    "pt": {
        "name": "Português",
        "messages": pt_messages,
        "icon": "src/assets/images/Portugal_Flag.svg",
    },
    "ru": {
        "name": "Русский",
        "messages": ru_messages,
        "icon": "src/assets/images/Russia_Flag.svg",
    },
    "ar": {
        "name": "العربية",
        "messages": ar_messages,
        "icon": "src/assets/images/Saudi_Arabia_Flag.svg",
    },
    "es": {
        "name": "Español",
        "messages": es_messages,
        "icon": "src/assets/images/Spain_Flag.svg",
    },
}


def get_messages(lang="vi"):
    if lang in lang_code:
        return lang_code[lang]["messages"]
    else:
        return en_messages


__all__ = ["get_messages", "lang_code"]
