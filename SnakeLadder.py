import random
print("Welcome to Snakes ladder problem")
position=0
print("Single player start at position:",position)

countdice=0
def diceroll():
    dice=random.randint(1,6)
    return dice
def randomoption(dice):
    global position
    opt=random.randint(1,3)#option
    #1 no move 2 ladder
    if (opt==2):
        if(position+dice<=100):
            position+=dice
    elif (opt==1):
        # print("No move")
        pass
    else:
        position-=dice
        if(position<0):#if position is negative then start from 0
            position=0
    print("Position is: ",position)
    return position

while(position<100):# until player1 reaches 100(win) it will execute
    dice=diceroll()
    position=randomoption(dice)
    countdice+=1

if(position>=100):
    print("Player1 win")
print("Total count of dice is:",countdice)
