lis = {}

def menu():
    print("""
1. Add Contact
2. Show Contacts
3. Search Contact
4. Remove Contact
5. Exit
""")
    choice = int(input("choice? "))
    return choice



def add():
    name = input("Name? ")
    ph = input("phone number? ")
    lis.update({name : ph})


def save():
    print(lis)


def search():
    ent = input("Name? ")
    print(lis.get(ent))
             

def remove():
    ent = input("Name? ")
    del lis[ent]


while True:
    choice = menu()
    
    if choice == 1:
        add()
    if choice == 2:
        save()
    if choice == 3:
        search()
    if choice == 4:
        remove()
    if choice == 5:
        break
         
