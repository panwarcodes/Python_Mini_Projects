# Rock_Paper_Scissor by @panwarcodes/github
import random

# Game logic
def game_logic(rps_user):
    if (rps_user == choice):
        return "I chose the same, draw!"
    elif (rps_user == 'rock' and choice == 'scissor'):
        return "I chose scissor randomly, I lost!"
    elif (rps_user == 'scissor' and choice == 'rock'):
        return "I chose rock randomly, I won!"
    elif (rps_user == 'scissor' and choice == 'paper'):
        return "I chose paper randomly, I lost!"
    elif (rps_user == 'paper' and choice == 'rock'):
        return "I chose rock randomly, I lost!"
    elif (rps_user == 'paper' and choice == 'scissor'):
        return "I chose scissor randomly, I won!"
    elif (rps_user == 'rock' and choice == 'paper'):
        return "I chose paper randomly, I won!"
    else:
        return "Your choice is invalid!"

while True:
    rps = ["rock", "paper", "scissor"]
    choice = random.choice(rps)
    rps_user = input("------------------------------------------------\nEnter your choice (rock, paper, scissor): ").lower()

    # Call game logic
    print(game_logic(rps_user))
    while True:
        restart = input("------------------------------------------------\nDo you want to play again? [y/n]: ").lower()
        if restart in ('y', 'n'):
            break
        print("Invalid input!")
    if (restart == 'y'):
        continue
    else:
        print("Goodbye, it was nice playing with you!")
        break