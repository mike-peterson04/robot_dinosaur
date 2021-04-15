from robot import Robot
from robotFleet import RobotFleet
from weapon import Weapon
def test_method():
    rob = Robot(Weapon("Missle_Pod"), "R.O.B")
    data = Robot(Weapon("Rifle"), "Data")
    twob = Robot(Weapon("Sword"), "2B")
    machine_overlord = RobotFleet([rob, data, twob])



if __name__ == '__main__':
    test_method()
