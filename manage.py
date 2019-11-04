import sys


if __name__ == "__main__":
    args = sys.argv
    if len(args) != 2:
        raise Exception("Please Provide valid number of argument")
    command = args[1]
    if command == "server":
        # run server code
        pass
    elif command == "client":
        # run client code
        pass
    else:
        raise Exception("Invalid argument [server | client]")
