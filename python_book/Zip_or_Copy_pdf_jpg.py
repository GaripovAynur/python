"""ZIPовать C:\\Users все jpg|pdf файлы
   или shutil.copy копировать все в одну папку"""


import os, zipfile, re, shutil
os.chdir('C:\\book')
pdf = re.compile(r'(\w)+(\.)(jpg|pdf)')
z = zipfile.ZipFile('spam.zip', 'w')
count = 1
for foldername, subfolder, filename in os.walk('C:\\Users'): # Папака для поиска
    for mo in filename:                                      # Файлы ввидк списка
        mo1 = pdf.search(mo)                                 # Вытаскиваем каждый файл из списка
        if None != mo1:
            mo2 = foldername + '\\' + mo1.group()
            count = count + 1
            print(count, mo2)

            try:                              # пропустить ошибки при итерации
                #shutil.copy(mo2, 'C:\\book')  # Копирует файлы
                z.write(os.path.join(mo2)) #копирует файлы, сохраняя весь путь как в оригинале
            except FileNotFoundError:
                print('поймал ошибку')        # Вывести ошибку

z.close()
