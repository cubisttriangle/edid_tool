from modules.EdidChunk import EdidChunk

class ManufacturerId( EdidChunk ):

    letters = [ 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
                'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' ]

    def __init__( self, id_str = None ):

        super( ManufacturerId, self ).__init__( "Manufacturer ID", 8, 2 )

        self.id = None

        if None != id_str:
            self.set_id( id_str )

    def char_to_int( self, char ):

        c = char.upper()

        for idx, letter in enumerate( self.letters ):
            if c == letter:
                return idx + 1

        raise ValueError( "Can't convert char to int: {}". format( c ) )

    def int_to_char( self, i ):
        return self.letters[i - 1]

    def print_char( self, char ):

        char_as_int = self.char_to_int( char )
        print( "{}: {}, {}".format( char, self.format_byte( char_as_int ), bin( char_as_int ) ) )

    def set_id( self, id_str ):

        if not isinstance( id_str, str ):
            raise ValueError()

        if len( id_str ) != 3:
            raise ValueError( "id_str should be three letters long." )

        self.id = id_str

        self.print_char( self.id[0] )
        self.print_char( self.id[1] )
        self.print_char( self.id[2] )

        num = self.char_to_int( self.id[0] ) << 10
        num = num | ( self.char_to_int( self.id[1] ) << 5 )
        num = num | self.char_to_int( self.id[2] )

        self.bytes = [ ( num >> 8 ), ( num & 0x00FF ) ]

        return self.bytes

    def set_bytes( self, byte_array ):

        self.validate_byte_array( byte_array )
        self.bytes = byte_array

        num = ( self.bytes[0] << 8 ) | self.bytes[1]

        self.id = self.int_to_char( num >> 10 )
        self.id = self.id + self.int_to_char( ( num & 0x3E0 ) >> 5 )
        self.id = self.id + self.int_to_char( num & 0x1F )

    def human_readable( self, indent ):
        return self.id
