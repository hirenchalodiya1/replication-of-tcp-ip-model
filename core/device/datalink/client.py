import settings
from core.utils import load
from core.utils.str_byte_conversion import str2bits


def make_frames(data):
    frames = []
    for i in range(0, len(data), settings.PACKET_SIZE):
        j = min(i+settings.PACKET_SIZE, len(data))
        frames.append(data[i:j])
    return frames


def client_dll(msg):
    data = str2bits(msg)
    checks = load(settings.ERROR_CHECKING)
    error_generator = load(settings.ERROR_GENERATOR)

    frames = make_frames(data)
    frames_to_send = []
    for i in frames:
        frames_to_send.append(error_generator(checks(i).encode()))
    return frames_to_send
