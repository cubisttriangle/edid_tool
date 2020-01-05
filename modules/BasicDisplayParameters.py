from modules.EdidChunkContainer import EdidChunkContainer
from modules.VideoInputParameters import VideoInputParameters
from modules.ScreenSize import ScreenSize
from modules.DisplayGamma import DisplayGamma
from modules.DisplaySupportedFeatures import DisplaySupportedFeatures

class BasicDisplayParameters( EdidChunkContainer ):

    attributes = [ "video_input_parameters", "screen_size", "gamma",
                   "supported_features" ]

    def __init__( self ):

        super( BasicDisplayParameters, self ).__init__( "Basic Display Parameters", 20, 5 )
        self.video_input_parameters = VideoInputParameters()
        self.screen_size = ScreenSize()
        self.gamma = DisplayGamma()
        self.supported_features = DisplaySupportedFeatures()
