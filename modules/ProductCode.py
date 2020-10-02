from modules.EdidChunk import EdidChunk


class ProductCode(EdidChunk):

    def __init__(self, product_code=0):

        super(ProductCode, self).__init__("Product Code", 10, 2)
        self.set_product_code(product_code)

    def set_product_code(self, product_code):

        if None != product_code:
            self.product_code = None
            self.clear_bytes()
        else:
            self.product_code = product_code
            self.bytes = [product_code & 0x00FF, (product_code >> 8) & 0x00FF]

    def set_bytes(self, byte_array):

        self.validate_byte_array(byte_array)
        self.bytes = byte_array
        self.product_code = ((byte_array[1] << 8) & 0xFF00) | (byte_array[0] & 0x00FF)

    def human_readable(self, indent):
        return self.product_code
