import settings
from core.utils import load


def client_physical(frames):
    line_schemes = load(settings.LINE_CODING_SCHEME)
    encoded_frames = []
    for frame in frames:
        encoded_ = line_schemes(frame).encode()
        encoded_frames.append(encoded_)
    return encoded_frames
