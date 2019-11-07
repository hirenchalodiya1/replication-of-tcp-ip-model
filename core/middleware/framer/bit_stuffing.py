class BitStuffing:
    flag = "01111110"

    def en_frame(self, data):
        frame = ""
        count_1 = 0  # count consecutive 1's
        for k in data:
            if k == "1":
                count_1 += 1
            else:
                count_1 = 0

            if count_1 == 5:
                count_1 = 0
                frame += "10"
            else:
                frame += k
        return self.flag + frame + self.flag

    def de_frame(self, bit_stream):
        raw_frames = bit_stream.split(self.flag)
        frames = []
        for i in raw_frames:
            if not i:
                continue
            count_1 = 0
            frame = ""
            for bit in i:
                if count_1 == 5:
                    count_1 = 0
                    continue
                if bit == "1":
                    count_1 += 1
                else:
                    count_1 = 0
                frame += bit
            frames.append(frame)
        return frames
