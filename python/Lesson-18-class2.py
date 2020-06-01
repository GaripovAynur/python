
#### Не разобрался почему не работает #####################

class Hero():
    """"Class to Create Hero for our Game"""
    def __init__(self, name, level, race):
        """"Initiate our hero"""
        self.name = name
        self.level = level
        self.race = race
        self.health = 100

    def show_hero(self):
        """Print all parametrs of this Hero"""
        discription = (self.name + "  Level is: " + str(self.level) + " Race is: " + " Health is" +
                       str(self.health)).title()
        print(discription)

    def level_up(self):
        """Upgrade Level of Hero"""
        self.level += 1

    def move(self):
        """Star moving hero"""
        print("Hero " + self.name + " start moving...")
    def set_health(self, new_health):
        self.health = new_health

#___________________________________________________________

class SuperHero(Hero):                                   #Родительское копирование из Hero
    """Class to creat Super Hero"""
    def __init__(self, name, level, race, magiclevel):   #Добавляем новое значение
        """"Initiate our Super Hero"""
        super().__init__(name, level, race)
        self.magiclevel = magiclevel1
        self.magic = 100
        """initiate our Super Hero"""

    def makemagic(self):
        """Use magic"""
        self.magic -= 10

    def show_hero(self):
        discription = (self.name + " Level is:" + str(self.level) + "Race is: " + self.race + "Health is" + str(self.health) +
                       " Magic is: " + self.magic).title()
        print(discription)