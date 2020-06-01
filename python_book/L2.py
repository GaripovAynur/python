##############AND###########################################

a = 16
b = 42
a > 0 and b > 0 # Истино если оба выржения верны

#####################OR######################################
a = 16
b = 42
a > 0 or b > 0 #Истино если хотябы одно выражение верное

################### IN ######################################
t = (1, 2, 3, 'abc', 'spam', 'eggs')
5 in t #Выражение не верное, 5 нет в t
'spam' in t #Выражение верное
'a' in ['a', 'b', 'c'] # True, так как а есть в списке.


########################### FOR ####################
l = [0, 1, 2, 3, 4]
for item in l :
    print(item)

for i in {0, 1, 2, 3, 4}: # тоже самое.
    print(i)


results = []
valeus = [1, 2, 4, 6]
for value in valeus:
    results.append(value ** 2) # Поднять во второй степень
    print(results)

for c in 'asdfghh' :
    print(c, end= '\n') # разбить по пробелам

string = ''
strings = ['sdad', 'fdsfa', 'agWR']
for s in strings:
    string += s #Склейка все в одну строчку
    print(string)
#Или
' '.join(strings) #Склейка все в одну строчку



l1ines = ['fsdfd', 'fdsfsfddf', 'dfsd']
for line in l1ines[:]:
    if len(line) > 7:
        l1ines.insert(0, line) #Установить значение 0 где > 7
        print(l1ines)
    l1ines


############range################

a = list(range(7, 13))
print(a) # 7, 8, 9, 10, 11, 12

a = list(range(7, 30, 3))
print(a) # [7, 10, 13, 16, 19, 22, 25, 28]

a = list(range(7))
print(a) # [0, 1, 2, 3, 4, 5, 6]


for i in range (1, 5):
    print(i, '^2', i **2) #1 ^2 1
                            #2 ^2 4
                            #3 ^2 9
                            #4 ^2 16



for i in range(5):
    print(i)
else:
    print('else!')


for i in range(10, 100, 5):
    print(i)
    if i >=30:
        break
else:
    print('else!')

while True:
    print('Once')
    break

i = 0
while True:
    print(i)
    i += 1
    if i > 3:
        break

i = 0
while i < 3:
    print(i)
    i +=1
else:
    print('Else')

############### def  Функция

def some_function():
    pass                #Ничего не делает
    print('Hello')
some_function()

def return_2():
    return 2
return_2()

def mul_x(x):
    print('Got', x)
    return
mul_x(3)

def mul_x(x):
    print('Got', x)
    def multiply (y):
        return x * y
    return multiply
mul_3 = mul_x(3)
mul_3(3)
mul_3(5)

def func():
    return 42, 'spam', 'eggs'
a, b, c = func()
print(a, b, c)


