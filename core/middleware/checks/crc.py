from core.middleware.mod2div import mod2div


# Class used to apply crc to the data
# by appending remainder of modular division
# at the end of data and returning
class CRC:
    def __init__(self, data, key):
        self.data = data
        self.key = key
        self.remainder = ''

    def divide(self):
        l_key = len(self.key)

        # Appends n-1 zeroes at end of data
        appended_data = self.data + '0' * (l_key - 1)
        self.remainder = mod2div(appended_data, self.key)

    def remainder(self):
        return self.remainder

    def codeword(self):
        return self.data + self.remainder
