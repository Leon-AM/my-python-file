
import random
hads = random.randint(1,100)
while True:


    ent1 = int(input("num?"))

    if ent1 > hads :
        print("smaler")
    elif ent1 < hads :
        print("larger")
    elif ent1 == hads:
        print("good job")
        break
