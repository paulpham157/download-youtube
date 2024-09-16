from .vi.Messages import vi_messages
from .en.Messages import en_messages


def get_messages(lang="vi"):
    if lang == "vi":
        return vi_messages
    elif lang == "en":
        return en_messages
    else:
        raise ValueError(f"Language not supported: {lang}")


__all__ = ["get_messages"]
