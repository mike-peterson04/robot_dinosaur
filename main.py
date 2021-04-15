from robot import Robot
from robotFleet import Fleet
from weapon import Weapon
def test_method():

    machine_overlord = Fleet()
    machine_overlord.create_fleet()
    print(machine_overlord)


def weapon_selection():
    print("Press 1 to equip your robot /w a Sword")
    print("Press 2 to equip your robot /w a Rifle")
    print("Press 3 to equip your robot /w a Missile Pod")
    selector = {
        "1": "Sword",
        "2": "Rifle",
        "3": "Missile Pod"
    }
    return selector[input("Which weapon do you choose")]


if __name__ == '__main__':
    test_method()
