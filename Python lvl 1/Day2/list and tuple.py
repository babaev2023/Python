# Кортеж (tuple) и список (list)

pustoi_spisok = []
spisok_slov   = ["один", 'два', 'три']
spisok_chisel = [1, 2, 3, 4, 5, 6, 7, 9]
spisok_svalka = [0, None, True, [], 'False', 25.7]

empty_tuple = ()
tuple_of_strings = ('a1', 'a2')
tuple_of_floats = (1.2, 3.4, 5.6, 7.8, 9e+1)
tuple_of_everything = ([0], (), None, False)

# Список и кортеж могут содержать любые объекты
# К существующим элементам списка можно обращаться
# на чтение и запись по положительным и отрицательным индексам

print('Pervoe slovo:', spisok_slov[0])  # обращение на чтение
spisok_slov[2] = 'четыре'  # присваивание - обращение на запись
print(spisok_slov)

# Строку по индексу изменить нельзя, кортеж - почти нельзя
# можно так
tuple_of_everything[0][0] = 66
print(tuple_of_everything)

# списки - это ссылки на списки ссылок

b = 6
vlist = [b, b, b, b+1, b, b]
new_list = vlist
new_list[0] = 9
print(vlist)
print(new_list)

print("Добавить в список - append")

spisok_slov.append('пять')
print(spisok_slov)

print("убрать из списка (del)")
# 1. del
print(spisok_chisel)
del spisok_chisel[0]
print(spisok_chisel)

# 2. pop - убрать и "вытащить"
last = spisok_chisel.pop()
print("Pop last:", last)
pop2 = spisok_chisel.pop(2)
print('Pop selected:', pop2)
print(spisok_chisel)

# 3. remove - по значению
spisok_chisel.remove(5)
print('5 was removed: ', spisok_chisel)



# создадим список с помощью генератора-выражения
natural_less_10 = [i for i in range(1, 10)]
print(natural_less_10)
# Из списка можно сделать нарезку (втч в обратном порядке)
# mylist[ОТКУДА_ВКЛЮЧИТЕЛЬНО:]  # начиная с
# mylist[:доКУДА_исКЛЮЧИТЕЛЬНО]  # не включая окончание
# mylist[C:ПО]  # не включая окончание
# mylist[C:ПО:ШАГ]  # не включая окончание
# любое может быть пропущено или стоять None

print(natural_less_10[10::-2])

nl = natural_less_10[::]  # [:]
# поверхностное копирование - только "первый этаж"
nl[0] = 1000
print(nl)
print(natural_less_10)


















