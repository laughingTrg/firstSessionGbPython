class ComplexNumbers:                                                   # комплексные числа
    def __init__(self, value):                                          # задаем само число
        self.value = value
        self.real = ComplexNumbers._get_real(value)                     # определяем действительное число
        self.imaginary = ComplexNumbers._get_imaginary(value)           # определяем мнимое число

    def __str__(self):                                                  # выводим число
        return self.value

    def __add__(self, other):                                           # переопределяем сложение
        other_real = ComplexNumbers._get_real(other.value)              # получаем действительную часть
        other_imaginary = ComplexNumbers._get_imaginary(other.value)    # получаем мнимую часть
        result_real = str(int(self.real) + int(other_real))             # определяем результат сложения реальной и мнимой частей
        result_imaginary = str(int(self.imaginary[:-1]) + int(other_imaginary[:-1])) + 'i'
        if '-' in result_imaginary:                                     # если есть минус в мнимой части
            return ComplexNumbers(result_real + result_imaginary)       # просто выводим 2 строки
        else:
            return ComplexNumbers(result_real+'+'+result_imaginary)     # если + выводим с +

    def __mul__(self, other):                                           # перегружаем перемножение
        other_real = ComplexNumbers._get_real(other.value)
        other_imaginary = ComplexNumbers._get_imaginary(other.value)
        result_real = int(self.real) * int(other_real) - int(self.imaginary[:-1]) * int(other_imaginary[:-1]) # получаем результат реальной части
        result_imaginary = int(self.real) * int(other_imaginary[:-1]) + int(other_real) * int(other_imaginary[:-1]) # получаем мнимую часть
        if '-' in str(result_imaginary):
            return ComplexNumbers(str(result_real) + str(result_imaginary) + 'i')
        else:
            return ComplexNumbers(str(result_real) + '+' + str(result_imaginary) + 'i')

    @staticmethod                                       # использую статикметод, чтобы не предавать селф
    def _get_real(value):
        if '+' in value:                                # если число с +
            real = value.split('+')[0]                  # получаем реальную часть
        else:
            if value.count('-') > 1:                    # если 2 минуса получаем реальную часть
                real = value[:value.rfind('-')]
            else:
                real = value.split('-')[0]
        return real

    @staticmethod
    def _get_imaginary(value):                          # получаем мнимую часть
        if '+' in value:
            real = value.split('+')[-1]
        else:
            real = value[value.rfind('-'):]
        return real

complex_num1 = ComplexNumbers('2+5i')                   # проверяем работу скрипта
complex_num2 = ComplexNumbers('-1+3i')
comp_num4 = ComplexNumbers('-7-19i')
comp_add = complex_num1 + complex_num2 + comp_num4
print(comp_add)
comp_mull = complex_num1 * complex_num2 * comp_num4
print(comp_mull)




