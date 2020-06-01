


enemy = {
    # key    volume
    'loc_x': 70,
    'loc_y': 50,
    'color': 'gren',
    'health': 100,
    'name': 'Mudillo',
}

print(enemy)
print("location X" + "  " + str(enemy['loc_x']))
print("location Y" + "  " + str(enemy['loc_y']))

a = (enemy['health']) - 70
print(a)
enemy['rank'] = 'Admiral'   # Добавить в словари новую переменную
print(enemy)

del enemy['rank'] # Удалить переменную
print(enemy)

if a < 100:                         #Если падает уровень здоровья, то цвет меняется на желтый.

    b = enemy['color']='yellow'
    print(b)
