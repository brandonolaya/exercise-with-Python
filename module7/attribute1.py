class House:
    def __init__(self, color, floors):
        self.color = color
        self.floors = floors

mi_house = House("white", "3")
print(f'my house is {mi_house.color} and it has {mi_house.floors} floors')