from modules.EdidChunk import EdidChunk


class FixedHeaderPattern(EdidChunk):

    def __init__(self):
        super(FixedHeaderPattern, self).__init__("Fixed Header Pattern", 0, 8,
                                                 [0x00, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0x00])

    def human_readable(self, indent):
        return self.__str__()
