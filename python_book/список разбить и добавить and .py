# apples, bananas, tofu and cats 
spam = ['apples', 'bananas', 'tofu', 'cats']
a = ''
for i in range(len(spam)):
    print(i)
    if int(len(spam)) > int(i+2):
       a = a+spam[i]+', '
    elif int(len(spam)) > int(i+1):
       a = a+spam[i]+' and '
    elif int(len(spam)) == int(i+1):
        a = a+spam[i]

print(a)

