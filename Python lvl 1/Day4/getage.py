# Обработка исключений 

def getAge():
    ageinput = input('Сколько тебе лет? ')
    age = int(ageinput)
    if age < 0:
        raise ValueError(
            'Возраст должен быть неотрицательным, а не %s' % (
                    age
                ))
    return age

age = None
while age is None:
    try:
        age = getAge()
    except ValueError as e:
        print(e)

