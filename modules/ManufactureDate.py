from modules.EdidChunk import EdidChunk


class ManufactureDate(EdidChunk):
    week_max = 53
    model_year_flag = 0xFF
    year_offset = 1990

    def __init__(self):

        super(ManufactureDate, self).__init__("Manufacturer Date", 16, 2)

    def set_date(self, week, year):

        if None == week or None == year:
            raise ValueError("Week / year may not be None.")

        if week > self.week_max and week != self.model_year_flag:
            raise ValueError("Week exceeds maximum value of {}, but is not model year flag ({}).".format(self.week_max,
                                                                                                         self.model_year_flag))

        self.bytes[0] = week
        self.bytes[1] = year

    def human_readable(self, indent=0):

        week = self.bytes[0]
        year = self.year_offset + self.bytes[1]

        if 0xFF == week:
            return "Year of model: {}".format(year)
        elif 0 == week:
            return "Year of manufacture: {}".format(year)
        else:
            return "Manufactured on week {} of {}".format(week, year)
