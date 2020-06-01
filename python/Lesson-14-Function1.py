

def napechatat_privetstvie(name):
    print("Congratulation "+ name + "wish you all the best!")


def summa(x, y):
    print(x+y)
    print(str(x)+str(y))

napechatat_privetstvie("Aynur")
napechatat_privetstvie("Denis")

summa(10, 20)

#################найти факториал ##############################

def factorial(x):
    otvet = 1
    for i in range (1, x + 1):
        otvet = otvet * i
    return otvet
print(factorial(4))


for i in range(1, 10):
    print(str(i) + "!\t = " + str(factorial(i)))