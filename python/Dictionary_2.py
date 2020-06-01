


enemy = {
    # key    volume
    'loc_x': 70,
    'loc_y': 50,
    'color': 'gren',
    'health': 100,
    'name': 'Mudillo',
}

all_enemys = []          #Просто пустое значение
print(all_enemys)

for xxx in range(0, 10):
    all_enemys.append(enemy.copy()) #append(enemy) добавить значение enemy
    print(all_enemys)

print("-----------------------------------")

for xxx in all_enemys:
    print(xxx)
print("##################################################")
all_enemys[5]['health'] = 70 #Меняет значение на 5 цикле, 6 значение будет 70.
all_enemys[8]['name'] = "COW"
all_enemys[2]['loc_x'] += 9
for yyy in all_enemys:  #Разбить по строчкам
    print(yyy)