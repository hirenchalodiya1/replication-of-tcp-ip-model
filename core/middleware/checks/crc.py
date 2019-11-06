from core.middleware.mod2div import mod2div


# Class used to apply crc to the data
# by appending remainder of modular division
# at the end of data and returning
class CRC:
    def __init__(self, data):
        self.data = data
        self.key = "1001"
        self.remainder = ''
        self.divide()

    def divide(self):
        l_key = len(self.key)

        # Appends n-1 zeroes at end of data
        appended_data = self.data + '0' * (l_key - 1)
        self.remainder = mod2div(appended_data, self.key)

    def codeword(self):
        return self.data + self.remainder

    def encode(self):
        return self.data + self.remainder

    def decode(self):
        zeroes = "0" * (len(self.key) - 1)
        if self.remainder == zeroes:
            print("Remainder after decoding is: " + self.remainder)
            return self.data[:-(len(self.key) - 1)]
        else:
            return ""
