

class Monster:
    def __init__(self, name, size, type, level, role, hp, pd, ad, mig, agi, cha, int, reductions, resistances, vulnerabilities, immunities, skills, senses, languages, features, ap, rp, attack_bonus, save_dc, walk_speed, fly_speed, swim_speed, climb_speed, burrow_speed, actions, reactions, round_actions):
        self.name = name
        self.size = size
        self.type = type
        self.level = level
        self.role = role
        self.hp = hp
        self.pd = pd
        self.ad = ad
        self.mig = mig
        self.agi = agi
        self.cha = cha
        self.int = int
        self.reductions = reductions
        self.resistances = resistances
        self.vulnerabilities = vulnerabilities
        self.immunities = immunities
        self.skills = skills
        self.senses = senses
        self.languages = languages
        self.features = features
        self.ap = ap
        self.rp = rp
        self.attack_bonus = attack_bonus
        self.save_dc = save_dc
        self.walk_speed = walk_speed
        self.fly_speed = fly_speed
        self.swim_speed = swim_speed
        self.climb_speed = climb_speed
        self.burrow_speed = burrow_speed
        self.actions = actions
        self.reactions = reactions
        self.round_actions = round_actions
    

class Action:
    def __init__(self, name, description, damage, damage_type):
        self.name = name
        self.description = description
        self.damage = damage
        self.damage_type = damage_type