# exercise 1
# Using this class
class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age
# Instantiate three Cat objects using the code provided above.
# Outside of the class, create a function that finds the oldest cat and returns the cat.
# Print the following string: “The oldest cat is <cat_name>, and is <cat_age> years old.”.
# Use the function previously created.

# Instantiate three Cat objects
cat1 = Cat("Whiskers", 5)
cat2 = Cat("Socks", 8)
cat3 = Cat("Fluffy", 3)

# Function to find the oldest cat
def find_oldest_cat(*cats):
    oldest_cat = None
    max_age = -1
    for cat in cats:
        if cat.age > max_age:
            max_age = cat.age
            oldest_cat = cat
    return oldest_cat

# Find the oldest cat
oldest_cat = find_oldest_cat(cat1, cat2, cat3)

# Print the oldest cat's information
if oldest_cat:
    print(f"The oldest cat is {oldest_cat.name}, and is {oldest_cat.age} years old.")
else:
    print("No cats found.")

# exercise 2
class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height
        
        
def bark(self):
    print(f'{self.name} goes woof!”.')
    
# dog1=Dog('didi',60)
# print(bark(dog1))
def jump(self):
    print(f'{self.name} jumps {(self.height)*2} cm high!')
    
davids_dog=Dog('Rex',50)
print(davids_dog.name,davids_dog.height)
jump(davids_dog)
bark(davids_dog)

sarahs_dog=Dog('Teacup',20)
print(sarahs_dog.name,sarahs_dog.height)
jump(sarahs_dog)
bark(sarahs_dog)

if sarahs_dog.height > davids_dog.height:
    print(f"The bigger dog is {sarahs_dog.name}.")
elif sarahs_dog.height < davids_dog.height:
    print(f"The bigger dog is {davids_dog.name}.")
else:
    print("Both dogs are the same size.")
    
# exercise 3
class Song:
    def __init__(self , lyrics):
        self.lyrics = lyrics
    def sing_me_a_song(self):
        for lyric in self.lyrics:
            print(lyric)
    
stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])
stairway.sing_me_a_song()

# Exercise 4 : Afternoon At The Zoo
class Zoo:
    def __init__(self , zoo_name):
        self.name = zoo_name
        self.animals=[]
    def add_animal(self,new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)
            print(f"{new_animal} added to the zoo!")
        else:
            print(f"{new_animal} is already in the zoo.")
    def get_animals(self):
        if self.animals:
            print("Animals in the zoo:")
            for animal in self.animals:
                print(animal)
        else:
            print("No animals in the zoo.")
    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
            print(f"{animal_sold} has been sold.")
        else:
            print(f"{animal_sold} is not in the zoo.")
    def sort_animals(self):
        if self.animals:
            sorted_animals = {}
            for animal in sorted(self.animals):
                first_letter = animal[0].upper()
                if first_letter not in sorted_animals:
                    sorted_animals[first_letter] = [animal]
                else:
                    sorted_animals[first_letter].append(animal)

            print("Sorted and grouped animals:")
            for index, animals in enumerate(sorted_animals.values(), start=1):
                if len(animals) == 1:
                    print(f"{index}: {animals[0]}")
                else:
                    print(f"{index}: {animals}")

        else:
            print("No animals in the zoo.")
 
        

# Create an instance of the Zoo class
my_zoo = Zoo("My Zoo")

# Add animals to the zoo
my_zoo.add_animal("Ape")
my_zoo.add_animal("Bear")
my_zoo.add_animal("Baboon")
my_zoo.add_animal("Cat")
my_zoo.add_animal("Cougar")
my_zoo.add_animal("Eel")
my_zoo.add_animal("Emu")

# Sort and group the animals in the zoo
my_zoo.sort_animals()
            
# Create an object called ramat_gan_safari
ramat_gan_safari = Zoo("Ramat Gan Safari")

# Call all the methods
ramat_gan_safari.add_animal("Lion")
ramat_gan_safari.add_animal("Baboon")
ramat_gan_safari.add_animal("Tiger")
ramat_gan_safari.add_animal("Snake")
ramat_gan_safari.add_animal("Cougar")
ramat_gan_safari.add_animal("Bear")
ramat_gan_safari.add_animal("Eel")
ramat_gan_safari.add_animal("Octopus")

ramat_gan_safari.get_animals()

ramat_gan_safari.sell_animal("Lion")

ramat_gan_safari.get_animals()

ramat_gan_safari.sort_animals()
