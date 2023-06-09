# Множества и словари

s = {1, 2, 3, 2, 1, 2, 3}
print(s, type(s))
print("=============================")

a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7}
a.difference(b)
{1, 2, 3}
a.intersection(b)
{4, 5}
a.symmetric_difference(b)
{1, 2, 3, 6, 7}
a.union(b)
{1, 2, 3, 4, 5, 6, 7}

#######################################
#
# Словарь
#



voc = {
    'cat': 'кошка',
    1: 'один',
    'speed': 3e+8
}

#from myvoc import voc  # после первой записи в myvoc.py

# доступ на чтение - в квадратных скобках по ключу
print(voc['cat'])

# доступ на запись, в том числе несуществующего элемента
voc[9.8] = 'Ускорение'

print(voc)

print('voc = ', voc)  # > myvoc.py
























