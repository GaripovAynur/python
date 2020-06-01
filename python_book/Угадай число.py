# Угадай число, у тебя 6 попыток

import random

a = random.randint(1, 6)
for i in range(1, 6):
    b = int(input("Введи число от 1 до 6:"))
    if a < b:
        print("Ваше число больше")
    elif a < b:
        print("Ваше число  меньше")
    elif a == b:
        print("Молодец, совпало")
        break
if a == b:
    print("Молодец, совпало")
else:
    print("Угаданное число , это" +a )