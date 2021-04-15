from dinosaur import Dinosaur


class Herd:
    def __init__(self):
        self.dinos = []

    def create_herd(self):
        i = 0
        while i < 3:
            print(f"If Dinosaur {i+1} is a T-Rex press 1:")
            print(f"If Dinosaur {i+1} is a Triceratops press 2:")
            print(f"If Dinosaur {i+1} is a Stegosaurus press 3:")
            selector = {
                "1": "T-Rex",
                "2": "Triceratops",
                "3": "Stegosaurus"
            }
            self.dinos.append(Dinosaur(selector[input()], input(f"What is Dinosaur {i+1}'s Attack Power?")))
            i += 1
