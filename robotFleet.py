class RobotFleet:
    def __init__(self, robots=[]):
        self.robots = robots
    def recruitment(self, robot):
        self.robots.append(robot)
