# объявляем переменные хранязие сумму чисел, сумма цифр которых делится на 7 без остатка и последовательности
power_list = []
total_summ_numbers = 0
total_summ_numbers_increment = 0
# составляем список чисел от 1 до 1000 в 3 степени
for number in range(1, 1001):
    if number % 2 != 0:     # если число делится на 2 с остатком, тогда добавляем в список число в 3 степени
        power_list.append(number ** 3)
print('Список нечетных чисел от 1 до 1000, каждое из которых возведено в 3 степень: ', power_list)

# суммируем числа которые в сумме цифр делятся на 7 без остатка
for power_number in power_list:
    sum_digits = 0
    str_number = str(power_number) # из числа делаем строку
    for digit in str_number:  # идем по цифрам числа для подсчета суммы цифр числа
        sum_digits += int(digit)
    if sum_digits % 7 == 0: #  если сумма цифр числа делится на 7, то суммируем
        total_summ_numbers += power_number

print('Сумма чисел, делящихся суммой цифр на 7 без остатка:', total_summ_numbers)

# инкрементируем каждое число списка на 17 Задание с плюсиком
print("")
print('--------------Задание со звездочкой---------------')
for i in range(len(power_list)):
    power_list[i] += 17
print('Список нечетных чисел от 1 до 1000, каждое из которых возведено в 3 степень (+17): ', power_list)

for power_number in power_list:                             # берем число из списка
    sum_digits = 0
    sum_digits += power_number % 10                          # в сумму цифр числа сразу добавляем остаток от деления на 10
    #print('number: ', power_number, 'sum_digits: ', sum_digits)
    digit_count = 0                                         # вводим переменную считающую степень 10
    power_number_count = power_number                       # вводим переменную для расчета числа степеней 10 исходного числа
    power_number_sub = power_number                         # создаем переменную для вычитания исходного числа
    while power_number_count // 10 != 0:                    # пока переменная делится на 10 на цело и не равна 0
        power_number_count = power_number_count // 10       # делим ее на 10 целочисленно
        digit_count += 1                                    # инкрементируем переменную количества степеней исходного числа

    for digit in range(digit_count, 0, -1):                 # для каждой степени числа 10 из счетчика степеней
        digit_of_number = power_number_sub // 10 ** digit   # определяем очередную цифру числа путем деления на 10 в степени счетчика степеней числа
        sum_digits += digit_of_number                       # прибавляем к переменной суммы цифр полученную цифру
        power_number_sub -= digit_of_number * 10 ** digit   # вычитаем из копии переменной исходного числа цифру умноженную на степень числа 10
    if sum_digits % 7 == 0:  # если сумма цифр числа делится на 7, то суммируем
        total_summ_numbers_increment += power_number

print('Сумма инкрементированных чисел, делящихся суммой цифр на 7 без остатка:', total_summ_numbers_increment)