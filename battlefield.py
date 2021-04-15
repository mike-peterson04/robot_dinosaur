from herd import Herd
from robotFleet import Fleet
import random


class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()
        self.dino_count = 0
        self.robo_count = 0
        self.fleet_health = 0
        self.herd_health = 0
        self.turn_arrow = ''
        for robo in self.fleet.robots:
            self.fleet_health += robo.health

        for dino in self.herd.dinos:
            self.herd_health += dino.health

    def run_game(self):
        self.fleet.create_fleet()
        self.herd.create_herd()
        self.display_welcome()
        coin = random.randint(1,2)

        if coin == 1:
            print("Coin flip came up heads it's the Dinosaur's turn")
            self.dino_turn(self.herd.dinos[self.dino_count])

        else:
            print("Coin flip came up Tails it's the Robots's turn")
            self.robo_turn(self.fleet.robots[self.robo_count])

        while self.fleet_health > 0 and self.herd_health > 0:

            if self.turn_arrow == 'dinos':
                print(f"It is the dinosaur's turn next")
                self.dino_turn(self.herd.dinos[self.dino_count])
            else:
                print("It is the Robot's turn next")
                self.robo_turn(self.fleet.robots[self.robo_count])
        self.display_winners()

    def display_welcome(self):
        print("Welcome, we will now have the opening coin flip. Dinosaurs go first on heads")


    def battle(self):
        self.fleet_health = 0
        self.herd_health = 0

        for robo in self.fleet.robots:
            self.fleet_health += robo.health

        for dino in self.herd.dinos:
            self.herd_health += dino.health

    def dino_turn(self, dinosaur):
        self.show_dino_opponent_options()
        dinosaur.attack(self.fleet.robots[int(input("What robot number do you wish to attack"))-1])
        if self.dino_count >= 2:
            self.dino_count = 0
        else:
            self.dino_count += 1
        self.battle()
        self.turn_arrow = "robots"

    def robo_turn(self, robot):
        self.show_robo_opponent_options()
        robot.attack(self.herd.dinos[int(input("What dinosaur number do you wish to attack")) - 1])
        if self.robo_count >=2:
            self.robo_count = 0
        else:
            self.robo_count += 1
        self.battle()
        self.turn_arrow = "dinos"

    def show_dino_opponent_options(self):
        i = 0
        for robo in self.fleet.robots:
            if robo.health > 0:
                print(f"Robot number {i+1} is armed with a {robo.weapon.type} and has {robo.health} remaining")
            i += 1

    def show_robo_opponent_options(self):
        i = 0
        for dino in self.herd.dinos:
            if dino.health > 0:
                print(f"dinosaur number {i + 1}  has {dino.health} remaining")
            i += 1

    def display_winners(self):
        if self.fleet_health > self.herd_health:
            print("The Robots won")
        else:
            print("The Dinosaurs won")


