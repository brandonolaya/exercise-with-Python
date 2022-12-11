class Crap:
    faces = 6
    def __init__(self,color):
        self.color = color

mi_crap = Crap("oranje")
print(f'my crap is {mi_crap.faces} and it has {mi_crap.color} color')