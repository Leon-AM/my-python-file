
import random
secret_number = random.randint(1,100)
count = 0
print("Guess the number between 1 and 100!")

while True:


    guess = int(input("your guess: "))
    count += 1

    if guess > secret_number :
        print("Smaller!")
    
    elif guess < secret_number :
        print("Lager!")
        
    elif guess == secret_number:
        print("Correct! :]")
        print(f"You guessed it in {count} attempts.")
        break