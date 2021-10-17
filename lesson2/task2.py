origin_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
res_list = []                                                       # создаем лист для вывода результата

for item in origin_list:                                            # проходим по всем элементам исходного списка и проверяем не число ли оно
    if item.isdigit():
        if len(item) < 2:
            res_list.append('"')                                    # если длина числа меньше 2, значит рисуем 0 впереди данного числа
            res_list.append('0' + item)                             # и добавляем число и кавычки в выходной список
            res_list.append('"')
        else:                                                       # если длина числа больше 2, значит 0 впереди рисовать не надо
            res_list.append('"')                                    # добавляем в выходной список элемент и кавычки
            res_list.append(item)
            res_list.append('"')
    elif item[0] == '+' or item[0] == '-':                          # иначе если первым символом элемента является знак + или -
        if len(item) == 2:                                          # если число с одной цифрой и знаком, добавляем между знаком и числом 0
            res_list.append('"')
            res_list.append(item[0] + '0' + item[1])
            res_list.append('"')
        else:                                                       # иначе просто выводим данный элемент и кавычки
            res_list.append('"')
            res_list.append(item)
            res_list.append('"')
    else:
        res_list.append(item)                                       # если это не число и не число со знаком просто добавляем в выходной список

print(res_list)                                                     # выводим полученный выходной список
next_digit = 0                                                      # для корректного вывода строки задаем переменную определяющую, что
for element in res_list:                                            # следующий элемент после кавычек число или число со знаком
    if element == '"' and next_digit == 0:                          # проходим по списку если встречаем кавычки и переменная равна 0
        next_digit = 1                                              # присваиваем переменной 1 и делаем вывод кавычек без пробелов в конце строки
        print(element, end='')
    elif next_digit == 1 and element == '"':                        # если у нас переменная 1 и снова кавычки, присваиваем переменной 0
        next_digit = 0                                              # и выводим кавычки с пробелом в конце
        print(element, end=' ')
    elif next_digit == 1:                                           # если просто переменная равна 1, значит на входе число - выводим его без пробелов
        print(element, end='')
    else:
        print(element, end=' ')                                     # в остальных случаях у нас текст, просто выводим



