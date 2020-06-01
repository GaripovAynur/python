# Угадай число, у тебя 6 попыток

number = int(input("Введите число"))

def collets(number):

    if number % 2 == 0:
        return number % 2
    else:
        return 3 * number + 1

print(collets(number))
