from exDino import ExDinosaur


class ExHerd:
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
            self.dinos.append(ExDinosaur(selector[input()]))
            i += 1
    def abandon_dead(self):
        i = 0
        while i < len(self.dinos):
            if self.dinos[i].health <= 0 or self.dinos[i].energy <= 0:
                print("A dinosaur is no longer able to battle removing it from the herd")
                self.dinos.pop(i)
            i += 1
        if len(self.dinos) == 0:
            self.dinos.append(ExDinosaur("T-Rex"))
            self.dinos[0].health = 0

