print('')

from dice_function_file import rolldice
from combatants import combatants
import random

friends = []
foes = []
the_dead = []

def create_factions(list):
  
  for combatant in list:
    if combatant["Faction"] == "friends":
      friends.append(combatant)
    else:
      foes.append(combatant)

create_factions(combatants)

def print_faction_names(faction):
  print(faction[0]["Faction"],':')
  for member in faction:
    print(member["Name"])
  print('')
  
print_faction_names(friends)
print_faction_names(foes)

input('')

def damage_dice_ints(comb):
    #This fuction takes the damage dice and turn them into seperate ints 
    # that can be input to the dice roll function  
    dmg_dice = comb["MainAttackDmg"]
    number_and_dice = dmg_dice.split('d')
    number_and_dice_ints = [int(item) for item in number_and_dice]
    return number_and_dice_ints


def attack_is_made(attacker,defender): 
  #this function processes the attacker attacking the defender, it 
  #determines hit or miss, calculates damage, and adds damage to the 
  #defenders total damage taken

  ### need to add crits in here
  attackRoll = rolldice(1,20) + int(attacker["MainAttackMod"])
  if attackRoll >= defender["AC"]: #if hit
      
      print('Hit!')

      damageRoll = rolldice(damage_dice_ints(attacker)[0],damage_dice_ints(attacker)[1])
      damageDealt = damageRoll + attacker["DmgMod"]

      defender["DmgTaken"] += damageDealt

      print(defender["Name"],'takes',damageDealt,'damage from',attacker["Name"])

  else: #if miss
      print(attacker["Name"],'missed',defender["Name"])
  
  if defender["DmgTaken"] >= defender["HP"]: #if the defender is killed
    print(defender["Name"],'has been slain by',attacker["Name"])
    the_dead.append(defender)

    if defender["Faction"] == 'friends':
      friends.remove(defender)

    else:
      foes.remove(defender)


    

def faction_attack(attacking_faction, target_faction):
  for combatant in attacking_faction:
    if len(target_faction) > 0:
      
      attacks_attempted = 0
      
      while attacks_attempted < combatant["NumofAttacks"]:
        target_number = random.randint(1,len(target_faction)) - 1
        attack_is_made(combatant,target_faction[target_number])
        attacks_attempted += 1
    
    else:
      filler = input('\nThere is no one left to fight.')
      break


while True:
  
  ### need to add an initiative system in here

  
  if (len(foes) > 0) and (len(friends) > 0) : 
    
    faction_attack( friends , foes )
    faction_attack( foes , friends )
    
  else:
    pass
  
  if(len(foes) > 0) and (len(friends) >0) : 
   
    print(foes[0]["Name"],'has taken',foes[0]["DmgTaken"],'damage.',) #this line cannot handle and empty foes list

  else:
    print('\nThe battle is over')
    print('The dead:')
    for member in the_dead:
      print(member["Name"])
    


  command = input('press enter to continue or type \'x\'')
  if command == 'x':
    break
  else:
    pass