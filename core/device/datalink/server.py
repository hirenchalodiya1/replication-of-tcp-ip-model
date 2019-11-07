import settings
from core.utils import load
from core.utils.str_byte_conversion import bits2str


def server_dll(bit_stream):
    data = ""
    checks = load(settings.ERROR_CHECKING)
    framer = load(settings.FRAMING_SCHEME)
    frames = framer().de_frame(bit_stream)
    for frame in frames:
        decoded = checks(frame).decode()
        if decoded != "":
            data += bits2str(decoded)
        else:
            return ""
    return data
