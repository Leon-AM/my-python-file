
import random
hads = random.randint(1,100)
count = 0
while True:


    ent1 = int(input("num?"))

    if ent1 > hads :
        print("smaler")
        count += 1
    elif ent1 < hads :
        print("larger")
        count += 1
    elif ent1 == hads:
        print("good job")
        count += 1
        break
print (f"your try : {count}")