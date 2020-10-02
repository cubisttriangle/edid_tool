from modules.EdidChunk import EdidChunk


class ScreenSize(EdidChunk):

    def __init__(self, screen_size=0):

        super(ScreenSize, self).__init__("Screen Size", 1, 2)
        self.set_horz_screen_size(screen_size)

    def set_bytes(self, byte_array):

        self.validate_byte_array(byte_array)
        self.set_horz_screen_size(byte_array[0])
        self.set_vert_screen_size(byte_array[1])

    def set_horz_screen_size(self, param):

        if None == param:
            self.bytes[0] = 0
        else:
            self.bytes[0] = param

    def set_vert_screen_size(self, param):

        if None == param:
            self.bytes[1] = 0
        else:
            self.bytes[1] = param

    def param_to_landscape_ar(self, param):
        return (param + 99.0) / 100.0

    def landscape_ar_to_param(self, ar):
        return (ar * 100) - 99

    def param_to_portrait_ar(self, param):
        return 100 / (param + 99.0)

    def portrait_ar_to_param(self, ar):
        return (100 / ar) - 99

    def human_readable(self, indent=0):

        horz = self.bytes[0]
        vert = self.bytes[1]

        if 0 == vert and 0 == horz:
            return "Undefined, e.g. projector"
        if 0 == vert:
            return "Landcape aspect ratio: {}".format(self.param_to_landscape_ar(horz))
        elif 0 == horz:
            return "Portrait aspect ratio: {}".format(self.param_to_portrait_ar(vert))
        else:
            return "Horizontal (cm): {}; Vertical (cm): {}".format(horz, vert)
