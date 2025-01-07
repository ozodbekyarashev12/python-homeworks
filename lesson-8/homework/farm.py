class Animal:
    def __init__(self, name, sound, food_type):
        self.name = name
        self.sound = sound
        self.food_type = food_type

    def make_sound(self):
        return f"{self.name} makes a {self.sound} sound."

    def eat(self):
        return f"{self.name} eats {self.food_type}."

    def sleep(self):
        return f"{self.name} is sleeping."


class Cow(Animal):
    def __init__(self, name, sound="moo", food_type="grass"):
        super().__init__(name, sound, food_type)

    def produce_milk(self):
        return f"{self.name} produces milk."


class Chicken(Animal):
    def __init__(self, name, sound="cluck", food_type="seeds"):
        super().__init__(name, sound, food_type)

    def lay_egg(self):
        return f"{self.name} lays an egg."


class Horse(Animal):
    def __init__(self, name, sound="neigh", food_type="hay"):
        super().__init__(name, sound, food_type)

    def run(self):
        return f"{self.name} is running fast."


# Example Usage
cow = Cow("Cowy")
chicken = Chicken("Misschicken")
horse = Horse("Sniper")

print(cow.make_sound())
print(cow.eat())
print(cow.produce_milk())

print(chicken.make_sound())
print(chicken.lay_egg())

print(horse.make_sound())
print(horse.run())