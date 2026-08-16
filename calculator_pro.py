while True:
    def meno():
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

        choice = int(input("Choose: "))
        
        ent2 = float(input("num one? "))
        ent3 = float(input("num two? "))
        return choice , ent2 , ent3
        

    def total(choice , ent2 , ent3):
        if choice == 1:
            return( ent2 + ent3)
        elif choice == 2:
            return(ent2 - ent3)
            
        elif choice == 3:
            return(ent2 * ent3)
        elif choice == 4:
            return(ent2 / ent3)
        elif choice == 5:
            return(ent2 ** ent3)
        elif choice == 6:
            return ent2 % ent3

    while True:
        choice, ent2, ent3 = meno()
        if choice == 7:
            break
    
    
    result = total(choice,ent2,ent3)
    print(result)