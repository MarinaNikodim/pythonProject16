class Animal:
    alive = True
    fed = False

    def __init__(self, name):
        self.food = None
        self.name = name

    def eat(self, food):
        self.food = food.name
        if isinstance(food, Plant) and food.edible:
            self.food = food.name
            self.fed = True
            #Fruit.edible = True
            print(f' {self.name} съел {food.name}')

        else:
            #Flower.edible = False
            print(f' {self.name} не стал есть {food.name}')
            self.alive = False


class Plant:
    def __init__(self, name, edible = False):
        self.name = name
        self.edible = edible


class Mammal(Animal):
    pass


class Predator(Animal):
    pass


class Flower(Plant):
    #edible = False
    def __init__(self, name):
        super().__init__(name, edible=False)


class Fruit(Plant):
    #edible = True
    def __init__(self, name):
        super().__init__(name, edible=True)


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
