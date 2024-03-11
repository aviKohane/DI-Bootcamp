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

my_bengal=Bengal()
my_chartreux=Chartreux()
my_siamese=Siamese()    
all_cats=[my_bengal,my_chartreux,my_siamese]
sara_pets=Pets(all_cats)