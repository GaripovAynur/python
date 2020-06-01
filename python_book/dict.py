a = {}
# aprint(a)
# a[2]=3
# a.setdefault(7, 'seven')
# a.setdefault(3, 'tri')
# a.setdefault(2, 'dva')
# a.setdefault(1, 'odin')
# a.setdefault(7, 'sevn')
# a.get(3)
#
# nt(a.get(3))

translet = {}
while True:
    s = input("Введите слово: ")
    if s in translet:
        print(str(translet)+'перевод' +s)
    else:
        r = input("Введите перевод"+s)
        translet[s] = r