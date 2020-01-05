from modules.EdidChunk import EdidChunk

class SerialNumber( EdidChunk ):

    def __init__( self ):

        super( SerialNumber, self ).__init__( "Serial Number", 12, 3 )
