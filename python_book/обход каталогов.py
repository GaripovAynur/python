'''os.walk() - возвращает три значения на каждой итерации цикла:
    1) Строку, содержащую текущее имя папаки;
    2) Список строк, представляющие имена папок, которые содержатся в текущец папке;
    3) Список строк, представляющин имена файлов, которые содержатся в текущец папке;'''

import os

for folderName, subfolders, filenames in os.walk('C:\\Users'):
    print('Текущая папка - ' + folderName)

    for subfolder in subfolders:
        print('ПОДПАПКА папки' + folderName + ':' + subfolder)

    for filename in filenames:
        print('Файл в папке'  + folderName + ':'+ filename)

    print('')


