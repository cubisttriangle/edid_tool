from modules.EdidChunk import EdidChunk


class EstablishedTimingBitmap(EdidChunk):
    timings = {
        0: {
            7: "720x400 @ 70 Hz (VGA)",
            6: "720x400 @ 88 Hz (XGA)",
            5: "640x480 @ 60 Hz (VGA)",
            4: "640x480 @ 67 Hz (Apple Macintosh II)",
            3: "640x480 @ 72 Hz",
            2: "640x480 @ 75 Hz",
            1: "800x600 @ 56 Hz",
            0: "800x600 @ 60 Hz"
        },

        1: {
            7: "800x600 @ 72 Hz",
            6: "800x600 @ 75 Hz",
            5: "832x624 @ 75 Hz (Apple Macintosh II)",
            4: "1024x768 @ 87 Hz, interlaced (1024x768i)",
            3: "1024x768 @ 60 Hz",
            2: "1024x768 @ 70 Hz",
            1: "1024x768 @ 75 Hz",
            0: "1280x1024 @ 75 Hz"
        },

        2: {
            7: "1152x870 @ 75 Hz (Apple Macintosh II)"
        }
    }

    def __init__(self):

        super(EstablishedTimingBitmap, self).__init__("Established Timing Modes", 35, 3)

    def get_supported_timings(self):

        timings = []

        for idx, bitfield in enumerate(self.bytes):

            for key, val in self.timings[idx].items():

                timing_supported = (bitfield >> key) & 1

                if timing_supported:
                    timings.append(val)

        return timings

    def human_readable(self, indent_no=0):

        supported = self.get_supported_timings()

        if len(supported) == 0:
            return "Unused"
        else:
            return "".join(["\n{}".format(self.indented(timing, indent_no + 1)) for timing in supported])
