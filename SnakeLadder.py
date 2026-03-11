import random
print("Welcome to Snakes ladder problem")
position1=0
position2=0
print("Player start at position 0:")

countdice1=0
countdice2=0

def diceroll():
    dice=random.randint(1,6)
    return dice

def randomoption(dice,position):
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
    # print("Position is: ",position)
    return position

while(position1<100 and position2<100):# until any player reaches 100(win) it will execute
    dice=diceroll()
    position1=randomoption(dice,position1)
    print("Position 1 is",position1)
    countdice1+=1

    if(position1>=100):
        print("Player 1 win")
        print("Total count of dice is:",countdice1)
        break
    
    dice=diceroll()
    position2=randomoption(dice,position2)
    print("Position 2 is:",position2)
    countdice2+=1
    if(position2>=100):
        print("Player 2 win")
        print("Total count of dice is:",countdice2)
        break
    
    
    
