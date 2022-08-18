'''
animalsl = ["dog","axolotle","kangoroo","fish","fox",]

animalsl.append("octopus")
animalsl.pop(1)
print(animalsl)

counter = (0)
nums = []
while counter <=4:
    bef = int(input("please enter 1 number "))
    counter = counter + 1
    nums.append(bef)
nums.sort()
print (str(nums))
'''


num = (0)
for i in range(46):
    num = num + i
    if i == 1000:
        break
    print(num)
