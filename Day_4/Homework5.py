﻿"""
Day_4\Homework5.py

По данному натуральному n выведите лесенку из n ступенек, i-я ступень состоит из  i-го количества цифры 1.
Формат входных данных
Вводится натуральное число n.
Формат выходных данных
Выведите ответ на задачу.

"""

a = 1
n = int(input("Введите количество ступенек: "))
while a <= n:
    print(str(1) * a)
    a += 1