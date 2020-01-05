from modules.EdidChunk import EdidChunk

class VideoInputParameters( EdidChunk ):

    # Bits per color
    bit_depth_map = {
        0b000: "Undefined",
        0b001: "6",
        0b010: "8",
        0b011: "10",
        0b100: "12",
        0b101: "14",
        0b110: "16",
        0b111: "reserved"
    }

    video_iface_map = {
        0b0000: "Undefined",
        0b0010: "HDMIa",
        0b0011: "HDMIb",
        0b0100: "MDDI",
        0b0101: "DisplayPort"
    }

    # Video white and sync levels, relative to blank.
    vid_sync_map = {
        0b00: "+0.7 / -0.3 V",
        0b01: "+0.714 / -0.286 V",
        0b10: "+1.0 / -0.4 V",
        0b11: "+0.7 / 0 V"
    }

    def __init__( self, input_params = 0 ):

        super( VideoInputParameters, self ).__init__( "Video Input Parameters", 0, 1 )
        self.input_type = None
        self.bit_depth = None
        self.video_interface = None
        self.set_params( input_params )

    def set_bytes( self, byte_array ):

        self.validate_byte_array( byte_array )
        self.set_params( byte_array[0] )

    def set_params( self, params ):

        if None == params:
            self.clear()
        elif self.is_digital( params ):
            self.set_digital_params( params )
        else:
            self.set_analog_params( params )

    def is_digital( self, param ):
        return ( param & 0b10000000 ) >> 7 == 1

    def is_analog( self, param ):
        return ( param & 0b10000000 ) == 0

    def set_digital_params( self, params ):

        if self.is_analog( params ):
            raise ValueError( "Invalid param value {}.".format( bin( params ) ) )

        self.input_type = "Digital"
        self.bit_depth = ( params & 0b01110000 ) >> 4
        self.video_interface = ( params & 0b00001111 )
        self.bytes = [ params ]

    def set_digital_params_from_vals( self, bit_depth, video_interface ):
        
        self.bytes[0] = 0b10000000 | ( bit_depth << 4 ) | ( video_inteface & 0b00001111 )
        self.set_digital_params( self, self.bytes[0] )

    def set_analog_params( self, params ):

        if self.is_digital( params ):
            raise ValueError( "Invalid param value {}.".format( bin( params ) ) )

        self.input_type = "Analog"
        self.video_sync = ( params & 0b01100000 ) >> 5
        self.blank_to_black_setup = ( params & 0b00010000 ) >> 4
        self.separate_sync_supported = ( params & 0b00001000 ) >> 3
        self.composite_sync_supported = ( params & 0b00000100 ) >> 2
        self.sync_on_green_supported = ( params & 0b00000010 ) >> 1
        self.vsync_pulse_must_be_serrated_on_composite_or_green = ( params & 0b00000001 )
        self.bytes = [ params ]

    def set_analog_params_from_vals( self, video_sync, blank_to_black_setup, separate_sync_supported,
                                     composite_sync_supported, sync_on_green_supported,
                                     vsync_pulse_must_be_serrated_on_composite_or_green ):
        self.bytes[0] = ( video_sync & 0x03 ) << 5 | \
                        ( blank_to_black_setup & 1 ) << 4 | \
                        ( separate_sync_supported & 1 ) << 3 | \
                        ( composite_sync_supported & 1 ) << 2 | \
                        ( sync_on_green_supported & 1 ) << 1 | \
                        ( vsync_pulse_must_be_serrated_on_composite_or_green & 1 )
        
        
    def clear( self ):

        self.clear_bytes()
        self.input_type = None
        self.bit_depth = None
        self.video_interface = None
        self.video_sync = None
        self.blank_to_black_setup = None
        self.separate_sync_supported = None
        self.composite_sync_supported = None
        self.sync_on_green_supported = None
        self.vsync_pulse_must_be_serrated_on_composite_or_green = None

    def human_readable( self, indent = 0 ):

        if "Analog" == self.input_type:
            return "Input type: Analog, VideoSync: {}, BlankToBlack: {}; SeparateSyncSupported: {}; CompositeSyncSupported: {}; SyncOnGreenSupported: {}; VsyncPulseMustBeSerratedOnCompositeOrGreen: {}".format(
              self.vid_sync_map.get( self.video_sync ),
              self.blank_to_black_setup,
              self.separate_sync_supported,
              self.composite_sync_supported,
              self.sync_on_green_supported,
              self.vsync_pulse_must_be_serrated_on_composite_or_green
            )
        elif "Digital" == self.input_type:
            return "InputType: {}; BitDepth: {}; VideoInterface: {}".format(
              self.input_type,
              self.bit_depth_map.get( self.bit_depth ),
              self.video_iface_map.get( self.video_interface )
            )
        else:
            return "Undefined"
 
