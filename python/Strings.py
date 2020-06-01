
name = "mr Ivan pupKiN"

print(name.title()) #Заглавную первую букву
print(name.upper()) #Все заглавную
print(name.lower()) #все маленькие буквы

print("Privet stroka nomer1\nPrivet\n\nstroka3") #\n следующая строка
print("Privet stroka nomer1\n\t\t\tPrivet\n\nstroka3") #\t - Tab
print("Privet stroka nomer" + name.lower())

a = "  .  .. fsdfsd ... .."
print(a)
print(a.rstrip()) #Убрать с права пробелы
print(a.lstrip()) #Убарть с лева
print(a.strip()) #С лева и с права убрать пробелы
print(a.strip("." ".")) # Точки убрать с лева и с права.
