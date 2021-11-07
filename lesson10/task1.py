class Matrix:                                                           # базовый класс матрицы
    def __init__(self, list_matrix):
        self._matrix = list_matrix                                      # аттрибут матрицы

    def __str__(self):                                                  # определяем метод стр выводим матрицу в консоль
        for el in self._matrix:
            print('|', *el, '|')
        return ''

    def __add__(self, add_matrix):                                      # определяем метод сложения передаем другой экземпляр класса матрица
        result = []
        for list_1, list_2 in zip(self._matrix, add_matrix._matrix):    # проходим по строкам матрицы
            result_list = []
            for num_1, num_2 in zip(list_1, list_2):                    # получаем элементы строки и складываем
                result_list.append(num_1 + num_2)
            result.append(result_list)
        return Matrix(result)                                           # позвращаем матрицу с полученными результатами

mx_3x2 = Matrix([[31, 22], [37, 43], [51, 86]])                         # проверяем работу скрипта
mx_3x3 = Matrix([[3, 5, 32], [2,4,6], [-1, 64, -8]])
mx_2x4 = Matrix([[3, 5, 8, 3], [8, 3, 7, 1]])
mx_2x4_add = Matrix([[3, 5, 8, 3], [8, 3, 7, 1]])
print(mx_3x2)
print(mx_3x3)
print(mx_2x4)
print(mx_2x4 + mx_2x4_add)

