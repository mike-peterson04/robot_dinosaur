from robot import Robot
class Fleet:
    def __init__(self):
        self.robots = []

    def create_fleet(self):
        i = 0
        while i < 3:
            self.robots.append(Robot(input(f'do you want a Sword, Rifle, or Missile Pod for Robot {i} (please type exactly as seen)'),input(f'Please name Robot {i} ')))
            i+=1

