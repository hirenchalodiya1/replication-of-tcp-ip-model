import sys
from core.user.server import run_server
from core.user.client import run_client
import core.device.datalink


if __name__ == "__main__":
    args = sys.argv
    if len(args) != 2:
        raise Exception("Please Provide valid number of argument")
    command = args[1]
    if command == "server":
        run_server()
    elif command == "client":
        run_client()
    elif command == "test":
        pass
    else:
        raise Exception("Invalid argument [server | client]")
