import settings
from importlib import import_module


def log(msg, verbosity=1):
    if verbosity <= settings.VERBOSITY:
        print(msg)


def load(path):
    module, klass = path.rsplit('.', 1)
    m = import_module(module)
    cls = getattr(m, klass)
    return cls
