from modules.EdidChunk import EdidChunk

class ManufactureDate( EdidChunk ):

    def __init__( self ):
        super( ManufactureDate, self ).__init__( "Manufacturer Date", 16, 2 )
        self.week = None
        self.year = None
