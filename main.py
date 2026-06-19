from tkinter import *
import pandas as pd

creatureTypes = ['Aberration','Beast', 'Celestial', 'Construct', 'Dragon', 'Elemental', 'Fey', 'Fiend','Giant', 'Humanoid', 'Monstrosity', 'Ooze', 'Plant', 'Undead']
damageTypes = ['Bludgeoning', 'Cold', 'Corrosion', 'Fire', 'Lightning', 'Piercing', 'Poison', 'Psychic', 'Radiant', 'Slashing', 'True', 'Umbral']
creatureSizes = ['Micro', 'Tiny', 'Small', 'Medium', 'Large', 'Huge', 'Gargantuan', 'Colossal', 'Titanic']
monsterLevels = ['Novice'] + [str(i) for i in range(0, 21)]
monsterRoles = ['Brute', 'Defender', 'Leader', 'Soldier', 'Striker', 'Tactician']
monsterTiers = ['Minion', 'Standard', 'Epic', 'Legendary']

parent = Tk()
parent.title("DC20 Monster Statblock creator")
monsterInfoFrame = Frame(parent)
monsterNameFrame = Frame(monsterInfoFrame)
monsterNameLabel = Label(monsterNameFrame, text="Name:")
monsterNameEntry = Entry(monsterNameFrame, borderwidth=2, relief="solid")
monsterNameLabel.grid(row=0, column=0, sticky='w')
monsterNameEntry.grid(row=1, column=0, sticky='w')
monsterNameFrame.grid(row=0, column=0, sticky='w', padx=20, pady=5)
monsterTypeFrame = Frame(monsterInfoFrame)
monsterTypeLabel = Label(monsterTypeFrame, text="Type:")
monsterTypeOption = StringVar(monsterTypeFrame)
monsterTypeOption.set(creatureTypes[0])
monsterTypeMenu = OptionMenu(monsterTypeFrame, monsterTypeOption, *creatureTypes)
monsterTypeLabel.grid(row=0, column=0, sticky='w')
monsterTypeMenu.grid(row=1, column=0, sticky='w')
monsterTypeFrame.grid(row=0, column=1, sticky='w', padx=20, pady=5)
monsterSizeFrame = Frame(monsterInfoFrame)
monsterSizeLabel = Label(monsterSizeFrame, text="Size:")
monsterSizeOption = StringVar(monsterSizeFrame)
monsterSizeOption.set(creatureSizes[0])
monsterSizeMenu = OptionMenu(monsterSizeFrame, monsterSizeOption, *creatureSizes)
monsterSizeLabel.grid(row=0, column=0, sticky='w')
monsterSizeMenu.grid(row=1, column=0, sticky='w')
monsterSizeFrame.grid(row=0, column=2, sticky='w', padx=20, pady=5)
monsterLevelFrame = Frame(monsterInfoFrame)
monsterLevelLabel = Label(monsterLevelFrame, text="Level:")
monsterLevelOption = StringVar(monsterLevelFrame)
monsterLevelOption.set(monsterLevels[0])
monsterLevelMenu = OptionMenu(monsterLevelFrame, monsterLevelOption, *monsterLevels)
monsterLevelLabel.grid(row=0, column=0, sticky='w')
monsterLevelMenu.grid(row=1, column=0, sticky='w')
monsterLevelFrame.grid(row=0, column=3, sticky='w', padx=20, pady=5)
monsterTierFrame = Frame(monsterInfoFrame)
monsterTierLabel = Label(monsterTierFrame, text="Tier:")
monsterTierOption = StringVar(monsterTierFrame)
monsterTierOption.set(monsterTiers[0])
monsterTierMenu = OptionMenu(monsterTierFrame, monsterTierOption, *monsterTiers)
monsterTierLabel.grid(row=0, column=0, sticky='w')
monsterTierMenu.grid(row=1, column=0, sticky='w')
monsterTierFrame.grid(row=0, column=4, sticky='w', padx=20, pady=5)
monsterRoleFrame = Frame(monsterInfoFrame)
monsterRoleLabel = Label(monsterRoleFrame, text="Role:")
monsterRoleOption = StringVar(monsterRoleFrame)
monsterRoleOption.set(monsterRoles[0])
monsterRoleMenu = OptionMenu(monsterRoleFrame, monsterRoleOption, *monsterRoles)
monsterRoleLabel.grid(row=0, column=0, sticky='w')
monsterRoleMenu.grid(row=1, column=0, sticky='w')
monsterRoleFrame.grid(row=0, column=5, sticky='w', padx=20, pady=5)
monsterInfoFrame.grid(row=0, column=0, sticky='w')
parent.mainloop()

#default stats are 3/2/0/0