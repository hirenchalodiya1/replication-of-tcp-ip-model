import settings
from core.utils import load


def server_physical(bit_stream):
    line_schemes = load(settings.LINE_CODING_SCHEME)
    decoded_bit_stream = line_schemes(bit_stream).decode()
    return decoded_bit_stream
