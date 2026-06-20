import csv
from classes import Trait

def load_hp(level,role,tier,traits):
    hp = 0
    with open('tables/monster_statistics.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Level'] == level or row['Level'] == -1 and level == 'Novice':
                hp = int(row['Average HP'])
                break
    with open('tables/monster_role.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Role'] == role:
                hp *= (1 + float(row['HP Modifier'].strip('%'))/100)
                break
    if tier == 'Epic':
        hp *= 2
    elif tier == 'Legendary':
        hp *= 4
    elif tier == 'Minion':
        hp /= 2
    hp_modifier = 0
    for trait in traits:
        
        if 'HP' in trait.name:
            hp_modifier += trait.bonus
    hp *= (1 + hp_modifier/100)
    return hp