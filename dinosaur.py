class Dinosaur:
    def __init__(self, species, atp):
        self.type = species
        self.health = 1000
        self.energy = 500
        self.attack_power = int(atp)
        self.attacks = ("Bite", "Charge", "Tail-Whip")

    def attack(self, robot):
        if self.health <= 0:
            print(f'{self.type} is out of health and is unable to attack')

        elif self.energy <= 0:
            print(f'{self.type} is out of energy and is unable to attack')

        else:
            print(f"press 1 to attack with a {self.attacks[0]}")
            print(f"press 2 to attack with a {self.attacks[1]}")
            print(f"press 3 to attack with a {self.attacks[2]}")
            attack_type = self.attacks[int(input())-1]
            self.energy -= 10
            robot.health -= self.attack_power
            if attack_type == self.attacks[0]:
                print(f"The {self.type} bites the robot for massive damage")
            elif attack_type == self.attacks[1]:
                print(f"The {self.type} charges the robot for critical damage")
            else:
                print(f"The {self.type} smacks the target with it's tail")
            if robot.health <= 0:
                robot.health = 0
                print("Your target has died")
