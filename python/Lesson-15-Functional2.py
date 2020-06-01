
def dannie(name, telephone, address):
    record = {
        'name' : name,
        'phone' : telephone,
        'address' : address
    }
    return record
user1 = dannie("Aynur", "+7932133432", "kazan")
print(user1)


def give_award(medal, *persons):
    for person in persons:
        print("Tovarich " + person.title() + " nagrajdaetsya medaliyu " + medal)

give_award("Za Berlin", "vasya", "petya")