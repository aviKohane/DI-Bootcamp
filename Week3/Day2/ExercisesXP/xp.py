# 🌟 Exercise 1 : Pets
# Instructions
# Create another cat breed named Siamese which inherits from the Cat class.
# Create a list called all_cats, which holds three cat instances :
# one Bengal, one Chartreux and one Siamese.
# Those three cats are Sara’s pets.
# Create a variable called sara_pets which value is an instance of the Pets class,
# and pass the variable all_cats to the new instance.
# Take all the cats for a walk, use the walk method.
class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())


class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'


class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Siamese(Cat):
    def sing(self, sounds):
        return f'{sounds}'


# Create instances of cat breeds
bengal_cat = Bengal("Bobbie", 3)
chartreux_cat = Chartreux("Charlie", 2)
siamese_cat = Siamese("Sissi", 4)

# Create a list of all cats
all_cats = [bengal_cat, chartreux_cat, siamese_cat]

# Create an instance of the Pets class
sara_pets = Pets(all_cats)

# Take all the cats for a walk
sara_pets.walk()


# 🌟 Exercise 2 : Dogs
# Instructions
# Create a class called Dog with the following attributes name, age, weight.
# Implement the following methods in the Dog class:
# bark: returns a string which states: “<dog_name> is barking”.
# run_speed: returns the dogs running speed (weight/age*10).
# fight : takes a parameter which value is another Dog instance, called other_dog.
# This method returns a string stating which dog won the fight. 
# The winner should be the dog with the higher run_speed x weight.

# Create 3 dogs and run them through your class.
class Dog:
    def __init__(self,name,age,weight):
        self.name=name
        self.age=age
        self.weight=weight
    def bark(self):
        return f'{self.name} is barking'
    def run_speed(self):
        return self.weight/self.age*10
    def fight(self,other_dog):
        self_result = self.run_speed() * self.weight
        other_result = other_dog.run_speed() * other_dog.weight
        if other_result > self_result:
            return f'{other_dog.name} won the fight!' 
        elif other_result == self_result:
            return f'There is no winner. '
        else:
            return f'{self.name} won the fight!'
            
dog1=Dog('Fifi',8,20)
dog2=Dog('Medor',5,30)
dog3=Dog('Hulk',3,15)
            
print(dog3.bark())
print(dog2.run_speed())
print(dog1.fight(dog2))      

