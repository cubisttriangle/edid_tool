from modules.EdidChunk import EdidChunk


class Version(EdidChunk):

    def __init__(self):
        super(Version, self).__init__("Version", 18, 2)

    def human_readable(self, indent=0):
        version = self.bytes[0]
        revision = self.bytes[1]

        return "EDID v{}.{}".format(version, revision)
