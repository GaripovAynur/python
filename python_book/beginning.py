

#строковые методы
b.title()  #Заглавную первую букву
b.upper() #Все заглавную
b.lower() #все маленькие буквы
b.isupper() #возвращает значение True, если все буквы верхнего регистра
b.islower() #возвращает значение True если все буквы нижнего регистра
b.isalpha()  #возвращает значение True, если строка состоит только из букв и не ял-ся пустой
b.isalnum() #возвращает значение True, если строка состоит только из буквенно-цифровых символов и не яв-ся пустой
b.isdecimal() #возвращает значение True, если строка состоит только из цифровых символов и не яв-ся пустой
b.isspace() #возвращает значение True, если строка состоит только из символов пробела, табуляции, новой строки и не яв-ся пустой
b.istitle() #возвращает значение True, если строка состоит только из слов, которые нач-ся с буквы в верхном регистре , за которой следуют только буквы в нижнем регистре.

'Hello world!'.startswith('Hello') # Возвращает True, т.к. строка начинается с Hello
'Hello world!'.endswith('world') # Возвращает True, т.к. строка заканчивается на world

', '.join(['cats', 'rats', 'bats']) # вывод будет такой: 'cats, rats, bats'
'; '.join(['cats', 'rats', 'bats']) # вывод будет такой: 'cats; rats; bats'
'MyABCnameABCisABCisABCSimon'.split('ABC') # вывод будет такой: ['My', 'name', 'is', 'is', 'Simon']

'hello'.center(20, '=') # вывод '=======hello========'
'hello'.rjust(20, '=') # вывод '================hello'
'hello'.ljust(20, '=') # вывод 'hello================'

' hello '.strip() # вывод 'hello', удаляет пробелы
' hello '.lstrip() # вывод ' hello'
' hello '.rstrip() # вывод 'hello '



12 in b[3:5] #  встречается ли 12 в диапозоне от 3 до 5
12 not in b[3:5]
print(a.__sizeof__()) #  показывает сколько памяти занимает
type() #  показывает какого типа
reverse() #  перевернуть значании b.reverse()
append() #  присвоение b.append(12) в конец списка
b.insert(2, 'hello') #добавляет  в индекс 2 значание.
clear()  #  очистить
a = copy.copy(b)  #  ккопия списка import copy
a = copy.deppcopy (b) #  копирует значение к существующему, если есть таковой
count() #  b.count(12) подсчитает сколько раз встречается 12 в пременной b
index() # b.index(54) показывает какой по индиксу 54
insert() #  b.insert(2, 100) значение индекса 2 заменяет на 100
d.pop()  #  b. pop() удаляется значение с конца
b.sort() #  сортирует список по возрастанию
b.sort(key=str.lower()) #  сортирует список по алфавиту
b.remove('bat') #  b.remove(100) удлаяет если находит значение 100
del b['bat'] #  удаляет значение их списка
next(v) #  для итерируемых объектов, пример v = iter(range(5))+*
if i.isalpha(): #  подчитывает все буквы, только буквыи:
a, b, *c = [True, 7, 'hello', 9, '54', 67, 4, 3] # a=True, b=7, все остальное относится к с, т.к. * ввиде списка с=[9, '54', 67, 4, 3]
pprint.pprint(count) # Красиво печататет import pprint (полезно когда работаешь словарями)



#Множество d = {}
a.intersection(b) # пересечение цифр a и b
a.intersection_update(b) # пересечение цифр a и b, и запичать на a
print(a | b) #объединение двух множеств, совподающие значения только остается один
a & b #значении пересечения
print(a.union(b)) #Одно и тоже print(a | b)
print(a - b) # из множества а удаляются все пересекающие элементы с b
print(a ^ b) # удаляется все совподающие элементы
a > b #совподаю ли все значение b с a

"""Множество (set) — неупорядоченная коллекция, хранящая набор уникальныхзначений и поддерживающая для них операции добавления (add , update),
удаления (remove,discard,pop) и определения вхождения."""

"""Словарь (dict) — неупорядоченная коллекция произвольных объектов с
доступом по ключу. Словарь более известен как ассоциативный массив.
Словарь состоит из набора пар "Ключ-Значение". И в отличии от списка,
где к каждому элементу можно обратиться по его порядковому номеру
(индексу), в словаре обращение к элементу происходит по ключу."""
#dict key: value d= {key:value}.
d.get(5) #получить значение 5 key
d.setdefault('color', 'black') #проверяет есть ли ключ color, если есть оставляет как есть, если нет то добавляет black
d.clear() #очистить
d.setdefault(7, 'seven') - #если нет ключа 7 то создает и присваевает значение seven
d.popitem() - #удаляется рандомно значении
d.items() - # Ключ - значение
d.keys()  # Возвращаются только ключи
d.values() # Только значения
d[2]=3 #добавляет значение
del a['5'] # Удалить переменную


# tuple a=() кортеж - является не изменяемый
b = tuple(range(5)) # создает итибиральный кортеж
b = list(b) # преобразование tuple в список для редактирования
b = tuple(a) # преобразование списка в tuple

"""def Функции – это многократно используемые фрагменты программы.
При помощи функций можно объединить несколько инструкций в один
блок, присвоить этому блоку имя и затем, обращаясь по имени
этого блока, выполнить инструкции внутри него в любом месте
программы  необходимое число раз. """
