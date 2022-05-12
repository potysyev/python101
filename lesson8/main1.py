class Date:
    def __init__(self, date):
        if isinstance(date, str):
            if date.count("-") == 2:
                self.date = date
            else:
                raise ValueError("Date format is incorrect! 'day-month-year' is expected")

    @classmethod
    def convert(cls, date_str):
        day, month, year = date_str.split('-')
        return int(day), int(month), int(year)

    @staticmethod
    def checkvalidity(date_tpl):
        if (0 < date_tpl[0] <= 31) and (0 < date_tpl[1] <= 12) and len(str(date_tpl[2])) <= 4:
            return True
        else:
            return False


if __name__ == "__main__":
    date1 = Date("01-03-1985")
    date2 = Date("12-31-2022")

    print(date1.checkvalidity(Date.convert(date1.date)))
    print(date2.checkvalidity(Date.convert(date2.date)))
