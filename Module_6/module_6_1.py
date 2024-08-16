class Animal:
    alive = True
    fed = False

    def __init__(self, name):
        self.name = name


class Plant:
    edible = False

    def __init__(self, name):
        self.name = name


class Mammal(Animal):

    def eat(self, food):
        if isinstance(food, Plant):
            if food.edible:
                print(f'{self.name} с удовольствием съедает {food.name}')
                self.fed = True
            elif not food.edible:
                print(f'{self.name} неохотно съедает {food.name}')
                self.fed = False
                self.alive = False

        else:
            print(f'{self.name} отказывается съедать {food.name}')


class Predator(Animal):

    def eat(self, food):
        if isinstance(food, Plant):
            if food.edible:
                print(f'{self.name} с удовольствием съедает {food.name}')
                self.fed = True
            elif not food.edible:
                print(f'{self.name} неохотно съедает {food.name}')
                self.fed = False
                self.alive = False

        else:
            print(f'{self.name} отказывается съедать {food.name}')


class Flower(Plant):
    edible = False


class Fruit(Plant):
    edible = True


a1 = Predator('Дракон')
a2 = Mammal('Мэлман')
p1 = Flower('Багульник')
p2 = Fruit('Яблоко')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)