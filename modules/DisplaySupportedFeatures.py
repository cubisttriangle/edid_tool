from modules.EdidChunk import EdidChunk

class DisplaySupportedFeatures( EdidChunk ):

    color_map = {
        0: {
            0b00: "Monochrome or grayscale",
            0b01: "RGB",
            0b10: "Non-RGB",
            0b11: "Undefinded"
        },
        1: {
            0b00: "RGB 4:4:4",
            0b01: "RGB 4:4:4 & YCrCb 4:4:4",
            0b10: "RGB 4:4:4 & YCrCb 4:2:2",
            0b11: "RGB 4:4:4 & YCrCb 4:4:4 & YCrCb 4:2:2"
        }
    }

    def __init__( self, features = None ):

        super( DisplaySupportedFeatures, self ).__init__( "Display Supported Features", 4, 1 )
        self.set_features( features )

    def set_features( self, features ):

        if None == features:
            self.clear_bytes()
        else:
            self.set_bytes( [ features ] )

    def set_param_from_features( self, standby_mode_supported, suspend_mode_supported,
                                 very_low_power_supported, color_encoding, s_rgb_is_default,
                                 preferred_timing_mode_includes_native_format,
                                 display_freq_is_continuous ):
        feat = ( standby_mode_supported & 0xFF ) << 7 | \
               ( suspend_mode_supported & 1 ) << 6 | \
               ( very_low_power_supported & 1 ) << 5 | \
               ( color_encoding & 0b11 ) << 3 | \
               ( s_rgb_is_default & 1 ) << 2 | \
               ( preferred_timing_mode_includes_native_format & 1 ) << 1 | \
               ( display_freq_is_continuous & 1 )

        self.set_bytes( [ feat ] )

    def human_readable( self, indent_no = 0 ):

        feat = self.bytes[0]
        standby_mode_supported = ( feat & 0b10000000 ) >> 7
        suspend_mode_supported = ( feat & 0b1000000 ) >> 6
        very_low_power_supported = ( feat & 0b100000 ) >> 5
        color_mode = ( feat & 0b11000 ) >> 3
        color_encoding = self.color_map[standby_mode_supported].get( color_mode )
        s_rgb_is_default = ( feat & 0b100 ) >> 2
        pref_timing_mode_includes_native_format = ( feat & 0b10 ) >> 1
        display_freq_cont = ( feat & 0b1 )

        indent = indent_no + 1

        stby_str = "Standby mode supported: {}".format( standby_mode_supported )
        stby = "\n{}".format( self.indented( stby_str, indent ) )

        sus_str = "Suspend mode supported: {}".format( suspend_mode_supported )
        sus = "\n{}".format( self.indented( sus_str, indent ) )

        vlp_str = "Very low power mode supported: {}".format( very_low_power_supported )
        vlp = "\n{}".format( self.indented( vlp_str, indent ) )

        col_str = "Color encoding: {}".format( color_encoding )
        col = "\n{}".format( self.indented( col_str, indent ) )

        srgb_str = "sRGB is default color space: {}".format( s_rgb_is_default )
        srgb = "\n{}".format( self.indented( srgb_str, indent ) )

        pref_str = "Preferred timing mode include native pixel format and refrest rate: {}".format( pref_timing_mode_includes_native_format )
        pref = "\n{}".format( self.indented( pref_str, indent ) )

        freq_str = "Display frequency is continuous: {}".format( display_freq_cont )
        freq = "\n{}".format( self.indented( freq_str, indent ) )
        
        return "{}{}{}{}{}{}{}".format( stby, sus, vlp, col, srgb, pref, freq )
