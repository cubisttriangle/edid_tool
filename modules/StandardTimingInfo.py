from modules.EdidChunk import EdidChunk

class StandardTimingInfo( EdidChunk ):

    ar_map = {
        0b00: "16:10",
        0b01: "4:3",
        0b10: "5:4",
        0b11: "16:9"
    }

    def __init__( self ):
        # Initialize to 'unused' values.
        b = [ 0x01 for i in range( 0, 15 ) ]
        super( StandardTimingInfo, self ).__init__( "Standard Timing Information", 38, 16, b )

    def human_readable( self, indent_no = 0 ):

        timings = []

        it = iter( self.bytes )
        idx = 1
        for a, b in zip( it, it ):

            t  = "Standard Timing {}".format( idx )
            hz = ""
            ar = ""
            rr = ""

            if 0x00 == a:
                hz = "WARNING: Reserved!"
            elif 0x01 == a:
                hz = ""
            else:
                hz = ( a + 31 ) * 8
                hz = "Horizontal addressable pixels: {}".format( hz )

            if 0x01 == b:
                rr = ""
            else:
                ar = self.ar_map[ ( b & 0b11000000 ) >> 6 ]
                ar = "Aspect Ratio: {}".format( ar )
                rr = ( b & 0b00111111 ) + 60
                rr = "Refresh Rate (Hz): {}".format( rr )

            if len( hz ) == 0 and len( ar ) == 0 and len( rr ) == 0:
                t = "{}: Unused".format( t )
            else:
                t = "{}: {}; {}; {} ".format( t, hz, ar, rr )

            idx = idx + 1

            timings.append( "\n{}".format( self.indented( t, indent_no + 1 )  ) )

        return "".join( timings )
