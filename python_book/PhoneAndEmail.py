"""Пример регулярного выражения
Создание регулярного выражения для поиска телефонных номеров
pyperclip - данный модуль предназначен для работы с текстовыми данными. То есть если мы скопируем в буфер обмена
какой то файл и попытаемся извлечь его с помощью pyperclip, в этом случаем будет возвращена пустая строка."""

import re, pyperclip

# Для телефонных номеров
phoneRegex = re.compile(r''' (
(\d{3}|\(\d{3}\))?
(\s|-|\.)?
(\d{3})
(\s|-|\.)
(\d{4})
(\s* (ext|x|ext.) \s* (\d{2,5}))?
) ''', re.VERBOSE)

""" re.VERBOSE - игнорируются пробелы и комментарии в строке
    re.IGNORECASE - игнорировать регистры
    re.DOTALL - По умолчанию символ \n конца строки не подходит под точку.
    С этим флагом точка — вообще любой символ """

# e-mail
emailRegex = re.compile(r'''(
[a-zA-Z0-9._%+-]+ #имя пользователя
@
[a-zA-Z0-9.-]+ #имя домена
(\.[a-zA-Z]{2,4})
)''', re.VERBOSE)

# поиск соотвествия в текстк, содержащемся в буфере обмена.
text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

# Копирование результатов в буфео обмена.
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Скопирован в буфео обмена:')
    print('\n'.join(matches))
else:
    print('Телефонные номера и почты не обнаружены')
