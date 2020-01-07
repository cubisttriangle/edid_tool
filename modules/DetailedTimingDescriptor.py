from modules.EdidChunk import EdidChunk
from modules.EdidChunkContainer import EdidChunkContainer
from modules.PixelClock import PixelClock
from modules.HzAddressableVideo import HzAddressableVideo

# If questioning any of the hex values I'm using, I find its easiest
# to convert them to binary, so it's easier to see their values.

# Also known as '18-byte Descriptor' or 'Detailed Timing Blocks'. 	
class DetailedTimingDescriptor( EdidChunk ):

    def __init__( self, byte_offset ):

        super( DetailedTimingDescriptor, self ).__init__( "Detailed Timing Descriptor",
                                                           byte_offset, 18 )

    def get_pixel_clock_value( self ):

        return ( ( ( self.bytes[1] & 0xFF ) << 8 ) | self.bytes[0] & 0xFF ) * 10000

    def get_hz_addressable_px( self ):

        return ( ( self.bytes[4] & 0xF0 ) << 4 ) | ( self.bytes[2] & 0xFF )

    def get_vt_addressable_px( self ):

        return ( ( self.bytes[7] & 0xF0 ) << 4 ) | ( self.bytes[5] & 0xFF )

    def get_hz_blanking_px( self ):

        return ( ( self.bytes[4] & 0x0F ) << 8 ) | ( self.bytes[3] & 0xFF )

    def get_vt_blanking_px( self ):

        return ( ( self.bytes[7] & 0x0F ) << 8 ) | ( self.bytes[6] & 0xFF )

    def get_hz_front_porch_px( self ):

        return ( ( self.bytes[11] & 0xC0 ) << 2 ) | ( self.bytes[8] & 0xFF )

    def get_vt_front_porch_ln( self ):

        return ( ( self.bytes[11] & 0x0C ) << 2 ) | ( ( self.bytes[10] & 0xF0 ) >> 4 )

    def get_hz_pulse_width_px( self ):

        return ( ( self.bytes[11] & 0x30 ) << 4 ) | ( self.bytes[9] & 0xFF )

    def get_vt_pulse_width_ln( self ):

        return ( ( self.bytes[11] & 0x03 ) << 8 ) | ( self.bytes[10] & 0x0F )

    def get_hz_addressable_mm( self ):

        return ( ( self.bytes[14] & 0xF0 ) << 4 ) | ( self.bytes[12] & 0xFF )

    def human_readable( self, indent_no = 0 ):

        ind = indent_no + 1

        s = "\n"

        px_clk = "Pixel Clock: {} Hz\n".format( self.get_pixel_clock_value() )
        s = s + self.indented( px_clk, ind )

        hz_addr = "Horizontal Addressable Video: {} pixels\n".format( self.get_hz_addressable_px() )
        s = s + self.indented( hz_addr, ind )

        hz_blnk = "Horizontal Blanking: {} pixels\n".format( self.get_hz_blanking_px() )
        s = s + self.indented( hz_blnk, ind )

        vt_addr = "Vertical Addressable Video: {} pixels\n".format( self.get_vt_addressable_px() )
        s = s + self.indented( vt_addr, ind )

        vt_blnk = "Vertical Blanking: {} pixels\n".format( self.get_vt_blanking_px() )
        s = s + self.indented( vt_blnk, ind )

        hz_fp = "Horizontal Front Porch: {} pixels\n".format( self.get_hz_front_porch_px() )
        s = s + self.indented( hz_fp, ind )

        vt_fp = "Vertical Front Porch: {} lines\n".format( self.get_vt_front_porch_ln() )
        s = s + self.indented( vt_fp, ind )

        hz_pw = "Horizontal Sync Pulse Width: {} pixels\n".format( self.get_hz_pulse_width_px() )
        s = s + self.indented( hz_pw, ind )

        vt_pw = "Vertical Sync Pulse Width: {} lines\n".format( self.get_vt_pulse_width_ln() )
        s = s + self.indented( vt_pw, ind )

        return s
