from modules.EdidChunkContainer import EdidChunkContainer
from modules.FixedHeaderPattern import FixedHeaderPattern
from modules.ManufacturerId import ManufacturerId
from modules.ProductCode import ProductCode
from modules.SerialNumber import SerialNumber
from modules.ManufactureDate import ManufactureDate
from modules.Version import Version


class EdidHeader(EdidChunkContainer):
    attributes = ['header_pattern', 'manufacturer_id', 'product_code',
                  'serial_number', 'manufacture_date', 'version']

    def __init__(self):
        super(EdidHeader, self).__init__("Header", 0, 20)

        self.header_pattern = FixedHeaderPattern()
        self.manufacturer_id = ManufacturerId()
        self.product_code = ProductCode()
        self.serial_number = SerialNumber()
        self.manufacture_date = ManufactureDate()
        self.version = Version()
