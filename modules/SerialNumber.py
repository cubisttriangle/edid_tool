from modules.EdidChunk import EdidChunk


class SerialNumber(EdidChunk):

    def __init__(self, serial_number=None):

        super(SerialNumber, self).__init__("Serial Number", 12, 3)
        self.set_serial_number(serial_number)

    def set_serial_number(self, serial_number):

        if None == serial_number:
            self.serial_number = 0
            self.clear_bytes()
        else:
            self.serial_number = serial_number
            self.bytes = [
                serial_number & 0xFF,
                (serial_number >> 8) & 0xFF,
                (serial_number >> 16) & 0xFF
            ]

    def set_bytes(self, byte_array):

        self.validate_byte_array(byte_array)

        self.bytes = byte_array

        self.serial_number = (byte_array[2] << 16) | \
                             (byte_array[1] & 0xFF) << 8 | \
                             (byte_array[0] & 0xFF)

    def human_readable(self, indent_no=0):

        return self.serial_number
