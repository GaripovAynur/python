import os
os.path.join('usr', 'bin', 'spam') #в зависимости какая ОС, будет вставлять \\ /
ПРИМЕР:
myFiles = ['account.txt', 'details.csv', 'invite.docx']
for filename in myFiles:
	print(os.path.join('usr', 'bin', filename))
  # вывод: usr\bin\account.txt
          usr\bin\details.csv
          usr\bin\invite.docx


os.getcwd() # Вывод текущего каталога Пример C:\\Python
os.chdir('C:\\book') #Изменение текущего каталога
os.makedirs('C:\\walnut\\waffles') #Создает папку, в т.ч. промежуточные

os.path.abspath(path)	#Возвращает абсолютный путь. os.path.abspath('.')  вывод: 'C:\\Python'
os.path.isabs(path)	#Возвращает значение True, если аргумент - абсолютный путь, и False, если аргумент - относительный путь.
os.path.relpath(path, start) #Возвращает строку относительного пути от start к path. Если путь start не предоставлен, то в качестве 
			      него используется текущий рабочий каталог


>>> path = 'C:\\Windows\\System32\\calc.exe'
>>> os.path.basename(path) #файл
#вывод: 'calc.exe'
>>> os.path.dirname(path)
#вывод: 'C:\\Windows\\System32' #путь до файла

>>>calcFilePath = 'C:\\Windows\\System32\\calc.exe'
>>>os.path.split(calcFilePath)
#('C:\\Windows\\System32', 'calc.exe') путь к папке, файл
###тоже самое### 
os.path.basename(calcFilePath) #('C:\\Windows\\System32', 'calc.exe')

os.path.getsize('C:\\Windows\\System32\\calc.exe') # Определяет размер файла в байтах 776192
os.listdir('C:\\Windows\\System32') # все файлы в папке '123.txt', 'aaclient.dll' ...

РАЗМЕР ВСЕХ ФАЙЛОВ в папке
totalSize = 0
for filename in os.listdir('C:\\Windows\\System32')
	totalSize = totalSize +
	os.path.getsize(os.path.join('C:\\Windows\\System32', filename)
print(totalSize) # 1117846456 байт

os.path.exists('C:\\Windows')	# Существует путь к папке или файл  True
os.path.isdir('C:\\Windows')	# True если это каталог есть, и false если это файл.
os.path.isfile('C:\\Windows')   # True если это файл есть, и false если это каталог.
"""shutil - содержит функцииб позволяющие копировать, перемещать, переименовывать и удалять файлы"""

shutil.copy('C:\\spam.txt', 'C:\\python') #Копирует файлы
shutil.copytree('C:\\folder', 'C:\\folder_copy') #Копирует папку со всем содержимым

shutil.move('C:\\spam.txt', 'C:\\python') # Перемещать в папку
shutil.move('C:\\spam.txt', 'C:\\python\\spam_new.txt') #Переместить в папку с новым названием

os.unlink('C:\\spam.txt') #Удаляет файл
os.rmdir('C:\\folder')  #Удаляет пустую папку
shutil.rmtree('C:\\folder') #Удаляет папку всместе с содержимым, без возвратно

import send2trash #Безопасное удаление
send2trash.send2trash('C:\\folder') #Безопасное удаление


