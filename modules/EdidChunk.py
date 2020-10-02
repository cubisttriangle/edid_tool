class EdidChunk(object):

    def __init__(self, name, byte_offset, chunk_len, byte_array=None):

        self.name = name
        self.byte_offset = byte_offset
        self.chunk_len = chunk_len
        if None == byte_array:
            self.clear_bytes()
        else:
            self.validate_byte_array(byte_array)
            self.bytes = byte_array

    def clear_bytes(self):
        self.bytes = [0x00 for i in range(0, self.chunk_len)]

    def get_bytes_from_edid_byte_array(self, byte_array):

        if None == byte_array:
            raise ValueError("EDID array cannot be None")

        if not isinstance(byte_array, (list, tuple)):
            raise ValueError("EDID array must be an array of bytes, but its a {}.".format(type(byte_array)))

        end = self.byte_offset + self.chunk_len

        if len(byte_array) < end:
            raise ValueError("EDID array is not long enough. Expecting {} but got {}.".format(
                end, len(byte_array)
            ))

        self.set_bytes(byte_array[self.byte_offset: end])

    def validate_byte_array(self, byte_array):

        if None == byte_array:
            raise ValueError("byte_array cannot be None")

        if not isinstance(byte_array, (list, tuple)):
            raise ValueError("byte_array must be a list of bytes, but it's a {}.".format(type(byte_array)))

        if len(byte_array) > self.chunk_len:
            raise ValueError(
                "byte_array should {} bytes long, but it is {} bytes long.".format(self.chunk_len, len(byte_array)))

    def format_byte(self, b):

        return "{0:#0{1}x}".format(b, 4).upper()[2:]

    def __str__(self):

        return " ".join([self.format_byte(b) for b in self.bytes]) if None != self.bytes else ""

    def indented(self, string, indented_no):
        return "{}{}".format("  " * indented_no, string)

    def info(self, indent=0):
        byte_str = self.indented("Bytes[{}]: {}".format(len(self.bytes), self.__str__()), indent + 1)
        readable = self.indented("Interpretation: {}".format(self.human_readable(indent + 1)), indent + 1)
        info_str = "{}:\n\n{}\n{}\n".format(self.name, byte_str, readable)
        return self.indented(info_str, indent)

    # Can be overridden to clear all attributes
    def clear(self):

        self.clear_bytes()

    # Can be overridden to parse the byte array and set other member variables.
    def set_bytes(self, byte_array):

        self.validate_byte_array(byte_array)
        self.bytes = byte_array

    # This should be implemented by inherited classes
    def human_readable(self, indent=0):

        return "HR"
        # raise NotImplemented( "human_readable() not implemented!" )
