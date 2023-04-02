from collections import namedtuple

Persona = namedtuple('persona', ["name", "tall", "weight"])
brandon = Persona('Brandon', 1.70, 86)

print(brandon[2]) #forma clasica
print(brandon.tall) #forma de busqueda