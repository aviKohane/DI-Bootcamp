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


# Exercise 4 : Family
# Instructions
# Create a class called Family and implement the following attributes:

# members: list of dictionaries
# last_name : (string)

# Implement the following methods:

# born: adds a child to the members list (use **kwargs), don’t forget to print a message congratulating the family.
# is_18: takes the name of a family member as a parameter and returns True if they are over 18 and False if not.
# family_presentation: a method that prints the family’s last name and all the members’ details.

# Create an instance of the Family class, with the last name of your choice, and the below members. Then call all the methods you created in Point 2.

#     [
#         {'name':'Michael','age':35,'gender':'Male','is_child':False},
#         {'name':'Sarah','age':32,'gender':'Female','is_child':False}
#     ]

class Family:
    def __init__(self,members,last_name):
        self.members=members
        self.last_name=last_name
        
    def born(self, **kwargs):
        self.members.append(kwargs)
        print(f"Congratulations! {kwargs['name']} is born into the {self.last_name} family.")
        
    def is_18(self, name):
        for member in self.members:
            if member['name'] == name:
                return member['age'] >= 18
        return False       
    
    def family_presentation(self):
        print(f'Last name family: {self.last_name}:')
        for member in self.members:
            print(f'Name: {member['name']}, Age: {member['age']}, Gender: {member['gender']}, Child: {member['is_child']}")')
    
# Create an instance of the Family class
family = Family( [{'name': 'Michael', 'age': 15, 'gender': 'Male', 'is_child': False},
{'name': 'Sarah', 'age': 22, 'gender': 'Female', 'is_child': False}],"Fridman")

# Call the born method to add a new member
family.born(name='Ety', age=0, gender='Female', is_child=True)

# Call the is_18 method to check if a member is over 18
print(f"Is Sarah over 18? {family.is_18('Sarah')}")

# Call the family_presentation method to print family details
family.family_presentation()
        
        
# Exercise 5 : TheIncredibles Family
# Instructions
# Create a class called TheIncredibles. This class should inherit from the Family class:
# This is no random family they are an incredible family, therefore the members attributes,
# will be a list of dictionaries containing the additional keys : power and incredible_name. (See Point 4)

# Add a method called use_power, this method should print the power of a member only if they are over 18 years old. If not raise an exception (look up exceptions) which stated they are not over 18 years old.


# Add a method called incredible_presentation which :

# Print a sentence like “*Here is our powerful family **”
# Prints the family’s last name and all the members’ details (ie. use the super() function, to call the family_presentation method)


# Create an instance of the Incredibles class, with the “Incredibles” last name, and the below members.

#     [
#         {'name':'Michael','age':35,'gender':'Male','is_child':False,'power': 'fly','incredible_name':'MikeFly'},
#         {'name':'Sarah','age':32,'gender':'Female','is_child':False,'power': 'read minds','incredible_name':'SuperWoman'}
#     ]


# Call the incredible_presentation method.


# Use the born method inherited from the Family class to add Baby Jack with the following power: “Unknown Power”.


# Call the incredible_presentation method again.


class TheIncredibles(Family):
    def __init__(self, last_name, members):
        super().__init__(last_name, members)

    def use_power(self, name):
        for member in self.members:
            if member['name'] == name:
                if member['age'] >= 18:
                    print(f"{member['name']} uses the power: {member['power']}")
                else:
                    raise ValueError(f"{member['name']} is not over 18 years old.")

    def incredible_presentation(self):
        print("*Here is our powerful family**")
        super().family_presentation()


# Create an instance of the TheIncredibles class
incredibles_family = TheIncredibles("Incredibles", [
    {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False, 'power': 'fly', 'incredible_name': 'MikeFly'},
    {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False, 'power': 'read minds', 'incredible_name': 'SuperWoman'}
])

# Call the incredible_presentation method
incredibles_family.incredible_presentation()

# Add Baby Jack using the born method
incredibles_family.born(name='Baby Jack', age=0, gender='Male', is_child=True, power='Unknown Power', incredible_name='JackUnknown')

# Call the incredible_presentation method again
incredibles_family.incredible_presentation()

