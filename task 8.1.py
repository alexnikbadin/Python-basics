class Data:

    def __init__(self, date):
        self.date = date

    @classmethod
    def get_number(cls, date):
        date = [int(x) for x in date.split('-')]
        print(list(map(int, date)))
        print(type(date[0]))

    @staticmethod
    def valid_number(date):
        date = [int(x) for x in date.split('-')]
        list(map(int, date))
        if date[0] > 31 or date[1] > 12 or 2021 < date[2] < 1900:
            print('Wrong date')
        else:
            print('Valid date')



Data.get_number(input('Enter a date : '))
Data.valid_number(input('Enter a date : '))
