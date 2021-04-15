class Weapon:
    def __init__(self, type, attack_power):
        if type == "Sword":
            self.type = type
            self.attack_power = int(attack_power)
        elif type == "Rifle":
            self.type = type
            self.attack_power = int(attack_power)
        elif type == "Missile Pod":
            self.type = type
            self.attack_power = int(attack_power)
        else:
            self.type = ''
            self.attack_power = 0
            print('Robot will attack with fists until you re-arm')
        # Code prior to UML doc
        # if type == "Sword":
        #     self.type = type
        #     self.durability = 300
        #     self.pref_terrain = 'Forest'
        #     self.bad_terrain = 'Field'
        # elif type == "Rifle":
        #     self.type = type
        #     self.durability = 200
        #     self.pref_terrain = 'Field'
        #     self.bad_terrain = 'City'
        # elif type == "Missile Pod":
        #     self.type = type
        #     self.durability = 100
        #     self.pref_terrain = 'City'
        #     self.bad_terrain = 'Forest'
        # else:
        #     print(f'{type} is not a recognized weapon type robot will attack with fists until you re-arm')