origin_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
index = 0                                                                               # вводим переменнуб индексации по исходному списку

while index != len(origin_list):                                                        # выполняем цикл пока у нас индекс не дошел до конца массива
    if origin_list[index].isdigit():                                                    # если ловим число и его длина меньше 2, присваиваем
        if len(origin_list[index]) < 2:                                                 # элементу по указанному индексу 0 к числу
            origin_list[index] = '0' + origin_list[index]                               # вставляем по указанному индексу кавычки
            origin_list.insert(index, '"')                                              # и по индексу +2 тоже кавычки
            origin_list.insert(index + 2, '"')
            index += 2                                                                  # инкрементируем индекс на 2, чтобы не проходить по вставленным элементам
        else:
            origin_list.insert(index, '"')                                              # если число с 2 и более знаками, просто вставляем кавычки
            origin_list.insert(index + 2, '"')
            index += 2
    elif origin_list[index][0] == '+' or origin_list[index][0] == '-':                  # если встречаем + или - и длина элемента = 2
        if len(origin_list[index]) == 2:
            origin_list[index] = origin_list[index][0] + '0' + origin_list[index][1:]   # присваиваем элементу значение знак + 0 + значение
            origin_list.insert(index, '"')                                              # не забываем добавить кавычки
            origin_list.insert(index + 2, '"')
            index += 2
        else:                                                                           # если длина числа со знаком отличается от 2, то просто добавляем кавычки
            origin_list.insert(index, '"')
            origin_list.insert(index + 2, '"')
    else:                                                                               # если у нас на входе текст, то просто идем дальше
        index += 1

print(origin_list)
next_digit = 0
for element in origin_list:                                                             # вывод строки элементов как в задании 2 :))
    if element == '"' and next_digit == 0:
        next_digit = 1
        print(element, end='')
    elif next_digit == 1 and element == '"':
        next_digit = 0
        print(element, end=' ')
    elif next_digit == 1:
        print(element, end='')
    else:
        print(element, end=' ')