
some_str = "qwerty"

some_str[0] # q - первый элемент
some_str[-1] # y - последний элемент
some_str[-2] # t - предпоследний элемент
some_str[1:4] # wer - то, что между индексами 1 и 4
some_str[:3] # qwe - с самого начала по 3

print(some_str[-1])
len(some_str)  #подсчитает сколько букв
b = len(some_str)
print(b)

a = some_str[len(some_str)-1] #взять значение
print(a)


####### СПИСОК  LISTS  [] ###############################
array = [1, 2, 3, 5]

a = array[0] = 10 # Заменить на 10
print(array)

b = array[2:3]
print(array)

c = array[:2] = [1, 4, 5]
print(array)

array.insert(0, 4) #Добавить на первое значение 4
print(array)

array.append(11) # Добавляет в конец 11
print(array)

array.pop() #Забрал с конца значение


###### Кортеж typl () #### Отличает от списка тем что является не изменяемым
tpl = (1, 2 ,3 ,4)

# tpl[2] = 7 #Заменить значение как списке не даст
print(tpl)


###### Словарь { 'key': 'value'} #######
dct = {'key': 'value'}
print(dct)

dct['spam'] = 'egges'
print(dct)

a = dct.keys()  # Возвращаются только ключи
b = dct.values() # Только значения
c = dct.items()  # Ключ - значение
print(str(a) + " " + str(b))

######## МНОЖЕСТВО похож на словарь , но без key ######

set_ = {1, 2, 3}
set_.add(4) #Добавить значение
print(set_)

array.append(set_) # Добавить предедущему списук array список set
print(array)

###########################################################
##############Форматирование строк#########################

a = '%%r %r %%s' % 'spam' # вместо %s применяется любое значение, например spam
print(a)

a = 'value : {}'.format(42)
print(a)

a = '{} and {}'.format('eggs', 'spam')
print(a)

a = '{1} and {0}'.format('eggs', 'spam')  #Если мы хотим первое значение ставит на нулевое и второе значение на первое
print(a)

a = '{0}{1}{0}'.format(13,11) # 0 = 13   1 = 11    0 = 13
print(a)

a = '{value}{key}{value}'.format(value = 42, key='spam')
print(a)

a = 'value: %.2f' % 12.345 #Округляют, до 2 значении после запятой
print(a)

#####не работает возможно версия питона##############################
#value = 123,456
#a_line = 'spam and eggs'
#text = (
#    'first line',
#    f'\na value {value:.2f}\n'
#    f'a line {a_line}'
#)
#print(text)

##########################################

matrix = [
#    0 1 2
    [1,2,3],  #0
    [4,5,6],  #1
    [7,8,9]   #2
]
print(matrix)

a = matrix[1]
print(a)

a = matrix[1][2]
print(a)  #будет значение 6

# if значение
a = 4
b = 6
value = a * 2 if a > b else b // 2
print('value',  value)