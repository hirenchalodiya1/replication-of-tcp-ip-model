class NRZ:
    def __init__(self, data):
        self.data = data


class NRZI(NRZ):
    def encode(self):
        enc_data = "0"
        cur_bit = "0"
        for char in self.data[1:]:
            if char == cur_bit:
                enc_data += "0"
            else:
                cur_bit = char
                enc_data += "1"
        return enc_data

    def decode(self):
        bit_data = "0"
        cur_bit = "0"
        for char in self.data[1:]:
            if char == "1":
                cur_bit = "0" if cur_bit == "1" else "1"
            bit_data += cur_bit
        return bit_data


class NRZL(NRZ):
    def encode(self):
        enc_data = ""
        for char in self.data:
            if char == "0":
                enc_data += "1"
            else:
                enc_data += "0"
        return enc_data

    def decode(self):
        bit_data = ""
        for char in self.data:
            if char == "0":
                bit_data += "1"
            else:
                bit_data += "0"
        return bit_data
