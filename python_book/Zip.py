import zipfile 

examleZip= zipfile.ZipFile('example.zip') # Открывает zip
examleZip.namelist() # показывает содержимое

spamINfo = examleZip.getinfo ('spam.txt')
spamINfo.file_size #размер файла без сжатья
spamINfo.compress_size #размер после сжатья

spamINfo.extractall() #извлечь все
spamINfo.extracе('spam.txt') #извлечь конкретный файл

newZip = zipfile.ZipFile('new.zip', 'w') #создать новый zip
newZip.write('spam.txt', compress_type=zipfile.ZIP_DEFLATED) # сжать
newZip.close() #закрыть

#ПРИМЕР
#Для записи всех файлов в директории можно воспользоваться функцией os.walk:
import zipfile
import os

z = zipfile.ZipFile('spam.zip', 'w')        # Создание нового архива
for root, dirs, files in os.walk('folder'): # Список всех файлов и папок в директории folder
for file in files:
   z.write(os.path.join(root,file))         # Создание относительных путей и запись файлов в архив
z.close()                                   # Закрытие архива
