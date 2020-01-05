from modules.EdidChunk import EdidChunk

class EstablishedTimingBitmap( EdidChunk ):

    def __init__( self ):
        super( EstablishedTimingBitmap, self ).__init__( 35, 3 )
