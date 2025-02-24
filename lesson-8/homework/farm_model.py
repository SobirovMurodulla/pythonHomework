# farm_model.py

class Animal:
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species

    def eat(self):
        print(f"{self.name} the {self.species} is eating.")

    def sleep(self):
        print(f"{self.name} the {self.species} is sleeping.")

class Cow(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, "Cow")

    def moo(self):
        print(f"{self.name} the Cow says 'Moo!'")

class Chicken(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, "Chicken")

    def cluck(self):
        print(f"{self.name} the Chicken says 'Cluck!'")

class Sheep(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, "Sheep")

    def baa(self):
        print(f"{self.name} the Sheep says 'Baa!'")

cow = Cow("Bessie", 5)
chicken = Chicken("Clucky", 2)
sheep = Sheep("Wooly", 3)

cow.eat()
cow.moo()
chicken.sleep()
chicken.cluck()
sheep.eat()
sheep.baa()