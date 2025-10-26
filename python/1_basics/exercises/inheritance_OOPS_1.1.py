# Python Object-Oriented Programming (OOP) - Exercises

# ==============================================================================
# Exercise 1: Inheritance - 2D and 3D Vectors
# ==============================================================================
# 1. Create a class (2-D vector) and use it to create another class representing a 3-D vector.

# solution 1
class  Vector2D:
    def __init__(self,x , y):
        self.x = x
        self.y = y
    
    def __str__(self):
       return f"{self.x}i + {self.y}j"
    
class Vector3D(Vector2D):
    def __init__(self,x, y, z):
        super().__init__(x,y)
        self.z = z

    def __str__(self):
        return f"{self.x}i + {self.y}j + {self.z}k"

if __name__ == "__main__":
    v2D = Vector2D(1,3)
    v3D = Vector3D(1,3,5)
    print(v2D)
    print(v3D)


# ==============================================================================
# Exercise 2: Multilevel Inheritance - Animals, Pets, and Dogs
# ==============================================================================
# 2. Create a class ‘Pets’ from a class ‘Animals’ and further create a class ‘Dog’ from ‘Pets’.
#    Add a method ‘bark’ to class ‘Dog’.

class Animals:
    def __init__(self,name, species):
        self.name = name
        self.species = species
    
    def __str__(self):
        return f"Animal Name: {self.name}\nAnimal Species: {self.species}"
    

class Pets(Animals):
    def __init__(self,name, species, colour, size):
        super().__init__(name, species)
        self.colour = colour
        self.size = size 
    
    def __str__(self):
        return f"Animal Name: {self.name}\nAnimal Species: {self.species}\nAnimal Colour: {self.colour}\nAnimal Size: {self.size}"

class Dog(Pets):
    def __init__(self,name, species, colour, size, breed):
        super().__init__(name, species, colour, size)
        self.breed = breed

    def __str__(self):
        return f"{super().__str__()}\nAnimal Breed: {self.breed}"

    def sound(self):
        print("Bark!!!!!!")

if __name__ == "__main__":
    a = Dog("Pakun","Mammal","Brown", "Medium", "German shephard")
    a.sound()
    print(a)
# ==============================================================================
# Exercise 3: Properties and Setters - Employee Class
# ==============================================================================
# 3. Create a class ‘Employee’ and add salary and increment properties to it.
#    Write a method ‘salaryAfterIncrement’ with a @property decorator.
#    Include a setter that changes the value of the increment based on the salary.

class Employee:
    def __init__(self, name, salary, increment):
        self.name = name
        self.salary = salary
        self.increment = increment
    
    @property
    def salaryAfterIncrement(self):
        return self.salary + (self.salary * self.increment/100)
    
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self,amount):
        self.increment = (amount/self.salary) * 100
        
        

if __name__ == "__main__":
    a = Employee("Mayank", 100,10)
    print(a.salaryAfterIncrement)
    a.salaryAfterIncrement = 20
    print(a.salaryAfterIncrement)
    print(a.increment)

# ==============================================================================
# Exercise 4: Operator Overloading - Complex Numbers
# ==============================================================================
# 4. Write a class ‘Complex’ to represent complex numbers, along with overloaded
#    operators ‘+’ and ‘*’ which add and multiply them.

# ==============================================================================
# Exercises 5, 6, and 7: Vector Class - Operator Overloading and Special Methods
# ==============================================================================
# 5. Write a class ‘Vector’ representing a vector of n dimensions. Overload the `+` and `*`
#    operators to calculate the sum and the dot product of two vectors.

# 6. For the ‘Vector’ class, write the `__str__()` method to print the vector as follows:
#    7i + 8j + 10k
#    (Assume a 3-dimensional vector for this problem).

# 7. For the ‘Vector’ class, override the `__len__()` method to display the dimension of the vector.