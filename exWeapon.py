class ExWeapon:
    def __init__(self, type):
        if type == "Sword":
            self.type = type
            self.durability = 30
            self.pref_terrain = 'Forest'
            self.bad_terrain = 'Field'
        elif type == "Rifle":
            self.type = type
            self.durability = 20
            self.pref_terrain = 'Field'
            self.bad_terrain = 'City'
        elif type == "Missile Pod":
            self.type = type
            self.durability = 10
            self.pref_terrain = 'City'
            self.bad_terrain = 'Forest'
        else:
            print(f'{type} is not a recognized weapon type robot will attack with fists until you re-arm')