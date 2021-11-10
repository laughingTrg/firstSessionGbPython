tutors = [                                                                              # создаем список учеников
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]

tutors_long = [                                                                         # создаем длинный список учеников
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', 'Mike', 'Dan','Tim'
]

klasses = [                                                                             # создаем список классов
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]

def gen_tutor_klass(tutors, klasses):                                                   # функция принимает списки учеников и классов
    idx = 1                                                                             # переменная для итерации вывода результата
    if len(tutors) > len(klasses):                                                      # если длина списка учеников больше длины списка классов
        for i in range(len(tutors) - len(klasses) + 1):                                 # то выравниваем длину списка классов заполняя None
            klasses.append(None)
    tutor_klass = ((name, grade) for name, grade in zip(tutors, klasses))               # создаем генератор кортежей(кченик, класс) из списков
    while idx <= len(tutors):                                                           # выводим значение генератора
        print(next(tutor_klass))                                                        # пока не закончилась длина списка учеников
        idx += 1

gen_tutor_klass(tutors, klasses)                                                        # проверяем, как работает короткий список учеников
print('-------------------------')
gen_tutor_klass(tutors_long, klasses)                                                   # проверяем, как работает длинный список учеников
print('-------------------------')
def check_gen():                                                                        # функция показывает, что создан генератор, и истощает его
    tutor_klass = ((name, grade) for name, grade in zip(tutors, klasses))
    print(tutor_klass)                                                                  # выводим информацию о генераторе
    while True:
        print(next(tutor_klass))                                                        # выводим значения генератора пока не получим ошибку StopIteration
check_gen()
