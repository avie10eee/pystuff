class Dog: # class definition
    def __init__(self, name, age): # constructor
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} is now sitting.")# method for sitting

    def roll_over(self):
        print(f"{self.name} rolled over!") # method for rolling over

pig = Dog("Pig", 5) # declaring an object




print(f"your dog's name is {pig.name} and he is {pig.age} old.")

pigaction = input("do you want to sit or roll over? ")
if pigaction == "sit":
    pig.sit()
elif pigaction == "roll over":
    pig.roll_over()
else:
    print("invalid input")

