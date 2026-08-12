while True:
    enter1 = int(input("number 1:"))
    enter2 = int(input("number 2:"))
    opertion = input(" + , - , * , / :")

    if opertion == "+":
        print(enter1 + enter2)

    elif opertion == "-":
        print(enter1 - enter2)

    elif opertion == "*":
        print(enter1 * enter2)

    elif opertion == "/":
        print(enter1 / enter2)
    enter3 = input ("exit:y/n?")
    if enter3 == "y":
        break