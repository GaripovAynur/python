

name = input("Please enter Your name:")

print("Privet " + name)

num1 = input ("Enter X:  ")
num2 = input ("Enter Y:  ")
summa1 = num1 + num2           #Складывает просто цифры 234+123=234123
summa2 = int(num1) + int(num2) #Математический расчет
print(summa1)
print(summa2)

print ("########Проверять пароль пока не совпадет со словом sekret#########")
message = ""
while True:
    message = input("Enter password  ")
    if message == 'secret'
        break
    print(message + "Password not correct")
print("Password was:" + message)


#################################################################

print ("########Собирать веденные слова#########")
mylist = []       # пустой список
msg =""           # пустая переменная

while msg != 'stop'.upper():      #upper все с большой буквой
    msg = input("Enter new item, and stop to :   ")
    mylist.append(msg)            #накапливать все слова msg
print(mylist)