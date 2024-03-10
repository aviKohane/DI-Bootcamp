class Farm:
    def __init__(self,name):
        self.name = name
        self.animals = {}  
    def add_animal(self,animal,num=1):
        if animal in self.animals:
            self.animals[animal]+=num
        else:
            self.animals[animal]=num
    def get_info(self):
        info = f"{self.name}'s farm\n"
        for animal, num in self.animals.items():
            info += f"{animal} : {num}\n"
        info += "E-I-E-I-O!"
        return info
    def get_animal_types(self):
        return sorted(list(self.animals.keys()))
    def get_short_info(self):
        animal_types = self.get_animal_types()
        animal_str = ""
        if len(animal_types) == 1:
            animal_str = animal_types[0]
        elif len(animal_types) > 1:
            animal_str = ", ".join(animal_types[:-1]) + " and " + animal_types[-1]
        return f"{self.name}'s farm has {animal_str}{'s' if len(animal_types) > 1 else ''}."
          
macdonald = Farm("McDonald")
macdonald.add_animal('cow',5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())
print("Animal types in the farm:", macdonald.get_animal_types())
print(macdonald.get_short_info())