#This will contain a function that gathers input
#to create a dictionary containing Cbnt name, main attack, and hp
combatants = [{
    "Name": "Brown Bear",
    "AC":11,
    "MainAttackMod":5,
    "MainAttackDmg":"1d8",
    "DmgMod":4,
    "HP": 34,
    "NumofAttacks":2,
    "DmgTaken":0,
    "Faction":"friends"
  },]
#delete all above


from tkinter import *





root = Tk()
root.title("Create Combatants")

#create the labels for user inputs
name_boxlabel = Label(root, text="Name", anchor = 'e')
ac_boxlabel = Label(root, text="Armor Class", anchor = 'e')
attkmod_boxlabel = Label(root, text="Attack Modifier", anchor = 'e')
dmg_boxlabel = Label(root, text="Damage Dice (xdy)", anchor = 'e')
hp_boxlabel = Label(root, text="Hit Points", anchor = 'e')
num_attacks_boxlabel = Label(root, text="Number of Attacks", anchor = 'e')
friend_boxlabel = Label(root, text="Friend", anchor = 'e')

#create input boxes
name_entry = Entry(root,width=20, borderwidth=3)
ac_entry = Entry(root,width=5, borderwidth=3,)
attkmon_entry = Entry(root, width=5, borderwidth=3)
dmg_entry = Entry(root, width = 5, borderwidth =3)
hp_entry = Entry(root, width=5, borderwidth=3)
numattacks_entry = Entry(root, width=5, borderwidth=3)

#create tick box
friend = IntVar()

friendly_check = Checkbutton(root, variable = friend)

#put labels on the screen
name_boxlabel.grid(row=0,column=0)
ac_boxlabel.grid(row=1,column=0)
attkmod_boxlabel.grid(row=2,column=0)
dmg_boxlabel.grid(row=3,column=0)
hp_boxlabel.grid(row=4,column=0)
num_attacks_boxlabel.grid(row=5,column=0)
friend_boxlabel.grid(row=6,column=0)

#put entry boxes on the screen
name_entry.grid(row=0,column=1,columnspan=2)
ac_entry.grid(row=1,column=1,columnspan=1)
attkmon_entry.grid(row=2,column=1,columnspan=1)
dmg_entry.grid(row=3,column=1,columnspan=1)
hp_entry.grid(row=4,column=1,columnspan=1)
numattacks_entry.grid(row=5,column=1,columnspan=1)

#put the checkbox on the screen
friendly_check.grid(row=6,column=1)

root.mainloop()