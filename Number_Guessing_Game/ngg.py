# This is a Number Guessing Game by @panwarcodes/github
import random
import time

random_num = random.randint(1, 30)
print("Welcome to Number Guessing Game!")
print("Game loading...")
time.sleep(2)

# Game logic
attempts = 0
while attempts < 11:
    attempts += 1
    if (attempts == 11):
        print("Game Over!\nTry again later...")
        break
    try:
        get_guess = int(input("Guess the number between 1 to 30, you get 10 attempts: "))
        if (get_guess == random_num):
            print("You WON!")
            break
        elif (get_guess != random_num):
            if get_guess < random_num:
                hint_giver = "Too low"
            elif (get_guess > random_num):
                hint_giver = "Too high"
            print(f"{hint_giver}, try again.\nAttempts used: {attempts}")
    except ValueError:
        print("Integer values are allowed only!\nYour attempt got used, be careful!.")
    
    