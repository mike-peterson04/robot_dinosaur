from exBattlefield import ExBattlefield
from battlefield import Battlefield


def test_method():
    i = game_selection()
    if i != "base":
        test_two = ExBattlefield()
        test_two.run_game()
    else:
        forest_planet = Battlefield()
        forest_planet.run_game()


def game_selection():
    print("Press 1 to run the game as assigned")
    print("Press 2 to run the game with expanded rules")
    selector = {
        "1": "base",
        "2": "ex"
    }
    return selector[input("Which game mode do you choose")]


if __name__ == '__main__':
    test_method()
