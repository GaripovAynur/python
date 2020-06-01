age = 14

if (age <= 4):
    print("You are baby")
elif (age > 4) and (age < 12):
    print("You age kid")
elif  (age >=12) and (age < 19):
    print("You age teenager")
else:
    print("You age old")

print("------END----------")


all_cars = ['kamaz', 'bmw', 'vw', 'seat', 'skoda', 'lada', 'audi']
german_cars = ['bmw', 'vw', 'audi']

for yyy in all_cars:
    if yyy in german_cars:
        print (yyy + " ""it is germany cars" )
    else:
        print("not garmany cars" " " + yyy)