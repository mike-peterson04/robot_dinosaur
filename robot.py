from weapon import Weapon
class Robot:
    def __init__(self, name):
        print(f"Press 1 to equip robot /w a Sword")
        print(f"Press 2 to equip robot /w a Rifle")
        print(f"Press 3 to equip robot /w a Missile Pod")
        selector = {
            "1": "Sword",
            "2": "Rifle",
            "3": "Missile Pod",
            "4": "No Weapon"
        }
        self.weapon = Weapon(selector[input()],input("What is the attack power of this robot's weapon?"))
        self.name = name
        self.power_level = 500
        self.health = 1000
    def attack(self,dinosaur):
        if self.health <= 0:
            print(f'{self.name} is out of health and is unable to attack')

        elif self.power_level <= 0:
            print(f'{self.name} is out of health and is unable to attack')

        else:
            self.power_level -= 10
            dinosaur.health -= self.weapon.attack_power
            if dinosaur.health <=0:
                print("Your target has died")
                