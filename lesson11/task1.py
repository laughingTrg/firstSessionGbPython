class Date:
    def __init__(self, input_date):
        print('Data class')
        self.input_date = input_date
        print('You send date:', input_date)

    @classmethod
    def exclude_date(cls, input_date):                                  # получаем список число, месяц, год
        date = input_date.split('-')
        for i in range(len(date)):
            date[i] = int(date[i])                                      # получаем список чисел даты
        return date

    @staticmethod
    def validate_date(input_date):
        valid_date = [31, 12, 9999]                                     # определяем валидную дату
        check_date = Date.exclude_date(input_date)                      # получаем список чисел даты
        for i in range(len(check_date) - 1):                            # проверяем соотвествие чисел в дате
            if check_date[i] > valid_date[i] or check_date[i] < 0 or check_date[-1] < 0: # при отрицательных или неправлиьных числах выводим ошибку
                raise ValueError('Invalid date')
        return print(f'Date {input_date} is valid')                     # выводим что дата валидная

date_start = Date('09-10-2021')                                         # проверяем работу скрипта
date_classmethod = Date.exclude_date('09-11-2021')
print('Call classmethod instantly:', date_classmethod)
print('Call classmethod from object:', date_start.exclude_date('09-10-2021'))

Date.validate_date('09-11-2021')

date_start.validate_date('23-31-2099')