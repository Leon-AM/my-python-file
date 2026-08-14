import random


choices = ["Rock", "Paper", "Scissors"]

print("""
1. Rock
2. Paper
3. Scissors
""")

user_choice = int(input("Your choice: "))

if user_choice not in [1, 2, 3]:
    print("Invalid choice!")
else:
    user_index = user_choice - 1
    computer_index = random.randint(0, 2)

    user = choices[user_index]
    computer = choices[computer_index]

    print(f"You: {user}")
    print(f"Computer: {computer}")

    if user == computer:
        print("Draw!")

    elif (
        (user == "Rock" and computer == "Scissors")
        or (user == "Paper" and computer == "Rock")
        or (user == "Scissors" and computer == "Paper")
    ):
        print("You win! ")

    else:
        print("Computer wins! ")