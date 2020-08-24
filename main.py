class Animal():
    voice = ''
    type_an = ''

    def feed(self):
        print('Животное сыто')

    def __init__(self):
        self.name = []
        self.weight = 0

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

    def __init__(self):
        self.name = ['Серый', 'Белый']
        self.weight = 3


class Cow(MilkyWay):
    voice = 'muuuuuuu'
    type_an = 'Корова'

    def __init__(self):
        self.name = ['Манька']
        self.weight = 50


class Sheep(Animal):
    voice = 'meeeeeeee'
    type_an = 'Овечка'

    def cut(self):
        print('Животное подстрижено')

    def __init__(self):
        self.name = ['Барашек', 'Кудрявый']
        self.weight = 20


class Chicken(Birds):
    voice = 'kokoko'
    type_an = 'Курица'

    def __init__(self):
        self.name = ["Ко-Ко", "Кукареку"]
        self.weight = 5


class Goat(MilkyWay):
    voice = 'mememe'
    type_an = 'Коза'

    def __init__(self):
        self.name = ["Рога", "Копыта"]
        self.weight = 15


class Duck(Birds):
    voice = 'Crya'
    type_an = 'Утка'

    def __init__(self):
        self.name = ["Кряква"]
        self.weight = 5


my_Goose = Goose()
my_Cow = Cow()
my_Sheep = Sheep()
my_Chicken = Chicken()
my_Goat = Goat()
my_Duck = Duck()
oll = []
animal_list = [my_Goose, my_Cow, my_Sheep, my_Chicken, my_Goat, my_Duck]
for an_weight in animal_list:
    oll_weight = an_weight.weight * len(an_weight.name)
    oll.append(oll_weight)
    max_weight = max(oll)
    if max_weight == an_weight.weight:
        print(f' Самое тяжелое животное: {an_weight.type_an}')
print(f" Общий вес животных: {sum(oll)}")

