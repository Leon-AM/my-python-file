ent = float(input("number? "))

def negpos():

    if ent < 0:
        print("Negative")
    elif ent == 0:
        print("Zero")
    else:
        print("positive")

def evod():
    if ent == 0:
        print("zero")
    elif ent % 2 == 0:
        print("Even")
    else:
        print("odd")
    
negpos()
evod()