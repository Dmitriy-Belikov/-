import random

while 1 == 1:
    print('Для завершения напиши выход')

    human = input('Введи камень, ножницы или бумага: ')
    human = human.lower()
    comp = random.choice(['камень', 'ножницы', 'бумага'])
    print('Компьютер ставит ' + comp)
    if human == comp:
        print('Ничья :)')

    elif human == 'камень' and comp == 'ножницы':
        print('Поздравляю с победой!')

    elif human == 'ножницы' and comp == 'бумага':
        print('Поздравляю с победой!')

    elif human == 'бумага' and comp == 'камень':
        print('Поздравляю с победой!')
    elif human == 'выход':
        break

    else:
        print('Вы проиграли')
