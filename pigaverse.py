import random


print("#######################################")
print("##                                   ##")
print("##                                   ##")
print("##                                   ##")
print("##          THE PIGAVERSE            ##")
print("##                                   ##")
print("##                                   ##")
print("##                                   ##")
print("#######################################")

name = input("welcome to the pigaverse. what is your name? ")

if name == "itai":
    print("welcome itai (sarcasticly)")
else:
    print("thank you for coming "+name)
if name == "avie":
    print("welcome owner")

game = input("would you like to play a guessing game, yes or no ")
ran = random.randint(1, 10)

if game == "yes":
    num = input("im guessing of a number between 1 and 10 what is it? ")





if num == ran:
    print("you got it right")
else:
    print("the answer was "+ str(ran))

