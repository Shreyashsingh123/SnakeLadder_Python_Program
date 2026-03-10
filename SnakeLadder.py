import random
print("Welcome to Snakes ladder problem")
position=0
print("Single player start at position:",position)

def diceroll():
    dice=random.randint(1,6)
    return dice