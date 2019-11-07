class Manchester:
    def __init__(self, data):
        self.data = data

    def encode(self):
        enc_data = ""
        for bit in self.data:
            if bit == "0":
                enc_data += "1-1"
            else:
                enc_data += "-11"
        return enc_data

    def decode(self):
        bit_data = ""
        for i in range(0, len(self.data), 3):
            j = i + 3
            bit = self.data[i:j]
            if bit == "1-1":
                bit_data += "0"
            elif bit == "-11":
                bit_data += "1"
        return bit_data
