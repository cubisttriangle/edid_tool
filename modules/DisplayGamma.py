from modules.EdidChunk import EdidChunk


class DisplayGamma(EdidChunk):

    def __init__(self, gamma=None):

        super(DisplayGamma, self).__init__("Display Gamma", 3, 1)
        self.gamma_to_param(gamma)

    def param_to_gamma(self, param):

        return (param + 100.0) / 100.0

    def gamma_to_param(self, param):

        if None == param:
            self.clear_bytes()
        else:
            self.bytes[0] = (param * 100) - 100

    def gamma_is_valid(self):

        gamma = self.param_to_gamma(self.bytes[0])

        return gamma >= 1.0 and gamma <= 3.54

    def human_readable(self, indent_no=0):

        return "{}".format(self.param_to_gamma(self.bytes[0]))
