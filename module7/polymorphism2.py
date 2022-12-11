class Mage:
    def attack(self):
        print("Fire ball")

class Goalkeeper:
    def attack(self):
        print("Green arrow")

class Swordsman:
    def attack(self):
        print("sword strike")

merlin = Mage()
legolas = Goalkeeper()
frodo = Swordsman()
characters = [legolas, merlin, frodo]

for character in characters:
    character.attack()