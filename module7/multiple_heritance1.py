#Manuela's parents work but now her daughter
# worked with her mother

class Father():
    def work(self):
        print("I work at the hospital")

    def reir(self):
        print("Ja ja ja!")

class Mother():
    def work(self):
        print("I work at the FBI")

class Hija(Mother, Father):
    pass

Manuela = Hija()
Manuela.work()