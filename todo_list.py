def menu():
    print("""
1. Add task
2. Show tasks
3. Remove task
4. Exit
""")
    choice = int(input("choice? "))
    return choice

lis = []

def add(choice):
    if choice == 1:
        enter_task = input("Enter task: ")
        lis.append(enter_task)


def show(choice):

    if choice == 2:
        for index, task in enumerate(lis, start=1):
            print(index, task)

def rem(choice):
    if choice == 3:
        enter = int(input("what?"))
        lis.pop(enter -1)
        print(lis)

while True:
    choice = menu()
    if choice == 4:
        break
    add(choice)
    show(choice)
    rem(choice)