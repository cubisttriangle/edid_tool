from modules.EdidChunk import EdidChunk
from modules.FixedHeaderPattern import FixedHeaderPattern
from modules.ManufacturerId import ManufacturerId
from modules.ProductCode import ProductCode
from modules.SerialNumber import SerialNumber
from modules.ManufactureDate import ManufactureDate
from modules.Version import Version

class EdidHeader( EdidChunk ):

    attributes = [ 'header_pattern', 'manufacturer_id', 'product_code',
                   'serial_number', 'manufacture_date', 'version' ]

    def __init__( self ):

        super( EdidHeader, self ).__init__( "Header", 0, 20 )

        self.header_pattern = FixedHeaderPattern()
        self.manufacturer_id = ManufacturerId()
        self.product_code = ProductCode()
        self.serial_number = SerialNumber()
        self.manufacture_date = ManufactureDate()
        self.version = Version()

    def set_bytes( self, byte_array ):

        self.validate_byte_array( byte_array )
        self.bytes = byte_array

        for attr in self.attributes:
            self.__getattribute__( attr ).get_bytes_from_edid_byte_array( self.bytes )

    def human_readable( self, indent = 0 ):

        s = "\n"

        for attr in self.attributes:
            s = s + "{}\n".format( self.__getattribute__( attr ).info( indent + 1 ) )

        return s
        
