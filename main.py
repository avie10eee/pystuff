# importing stuff
from tqdm import tqdm
import time

# welcome
print("╔═╦╗╔╦╗╔═╦═╦╦╦╦╗╔═╗╦╦╗╔═╗")
print("########################")
print("########################")
print("##welcome to pig coffee##")
print("########################")
print("########################")
print("╚═╩══╩═╩═╩═╩╝╚╩═╩═╝╚╩═╩═╝")

# filtering out the itai's of the world
name = input("what is your name ")
if name == "itai":
    print("go away itai you are not permitted here")
else:
    print("welcome to pig coffee how can i help you, my name is gerared")
    print("menu")
    print("1. coffee")
    print("2. tea")
    print("3. chocolate")

    # All the order stuff
    order = input("what would you like ")
    if order == "coffee":
        print("just a second")
        for i in tqdm(range(101),
            desc="Brewing…",
            ascii=False, ncols=75):
            time.sleep(0.01)

        print("Complete.")
        print("here is your coffee")

    if order == "tea":
        print("just a second")
        for i in tqdm(range(101),
            desc="Steeping…",
            ascii=False, ncols=75):
            time.sleep(0.01)

        print("Complete.")
        print("here is your tea")

    if order == "chocolate":
        print("just a second")
        for i in tqdm(range(101),
            desc="Getting it…",
            ascii=False, ncols=75):
            time.sleep(0.01)

        print("Complete.")
        print("here is your chocolate")
    # do you want to stay?
    stay = input("do you want to (stay) or (take it to go) ")
    if stay == "stay":
        print("have a seat")
    else:
        if stay == "take it to go":
            print("goodbye")