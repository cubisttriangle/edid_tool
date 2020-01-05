from modules.EdidChunk import EdidChunk

class StandardTimingInfo( EdidChunk ):

    def __init__( self ):
        super( StandardTimingInfo, self ).__init__( "Standard Timing Information", 38, 16 )
