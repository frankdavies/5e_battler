import random

def rolldice(NofDice,NofSides):
    roll = 0
    total = 0 

    if NofSides == 0:
        return
    
    elif NofDice == 0:
        return
    
    else:
        while NofDice > roll:
            thisroll = random.randint(1,NofSides)
            total += thisroll
            roll += 1
            #print(thisroll)#dont include
        
        print(NofDice,'d',NofSides,"  TOTAL:",total,)
    return total

#Dice = int(input('number of dice:  '))
#Sides = int(input('number of sides: '))

#rolldice(Dice,Sides)


