import settings
from core.utils import load


def make_frames(data):
    frames = []
    for i in range(0, len(data), settings.PACKET_SIZE):
        j = min(i+settings.PACKET_SIZE, len(data))
        frames.append(data[i:j])
    return frames


def client_dll(msg):
    encoded_data = load(settings.ERROR_CHECKING)(msg).encode()
    frames = make_frames(encoded_data)
    error_generator = load(settings.ERROR_GENERATOR)
    frames_to_send = []
    for i in frames:
        frames_to_send.append(error_generator(i))
    return frames_to_send
