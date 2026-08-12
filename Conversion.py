while True:
    enter1 = float(input("number1?"))
    enter2 = input("A:K/M? ,B:M/K ,C:C/F ,D:F/C ?")

    if enter2 == "A":
        print(enter1 * 1000)
    elif enter2 == "B":
        print(enter1 / 1000)
    elif enter2 == "C":
        print(enter1 *1.8 +32)
    elif enter2 == "D":
        print((enter1 - 32) / 1.8)
    else:
        print("Invalid option!")
    enter3 = input ("exit: y/n?")
    if enter3 == "y":
        break