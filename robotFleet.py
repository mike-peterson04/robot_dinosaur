class RobotFleet:
    def __init__(self, robots=[]):
        self.robots = robots
        self.health = 0
        for x in robots:
            self.health += x.life
    def recruitment(self, robot):
        self.robots.append(robot)

    def check_health(self):
        return self.health
