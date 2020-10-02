from modules.EdidChunkContainer import EdidChunkContainer
from modules.EdidHeader import EdidHeader
from modules.BasicDisplayParameters import BasicDisplayParameters
from modules.ChromaticityCoordinates import ChromaticityCoordinates
from modules.EstablishedTimingBitmap import EstablishedTimingBitmap
from modules.StandardTimingInfo import StandardTimingInfo
from modules.DetailedTimingDescriptor import DetailedTimingDescriptor

import struct


class Edid(EdidChunkContainer):
    attributes = ['edid_header', 'basic_display_parameters', 'chromaticity_coordinates',
                  'established_timings', 'standard_timing_info', 'detailed_descriptor1',
                  'detailed_descriptor2', 'detailed_descriptor3', 'detailed_descriptor4']

    def __init__(self):
        super(Edid, self).__init__("EDID", 0, 256)
        self.edid_header = EdidHeader()
        self.basic_display_parameters = BasicDisplayParameters()
        self.chromaticity_coordinates = ChromaticityCoordinates()
        self.established_timings = EstablishedTimingBitmap()
        self.standard_timing_info = StandardTimingInfo()
        self.detailed_descriptor1 = DetailedTimingDescriptor(0x36)
        self.detailed_descriptor2 = DetailedTimingDescriptor(0x48)
        self.detailed_descriptor3 = DetailedTimingDescriptor(0x5A)
        self.detailed_descriptor4 = DetailedTimingDescriptor(0x6C)

    def load_from_file(self, file_path):
        with open(file_path, mode='rb') as edid_file:
            contents = edid_file.read()
            if len(contents) == 0:
                raise ValueError("Edid file is empty: '{}'".format(file_path))
            byte_format = "B" * (len(contents) // 1)
            edid_bytes = struct.unpack(byte_format, contents)
            self.set_bytes(edid_bytes)
