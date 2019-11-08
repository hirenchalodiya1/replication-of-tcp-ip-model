from decouple import config

# server host and port
SERVER_HOST = config("SERVER_HOST", cast=str, default="localhost")
SERVER_PORT = config("SERVER_PORT", cast=int, default=6783)

# verbosity
VERBOSITY = config("VERBOSITY", cast=int, default=1)

# Error checking scheme
ERROR_CHECKING = config("ERROR_CHECKING", cast=str)

# CRC settings
CRC_KEY = config("CRC_KEY", cast=str, default="1001")

# Error generator scheme
ERROR_GENERATOR = config("ERROR_GENERATOR", cast=str)
ERROR_MAX_BITS = 2
ERROR_DISTRIBUTION = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                      1, 1, 1, 1, 1, 1, 2, 2, 2, 3]

# Frame Settings
PACKET_SIZE = 32
FRAMING_SCHEME = config("FRAMING_SCHEME", cast=str)

# Line Coding Schemes
LINE_CODING_SCHEME = config("LINE_CODING_SCHEME", cast=str)
