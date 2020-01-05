from modules.EdidChunk import EdidChunk

class Version( EdidChunk ):

    def __init__( self ):
        super( Version, self ).__init__( "Version", 18, 2 )
        self.version = None
        self.revisio = None

