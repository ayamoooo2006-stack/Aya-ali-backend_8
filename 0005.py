class Animal:
    def init(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species
    
    def info(self):
        print(f"Name: {self.name}, Age: {self.age}, Species: {self.species}")

# Subclass Dog
class Dog(Animal):
    def init(self, name, age, species, breed):
        super().init(name, age, species)
        self.breed = breed
    
    def info(self):
        super().info()
        print(f"Breed: {self.breed}")

# Subclass Cat
class Cat(Animal):
    def init(self, name, age, species, color):
        super().init(name, age, species)
        self.color = color
    
    def info(self):
        super().info()
        print(f"Color: {self.color}")

# Example usage with updated names and color
dog1 = Dog("Fgl", 3, "Dog", "Golden Retriever")
cat1 = Cat("Toty", 2, "Cat", "Pink")

dog1.info()
print("------")
cat1.info()