from exRobot import ExRobot


class ExFleet:
    def __init__(self):
        self.robots = []

    def create_fleet(self):
        i = 0
        while i < 3:
            self.robots.append(ExRobot(input(f'Please name Robot {i+1} ')))
            i += 1

    def abandon_dead(self):
        i = 0
        while i < len(self.robots):
            if self.robots[i].health <= 0 or self.robots[i].power_level <= 0:
                print("A robot is no longer able to battle removing it from the fleet")
                self.robots.pop(i)
            i += 1
        if len(self.robots) == 0:
            self.robots.append(ExRobot("dead"))
            self.robots[0].health = 0

