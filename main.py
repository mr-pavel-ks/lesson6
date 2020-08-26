class Animal():
    voice = ''
    type_an = ''

    def feed(self):
        print('Животное сыто')

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def sound(self):
        print(f"Животное издает звук  {self.voice}")


class Birds(Animal):
    def eggs(self):
        print('Яйца собраны')


class MilkyWay(Animal):
    def milk(self):
        print('Животное подоено')


class Goose(Birds):
    voice = 'gagagaga'
    type_an = 'Гусь'


class Cow(MilkyWay):
    voice = 'muuuuuuu'
    type_an = 'Корова'


class Sheep(Animal):
    voice = 'meeeeeeee'
    type_an = 'Овечка'

    def cut(self):
        print('Животное подстрижено')


class Chicken(Birds):
    voice = 'kokoko'
    type_an = 'Курица'


class Goat(MilkyWay):
    voice = 'mememe'
    type_an = 'Коза'


class Duck(Birds):
    voice = 'Crya'
    type_an = 'Утка'


my_Goose_1 = Goose('Серый', 5)
my_Goose_2 = Goose('Белый', 15)
my_Cow = Cow('Манька', 30)
my_Sheep_1 = Sheep('Барашек', 10)
my_Sheep_2 = Sheep('Кудрявый', 11)
my_Chicken_1 = Chicken("Ко-Ко", 16)
my_Chicken_2 = Chicken("Кукареку", 5)
my_Goat_1 = Goat("Рога", 6)
my_Goat_2 = Goat("Копыта", 2)
my_Duck = Duck('Кряква', 1)

oll = []
animal_list = [my_Goose_1, my_Goose_2, my_Cow, my_Sheep_1, my_Sheep_2, my_Chicken_1, my_Chicken_2, my_Goat_1, my_Goat_2,
               my_Duck]

for an_weight in animal_list:
    oll.append(an_weight.weight)
    max_weight = max(oll)
    if max_weight == an_weight.weight:
        name_big_animal = an_weight.name
        type_big_animal = an_weight.type_an
print(f' Самое тяжелое животное: {type_big_animal}, {name_big_animal}')
print(f" Общий вес животных: {sum(oll)}")


