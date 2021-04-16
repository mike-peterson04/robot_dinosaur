from exWeapon import ExWeapon
class ExRobot:
    def __init__(self, name):

        if name != "dead":
            print(f"Press 1 to equip robot /w a Sword")
            print(f"Press 2 to equip robot /w a Rifle")
            print(f"Press 3 to equip robot /w a Missile Pod")
            selector = {
                "1": "Sword",
                "2": "Rifle",
                "3": "Missile Pod",
                "4": "No Weapon"
            }
            self.weapon = ExWeapon(selector[input()])
        self.name = name
        self.power_level = 500
        self.health = 1000
        self.base_attack = 100

    def attack(self, dinosaur, terrain):
        temp_attack = self.base_attack
        if terrain == self.weapon.pref_terrain:
            temp_attack *= 5
        elif terrain == self.weapon.bad_terrain:
            temp_attack -= 50

        if self.health <= 0:
            print(f'{self.name} is out of health and is unable to attack')

        elif self.power_level <= 0:
            print(f'{self.name} is out of health and is unable to attack')

        else:
            self.power_level -= 10
            dinosaur.health -= temp_attack
            if dinosaur.health <=0:
                dinosaur.health = 0
                print("Your target has died")
