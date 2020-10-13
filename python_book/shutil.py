"""shutil - содержит функцииб позволяющие копировать, перемещать, переименовывать и удалять файлы"""

shutil.copy('C:\\spam.txt', 'C:\\python') #Копирует файлы
shutil.copytree('C:\\folder', 'C:\\folder_copy') #Копирует папку со всем содержимым

shutil.move('C:\\spam.txt', 'C:\\python') # Перемещать в папку
shutil.move('C:\\spam.txt', 'C:\\python\\spam_new.txt') #Переместить в папку с новым названием

os.unlink('C:\\spam.txt') #Удаляет файл
os.rmdir('C:\\folder')  #Удаляет пустую папку
shutil.rmtree('C:\\folder') #Удаляет папку всместе с содержимым


