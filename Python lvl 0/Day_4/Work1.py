﻿"""
#Day_4\Work1.py

На входе 3-хзначное число.
На выходе количество в рязрядах сотни, десятки и единицы

Пример:
In: Введите число: 123

Out: 
Сотни: 1
Десятки: 2
Единицы: 3
"""

nnn = int(input('Введите трёхзначное число: '))
print('Сотен:', nnn // 100)
print('Десятков:', nnn % 100 // 10)
print('Единиц:', nnn % 10) 