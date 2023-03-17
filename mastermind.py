import random

COLORS = ["R", "G", "B", "O", "Y", "W"]
TRIES = 10
CODE_LENGTH = 4

def generate_code():
    code = []

    for _ in range (CODE_LENGTH):
        color = random.choice(COLORS)
        code.append(color)
    
    return code

def guess_code():
    while True:
        guess = input("Guess: ").upper().split(" ")

        if len(guess) != CODE_LENGTH:
            print(f"Your guess must me {CODE_LENGTH} colors.")
            continue

        for color in guess:
            if color not in COLORS:
                print(f"Invalide color: {color}. Please try again")
                break
        else:
            break
    
    return guess


