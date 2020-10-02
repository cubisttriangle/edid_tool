from modules.EdidChunk import EdidChunk


class EdidChunkContainer(EdidChunk):
    attributes = []

    def __init__(self, name, offset, length):

        super(EdidChunkContainer, self).__init__(name, offset, length)

    def set_bytes(self, byte_array):

        self.validate_byte_array(byte_array)
        self.bytes = byte_array

        for attr in self.attributes:
            self.__getattribute__(attr).get_bytes_from_edid_byte_array(byte_array)

    def human_readable(self, indent=0):

        s = "\n"

        for attr in self.attributes:
            s = s + "\n{}".format(self.__getattribute__(attr).info(indent + 1))

        return s
