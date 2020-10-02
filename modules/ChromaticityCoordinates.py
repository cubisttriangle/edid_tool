from modules.EdidChunk import EdidChunk


class ChromaticityCoordinates(EdidChunk):

    def __init__(self):
        super(ChromaticityCoordinates, self).__init__("Chromaticity Coordinates", 25, 10)
