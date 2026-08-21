def menu():
    print("""
========================
    CALCULATOR
========================

1. Add
2. Subtract
3. Multiply
4. Divide
5. Power
6. Modulo
7. Exit\n""")




def operacion(choice , num1 , num2):
    if choice == 1:
        return num1 + num2
    elif choice == 2:
        return num1 - num2
    elif choice == 3:
        return num1 * num2
    elif choice == 4:
       return num1 / num2
    elif choice == 5:
        return num1 ** num2
    elif choice == 6:
        return num1 % num2



while True:
    menu()
    try:    
        choice = int(input("choice? "))
    except ValueError:
        print("your choice isn't int!")
        continue
    while choice >7:
        print("bog")
        choice = int(input("choice? "))
            
    if choice ==7:
        break
    else:
        num1 = float(input("num1 ?"))
        num2 = float(input("num2 ?"))
        
    result = operacion(choice , num1 , num2)
    print(f"\n Result: {result}")


