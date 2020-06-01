
inputfile = "../users_name.txt"   #Сканировать файл на директорию выше. Можно написать полный путь

myfile = open(inputfile, mode='r', encoding='latin_1')  #Определяем параметры, кодировку

for num, line in enumerate (myfile, 1): # num -  по порядку нумерует. Line - каждая строка, 1 - отчет начинать с 1
    if "Carline" in line:               # Найти совподение с Карлина
        print("Line #: " + str(num) + " : " + line.strip())


 #"""Проверка паролей"""


inputfile = "../password.txt"   #Сканировать файл на директорию выше. Можно написать полный путь
outputfile = "../match.txt"

password_tolookfor = "vasya"

myfile1 = open(inputfile, mode='r', encoding='latin_1')  #Определяем параметры, кодировку
myfile2 = open(outputfile, mode='w', encoding='latin_1')  # Записываем, если хочем >> то тогда вместо w ставить a (append)

for num, line in enumerate (myfile1, 1): # num -  по порядку нумерует. Line - каждая строка, 1 - отчет начинать с 1
    if password_tolookfor in line:               # Найти совподение с Карлина
        print("Line #: " + str(num) + " : " + line.strip())
        myfile2.write("Found password" + line)  #Записывает все данные прошедшие через if
myfile1.close()  # закрыть блокнот
myfile2.close()