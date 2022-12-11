#Juanito has other hobbies than his father
# so he changes the hobbies he inherited from his father

class Father:
    height = 170
    hair = "Negro"
    def walk(self):
        return "I'm walking"

    def hobby(self):
        return "read books"

class Son(Father):
    def hobby(self):
        return "read Manga"

juanito = Son()
print(juanito.hobby())