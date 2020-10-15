helloFile = open(r'C:\Users\a.garipov\PycharmProjects\untitled2\1.txt') #открыть файл
readfile = helloFile.read() # Прочитать содержимое файла
readfile = helloFile.readlines() #тоже самое что read, но все строчки в одной линии

helloFile = open(r'C:\Users\a.garipov\PycharmProjects\untitled2\1.txt', 'w') #открыть файл в режиме перезаписи
Пример: helloFile.write('Dobavit znachenie') # кол-во символов 25

helloFile = open(r'C:\Users\a.garipov\PycharmProjects\untitled2\1.txt', 'a') #открыть файл в режиме добавления
Пример: helloFile.write('Dobavit znachenie') # кол-во символов 125

helloFile.close() #закрыть файл


import shelve #сохранять переменные в двоичных файлах-храналищах.
shelfFile = shelve.open('mydata')
cats = ['Zophie', 'Pooka', 'Simon']
shelfFile['cats'] = cats
shelfFile.close() # Создается три файла mydata.bak, mydata.dat, mydata.dir




