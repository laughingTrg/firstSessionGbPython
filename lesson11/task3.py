class IsNumber(Exception):
    def __init__(self, txt):
        self.txt = txt

nums_list = []
print('Программа заполнения списка числами. Для выхода введите слово "stop"')
while True:
    try:
        check_num = input('Введите число для добавления в список или "stop" для выхода: ')
        if not check_num.isdigit():
            raise IsNumber('Вы ввели не число. Попробуйте еще раз.\n')
    except IsNumber as err:
        if check_num == 'stop':
            print('Вы сформировали следующий список чисел: ', nums_list)
            break
        print(err)
    else:
        nums_list.append(int(check_num))
