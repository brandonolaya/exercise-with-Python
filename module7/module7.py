## programing POO


# class Pajaro:
#     pass

# mi_pajaro = Pajaro()
# print(type(mi_pajaro))



# class Pajaro:

#     ## esto quiere decir que todos los pajaron tiene pico
#     pico = True
#     ## este es el metodo contructor que asigna atributos a la clase
#     ## estos atributos pueden cambiar
#     def __init__(self, color, raza):
#         self.color = color
#         self.raza = raza



# mi_pajaro = Pajaro("verde", "Loro")
# mierda = "caca"
# ## se usa para buscar las propiedades de nuestro metodo
# print(f'mi pajaro es un {mi_pajaro.raza} es de color {mi_pajaro.color}')
# print(f'Los pajarons tiene pico? {Pajaro.pico}')
# print(f'Mi {mi_pajaro.raza} tiene pico? {mi_pajaro.pico}')



# class Pajaro:
#     alas= True
#     def __init__(self, color, raza):
#         self.color = color
#         self.raza = raza

#     def caminar(self):
#         print(f'camino el pajaro de color {self.color}')

#     def volar(self, metros):
#         print(f'el pajaro ha volado {metros} metros')

# el_loro = Pajaro("negro", "loro")

# el_loro.caminar()
# el_loro.volar(15)


#############################################################
#decoradores

# metodos de instancia son los anteriores
# acceder y modifican atributos
# accede a otros metodos
# modifican el estado de la clase


# metodos de clase @classmethod
# pueden modificar los atributos de una clase
# se decaran con un decorador "@"

# metodos estaticos @staticmethod
# es util para idicar que no se modificil el metodo de la clase





# # class Pajaro:
# #     alas= True
# #     def __init__(self, color, raza):
# #         self.color = color
# #         self.raza = raza

# #     def caminar(self):
# #         print(f'camino el pajaro de color {self.color}')

# #     def volar(self, metros):
# #         """"los metodos acceden a otros metodos
# #         """
# #         print(f'el pajaro ha volado {metros} metros')
# #         self.caminar()

# #     def to_paint_white(self):
# #         self.color = "blanco"
# #         print(f'el pajaro a hora es {self.color}')

# #     @classmethod
# #     no necesitan una instacia para poder ejecutarcen, los de sel si deben llarsen para ejecutarsen
# #     no permite poner self
# #     deja tomar a los de clase pero no a los de instancia
# #     def comer_gusanos(cls, cantidad):
# #         self.cantidad = cantidad
# #         print(f'se comido {cantidad} gusanos')
# #         cls.alas = False
# #         print(Pajaro.alas)

# #     @staticmethod
# #     # no se relacio con las instacias no pertime el self
# #     # estos metodos no puende acceder a la clase ni a los atributos de ella
# #     # se usan para que ciertos metodos no modifiquen las instancias
# #     def cagar():
# #         print("El pajaro se cago feo")

# # el_loro = Pajaro("negro", "loro")

# # el_loro.caminar()
# # el_loro.volar(15)
# # el_loro.to_paint_white()
# # el_loro.volar(23)
# # el_loro.alas = False
# # print(el_loro.alas, "\n")

# # Pajaro.comer_gusanos(6)
# # Pajaro.caminar()



############################################################################
#3Herencia

# class Padre:
#     def respirar():
#         pass

# class Hijo(Padre):
#     pass

# class Hija(Padre):
#     pass
# #Para ver quien hereda
# print(Hijo.__base__)
# #Para saver a quien le transmite su herencia
# print(Padre.__subclasses__())





# class Padre:
#     def __init__(self, color, edad):
#         self.edad = edad
#         self.color = color


#     def respirar(self):
#         print("me gusta respirar")

# class Hijo(Padre):
#     pass

# class Hija(Padre):
#     pass

# valentin = Padre("verde", 54)
# brandon = Hijo("negro", 26)
# brandon.respirar()
# valentin.respirar()
# print(f'el color de valentin es {valentin.color}')




#############################################################
##Heredar extendida
## metodos Herdados = pueden heredar exactamente todos los metodos
## metodos modificador = herreda el metodo pero se modifica luego
## metodos nuevos = metodos que no tiene la clase padre



# class Animal:
#     def __init__(self, color, raza):
#         self.color = color
#         self.raza = raza

#     def nacer(self):
#         print("Nacio")

#     def murio(self):
#         print("Se murio")

# class Perro(Animal):
#     def __init__(self, color, raza, correr):
#         super().__init__(color,raza) ## con super herreda lo anteriro y no hay que construirla
#         # self.color = color
#         # self.raza = raza
#         self.correr = correr # solo se contrulle lo nuevo

#     def nacer(self):
#         print("Este perro Nacio")

#     def correr(self, metros):
#         print(f'El perro corrio {metros} metros')

# guffy = Perro("cafe", "chanda", 250)
# lorenzo = Animal() #solo pide los parametros de la calse animal no tien acceso a mas metodos
# chandosqui = Perro()# tiene nuevos parametrs y se puede acceder a otros metodos dentro de las dos clases


# guffy.nacer() ## tipo de metodo heradado pero modificado
# guffy.correr(2050)
# guffy.murio()




################################################
### Herencia multiple


# class Madre:
#     def ama(self):
#         print("ella te ama")

#     def hablar(selft):
#         print("Chao")
# class Padre:
#     def hablar(self):
#         print("Hola")

# class Hijo(Madre, Padre):## Si hay dos metodos con el mismo nombre tomara el que primero se herede
#     pass

# class Nieto(Hijo):
#     pass

# fernando = Nieto()

# fernando.hablar()
# fernando.ama()
# print(Nieto.__mro__)## para ver el orden de las clases




##########################################
##Polimorfismos, hace que los objetos tengar diferentes formas

class Vaca:

    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + " Muuu...")


class Oveja:

    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + " Beee...")


mi_vaca = Vaca("Nicole")
mi_Oveja = Oveja("Clara")
##dos objetos de formas distintas ejecutan metodos con el mismo nombre
# mi_vaca.hablar()
# mi_Oveja.hablar()

animales = [mi_vaca,mi_Oveja]
for animal in animales: ## en una iteracion llamo a los objetos de formas distintaa
    animal.hablar() ##pero ejecutan el mismo metodos


def animal_habla(animal):
    animal.hablar()

animal_habla(mi_vaca)
animal_habla(mi_Oveja)