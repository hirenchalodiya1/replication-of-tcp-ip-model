VERBOSITY = 1


def log(msg, verbosity=1):
    if verbosity >= VERBOSITY:
        print(msg)
