# Simple strong password generator by @panwarcodes/github
import random

desired_length = int(input("Desired length of password: "))
randomize_me = "abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*"
converting_to_list = list(randomize_me)
random.shuffle(converting_to_list)
list_to_string = ''.join(converting_to_list)

print(list_to_string[:desired_length])
        
    
