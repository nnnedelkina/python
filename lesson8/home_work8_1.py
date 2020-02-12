class Date:

    def __init__(self, st_date):
        self.date = Date.valid_date(Date.to_number(st_date))

    @classmethod
    def to_number(cls, st_date):
        return list(map(int, st_date.split('-')))

    @staticmethod
    def valid_date(list_date):
        if not 1 <= list_date[0] <= 31:
            raise Exception('вы ввели некорректную дату')
        if not 1 <= list_date[1] <= 12:
            raise Exception('вы ввели некорректный месяц')
        return list_date

try:
    str_date = input('введите дату в формате dd-mm-yyyy: ')
    date = Date(str_date)
    print('.'.join(map(str, date.date)))
except Exception as err:
    print(err)
