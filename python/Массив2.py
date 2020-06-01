

#         0      1      2       3       4
cars = ['bmw', 'vw', 'seat', 'skoda', 'lada']

for x in cars:
    print(x)
    print(x.upper())  # Распечатать все буквы заглавные

for x in range(1, 6): #Цикл от 1 до 5
    print(x)

mynumber_list = list(range(0, 10))
print(mynumber_list)                #Вывести все значения в один ряд
print("=========================================")

for x in mynumber_list:
    x = x * 2
    print(x)

mynumber_list.sort(reverse=True)   # Сортировка наоборот
print(mynumber_list)

print("Max number is:" + str(max(mynumber_list))) #Макс значение
print("Min number is:" + str(min(mynumber_list))) #Мин значение
print("Sum number is:" + str(sum(mynumber_list))) #Сумма

print("=========================================")

#         0      1      2       3       4
cars = ['bmw', 'vw', 'seat', 'skoda', 'lada']

mycars = cars[1:4]   # Значение 1 между 4
print(mycars)
mycars = cars[:4]   # Значние до 4
print(mycars)

mycars = cars [-4:-1] # Значение 1 между 4
print(mycars)

mycars = cars [:] #Копирует массив, предедущий массив не будет изменятся