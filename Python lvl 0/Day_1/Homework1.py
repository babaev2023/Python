﻿#Day_1\Homeworks1.py
# Без ввода данных - вариант 1
# print("Прямоугольник со сторонами a и b")
# a = 35
# b = 10
# print("Сторона a", a)
# print("Сторона b", b)
# P=2*(a+b)
# S=a*b 
# print("Периметр прямоугольника", P)
# print("Площадь прямоугольника", S)

# Вариант 2
print("Прямоугольник со сторонами a и b")
a = input('Введите высоту прямоугольника: ')
b = input('Введите длину прямоугольника: ')

# Меняем тип переменной с str на int, с помощью функции int()
a_as_number = int(a)
b_as_number = int(b)

P=2*(a_as_number+b_as_number)
S=a_as_number*b_as_number 
print("Периметр прямоугольника", P)
print("Площадь прямоугольника", S)