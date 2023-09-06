firstPlayer, secondPlayer = input('Ввод: ').split(' ')

if firstPlayer == 'камень':
    if secondPlayer == 'бумага':
         result = 'игрок 2 выиграл'
    elif secondPlayer == 'ножницы':
        result = 'игрок 1 выиграл'
    else:
        result = 'ничья'
elif firstPlayer == 'бумага':
    if secondPlayer == 'ножницы':
        result = 'игрок 2 выиграл'
    elif secondPlayer == 'камень':
        result = 'игрок 1 выиграл'
    else:
        result = 'ничья'
elif firstPlayer == 'ножницы':
    if secondPlayer == 'камень':
        result = 'игрок 2 выиграл'
    elif secondPlayer == 'бумага':
        result = 'игрок 1 выиграл'
    else:
        result = 'ничья'
else:
    result = 'Некорректный ввод'

print('Вывод:', result)