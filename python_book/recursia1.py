#Палиндром
#шабаш
#

def palindrom(s):
    if len (s) <=1: #Проверяет длина слово больше 0, если до то True
        return True
    if s[0]!=s[-1]: #Если последние буквы не совподают, то false
        return False
    return palindrom(s[1:-1]) # Если каждый раз совподает последня и первая буква, предпоследняя и вторая буква и т.д. то True
print(palindrom('шабаш')) #Проверочное слово
