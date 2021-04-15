class Dinosaur:
    def __init__(self, species, atp):
        self.type = species
        self.health = 1000
        self.energy = 500
        self.attack_power = int(atp)

    def attack(self, robot):
        if self.health <= 0:
            print(f'{self.type} is out of health and is unable to attack')

        elif self.energy <= 0:
            print(f'{self.type} is out of energy and is unable to attack')

        else:
            self.energy -= 10
            robot.health -= self.attack_power
            if robot.health <= 0:
                print("Your target has died")
