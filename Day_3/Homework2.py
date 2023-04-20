﻿#Day_3\Homework2.py
""" 
Задача 2. Коровы 
По данному числу n закончите фразу «На лугу пасется...» одним из возможных продолжений: 
«n коров», «n корова», «n коровы», правильно склоняя слово «корова».

Формат входных данных
Дано число n (0 <= n <= 200).

Формат выходных данных
Программа должна вывести введенное число n и одно из слов (на латинице): 
коров, корова или коровы, например, 1 корова, 2 коровы, 5 коров, 125 коров.
 
Входные данные / Выходные данные
1	           На лугу пасется 1 корова
33	           На лугу пасется 33 коровы
"""

cows = int(input('Введите число коров: '))
if cows > 200:
	print ("Выход за диапозон 0 - 200")

else: 
	if 11 <= cows % 100 <= 19:
			print('На лугу пасется', cows, 'коров.')
	else:
		units = cows % 10
		if units == 1:
				print('На лугу пасется', cows%10, 'корова.')
		elif 2 <= units <= 4:
				print('На лугу пасется', cows, 'коровы.')
		else:
				print('На лугу пасется', cows, 'коров.')