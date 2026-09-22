class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

def get_pet(pet_type):
    pets = dict(dog=Dog, cat=Cat)
    pet_class = pets.get(pet_type)
    return pet_class() if pet_class else None

dog = get_pet("dog")
cat = get_pet("cat")

print(dog.speak())
print(cat.speak())
