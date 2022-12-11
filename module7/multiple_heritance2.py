class Animal:
    eat = True

class Brid(Animal):
    fly = True

class Reptile(Animal):
    paison = True

class Mammal(Animal):
    def walk(self):
        print("I'm walk")

class Chimera(Mammal, Reptile, Brid):
    pass

chimerita = Chimera()

print(f'La chimerita puede volar = {chimerita.fly}')
print(f'La chimerita estaminando?? ')
chimerita.walk()