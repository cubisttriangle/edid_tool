from modules.EdidChunk import EdidChunk
from modules.EdidHeader import EdidHeader
from modules.BasicDisplayParameters import BasicDisplayParameters
from modules.ChromaticityCoordinates import ChromaticityCoordinates
from modules.EstablishedTimingBitmap import EstablishedTimingBitmap
from modules.StandardTimingInfo import StandardTimingInfo

import struct

class Edid( EdidChunk ):

    attributes = [ 'edid_header', 'basic_display_parameters', 'chromaticity_coordinates',
                   'standard_timing_info' ]

    def __init__( self ):

        super( Edid, self ).__init__( "EDID", 0, 256 )
        self.edid_header = EdidHeader()
        self.basic_display_parameters = BasicDisplayParameters()
        self.chromaticity_coordinates = ChromaticityCoordinates()
        self.standard_timing_info = StandardTimingInfo()

    def load_from_file( self, file_path ):

        with open( file_path, mode = 'rb' ) as edid_file:
            contents = edid_file.read()
            byte_format = "B" * ( len( contents ) // 1 )
            edid_bytes = struct.unpack( byte_format, contents )
            self.set_bytes( edid_bytes )

    def set_bytes( self, byte_array ):

        self.bytes = byte_array

        for attr in self.attributes:
            self.__getattribute__( attr ).get_bytes_from_edid_byte_array( self.bytes )

    def human_readable( self, indent = 0 ):

        s = "\n"

        for attr in self.attributes:
            s = s + "{}\n".format( self.__getattribute__( attr ).info( indent + 1 ) )

        return s
