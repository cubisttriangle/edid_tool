from modules.EdidChunkContainer import EdidChunkContainer
from modules.EdidHeader import EdidHeader
from modules.BasicDisplayParameters import BasicDisplayParameters
from modules.ChromaticityCoordinates import ChromaticityCoordinates
from modules.EstablishedTimingBitmap import EstablishedTimingBitmap
from modules.StandardTimingInfo import StandardTimingInfo

import struct

class Edid( EdidChunkContainer ):

    attributes = [ 'edid_header', 'basic_display_parameters', 'chromaticity_coordinates',
                   'established_timings', 'standard_timing_info' ]

    def __init__( self ):

        super( Edid, self ).__init__( "EDID", 0, 256 )
        self.edid_header = EdidHeader()
        self.basic_display_parameters = BasicDisplayParameters()
        self.chromaticity_coordinates = ChromaticityCoordinates()
        self.established_timings = EstablishedTimingBitmap()
        self.standard_timing_info = StandardTimingInfo()

    def load_from_file( self, file_path ):

        with open( file_path, mode = 'rb' ) as edid_file:
            contents = edid_file.read()
            if len( contents ) == 0:
                raise ValueError( "Edid file is empty: '{}'".format( file_path ) )
            byte_format = "B" * ( len( contents ) // 1 )
            edid_bytes = struct.unpack( byte_format, contents )
            self.set_bytes( edid_bytes )
