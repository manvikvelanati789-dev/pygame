class PetProfile:
    # init func for obj
    def __init__(self, animal_type, age, breed):
        self.animal_type = animal_type
        self.age = age
        self.breed = breed
    #obj func for info
    def show_details(self):
        print(f"Pet Type: {self.animal_type} | Age: {self.age} years | Breed: {self.breed}")
# create obj 
# create two distinct pet objects
pet1 = PetProfile(animal_type="Dog", age=4, breed="Labrador")
pet2 = PetProfile(animal_type="Cat", age=2, breed="Persian")
# call func.
pet1.show_details()
pet2.show_details()