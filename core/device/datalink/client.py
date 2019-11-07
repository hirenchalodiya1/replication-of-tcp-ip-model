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
    framer = load(settings.FRAMING_SCHEME)

    frames = make_frames(data)
    frames_to_send = []
    for frame in frames:
        encoded_ = checks(frame).encode()
        errored_ = error_generator(encoded_)
        framed_ = framer().en_frame(errored_)
        frames_to_send.append(framed_)
    return frames_to_send
