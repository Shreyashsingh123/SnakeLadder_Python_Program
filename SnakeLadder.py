import random
print("Welcome to Snakes ladder problem")
position=0
print("Single player start at position:",position)

def diceroll():
    dice=random.randint(1,6)
    return dice
def randomoption(dice):
    global position
    opt=random.randint(1,3)#option
    if (opt==2):
        print("Ladder")
        position+=dice
    elif (opt==1):
        print("No move")
    else:
        print("Snake")
        position-=dice
    return position
