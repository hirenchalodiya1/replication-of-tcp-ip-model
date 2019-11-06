import settings
from core.utils import load
from core.utils.str_byte_conversion import bits2str


def server_dll(frames):
    data = ""
    checks = load(settings.ERROR_CHECKING)
    for i in frames:
        decoded = checks(i).decode()
        if decoded != "":
            data += bits2str(decoded)
        else:
            return ""
    return data
