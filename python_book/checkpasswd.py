# put your python code here
import re

a = input('Прошу вести сложный пароль')
passre1 = re.compile(r'\W')
passre2 = re.compile(r'\d')
passre3 = re.compile(r'[a-z]')
passre4 = re.compile(r'[A-Z]')
W = passre1.search(a)
d = passre2.search(a)
az = passre3.search(a)
AZ = passre4.search(a)
if 8 <= len(a):
    if W != None:
        if d != None:
            if az != None:
                if AZ != None:
                    print('Пароль сложный')
                else:
                    print('Пароль не сложный, нет заглавных букв!')
            else:
                print('Пароль не сложный, нет маленьких букв!')
        else:
            print('Пароль не сложный, нет цифр!')
    else:
        print('Пароль не сложный, нет специального символа!')
else:
    print('Пароль не сложный')
