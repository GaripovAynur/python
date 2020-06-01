cities = ['New York', 'Moskow', 'new dehli']

print(cities)
print(len(cities)) #Количество

print(cities[0]) #Показать первый город
print(cities[-2]) # Показать сзади второй город
print(cities[2].upper()) #Все заглавные буквы

cities[2]='Tula' # Заменить второй город
print(cities)

cities.append('Kursk') #добавить город с конца
cities.append('Yalta') #Добавить город с конца
print(cities)

cities.insert(2, 'Kazan') #Добавить город 3им.
print(cities)

del cities[-1] #Удалить город с конца
print(cities)

cities.remove('Moskow') #Удалить конкретный город
print(cities)

deleted_city = cities.pop()   #Удаляет последний город
print("Deleted " + deleted_city)

cities.sort() # Отсортировать по алфавиту
print(cities)

cities.sort(reverse=True)  #Отсортировать наоборот или cities.reverse()
print(cities)