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
