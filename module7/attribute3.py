class Character:
    real = False

    def __init__(self, species, magic, age, weapon):
        self.species = species
        self.magic = age
        self.age = age
        self.weapon = weapon

legolas = Character("elf", False, 125, "bow")

print(f'the {legolas.species} legolas is {legolas.age} years old \
and using as weapon the {legolas.weapon} because {legolas.magic} magic')