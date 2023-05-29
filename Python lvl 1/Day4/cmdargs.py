#Обработка параметров командной строки

import os
import random

# Тест по арифметике:
#    получить сложность. Это может быть количество знаков в числах,
#    номер сложности в вашем словаре допустимых математических
#    операций (+, +-, +-*...), количество заданий или количество верных
#    ответов "проходного балла"


def genExample(difficulty):
    a = random.randint(0,9)
    b = random.randint(1,9)
    sign = random.choice(
        '+-*/'[:(difficulty+1)]
    )
    if sign == '/':
        c = a * b
        a, c = c, a
        answer = c
    question = str(a) + sign + str(b)
    answer = int(eval(question))
    return question, answer


# Предположим, мы ожидаем записи diffuculty=N
difficulty = 4
for arg in os.sys.argv:
    if arg.startswith('difficulty='):
        N = arg.split('difficulty=')[1]
        if N.isdigit():
            N = int(N)
            if N in range(4):
                difficulty = N
                print('new difficulty', difficulty)

                
print(genExample(difficulty))
# ВСЕ ЭТО СДЕЛАНО в предположении, что программа поддерживает
# 5 уровней сложности:
# 0 - только сложение
# 1 +-
# 2 +-*
# 3 +-*/
# 4 - без ограничений






    
