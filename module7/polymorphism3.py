#from a function make each animal execute its bite function
class Dog:
    def to_bite(self):
        print("The dog to bite")

class Cat:
    def to_bite(self):
        print("The cat to bite")

class Shark:
    def to_bite(self):
        print("The shark to bite")

def animal_bite(bite):
    bite.to_bite()

mirringo = Dog()
michi = Cat()
pakas = Shark()

animal_bite(mirringo)
animal_bite(michi)
animal_bite(pakas)