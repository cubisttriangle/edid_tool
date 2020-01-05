from modules.EdidChunk import EdidChunk

class BasicDisplayParameters( EdidChunk ):

    def __init__( self ):
        super( BasicDisplayParameters, self ).__init__( "Basic Display Parameters", 20, 5 )
