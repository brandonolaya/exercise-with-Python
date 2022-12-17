from pathlib import Path
from os import system
import os


def file_counter(rute):
    """This function is responsible for counting the .txt files
    that is saved, and back the sum of the files found
    """
    counter = 0
    for txt in Path(rute).glob("**/*.txt"): ## busca en todoas las carpetas y dentro de ellas lso archivos txt
        counter += 1
    return counter


def info_rutes():
    """This function is reponsible of te rute at categories, and return rute
    """
                #se puede cambiar por Path.home para que funciones en cualquier pc
    base = Path("C:\\Users\\bvola\\OneDrive\\Documents\\python\\exercise_python\\module6\\","recipes")
    return base


def show_categories(rute):
    """This function show the categories that has been created
    and return a list of category names
    """
    system("cls")
    rute_categories = Path(rute)
    list_categories = []
    counter = 1
    for floder in rute_categories.iterdir():
        floder_str = str(floder.name)
        if floder_str == "main.py":
            continue
        print(f'[{counter}] - {floder_str}')
        list_categories.append(floder)
        counter += 1
    return list_categories


def choose_categories(lista):
    """This function is for choose a category
    and return only name of the category
    """
    choose_true = "x"

    while not choose_true.isnumeric() or int(choose_true) not in range(1, len(lista) + 1):
        choose_true = input("\nChoose a categories: ")
    return lista[int(choose_true) - 1]


def show_recipe(rute):
    """This function is for show the recipe name
    and return a list the all recipe name
    """
    print("Recipes:")
    rute_recipes = Path(rute)
    list_recipes = []
    counter = 1

    for recipe in rute_recipes.glob('*.txt'):
        recipe_str = str(recipe.name)
        print(f'[{counter}] - {recipe_str}')
        list_recipes.append(recipe)
        counter += 1
    return list_recipes


def choose_recipe(lista):
    """This function is for choose a recipe
    and return only name of the recipe
    """
    choose_true = "x"

    while not choose_true.isnumeric() or int(choose_true) not in range(1, len(lista) + 1):
        choose_true = input("\nChoose a recipe: ")
    return lista[int(choose_true) - 1]


def read_recipe(recipe):
    """This function read the contents of the recipe
    """
    print(Path.read_text(recipe))
    print("\n")


def create_recipe(rute):
    """This function create file assigns it a name and it is content
    and identifies it something with that name has already been created
    """
    exists = False

    while not exists:
        print("Write the name of your recipe: ")
        name_recipe = input() + ".txt"
        print("Write content your new recipe: ")
        contents_recipe = input()
        rute_new = Path(rute, name_recipe)

        if not os.path.exists(rute_new):
            Path.write_text(rute_new, contents_recipe)
            print(f' Your recipe {name_recipe} has been created\n')
            exists = True
        else:
            print("The name of recipe, it already exists")


def create_category(rute):
    """This function create floder assigns it a name
    and identifies it something with that name has already been created
    """
    exists = False

    while not exists:
        print("Write the name of your category: ")
        name_category = input()
        rute_new = Path(rute, name_category)

        if not os.path.exists(rute_new):
            Path.mkdir(rute_new)
            print(f' Your new category {name_category} has been created\n')
            exists = True
        else:
            print("The name of category, it already exists")


def delete_category(category):
    """This function delete a category that has been created
    """
    try:
        Path(category).rmdir()
        print(f'The category {category.name} has been deleted')
    except OSError as error:
        print("has a files\n")


def delete_recipe(recipe):
    """This function delete a recipe that has been created
    """
    Path(recipe).unlink()
    print(f'The recipe {recipe.name} has been deleted')


def menu1():
    """only show the option of the program
    """
    print("""This is a menu for recipes
    [1] - Read recipe
    [2] - Create a new recipe
    [3] - Create a new category
    [4] - Delete recipe
    [5] - Delete category
    [6] - Finish program
    """)


def user_menu():
    """This function, call a funtions depending an of each case that applies
    """
    start = True
    while start:
        menu1() 
        menu = input("numero: ")
        match menu:
            case "1":
                list_categories = show_categories(info_rutes()) # para optener las categorias y las pasa en una lsita
                my_category = choose_categories(list_categories) # sabe las carpetas, para elegir una
                my_recipes = show_recipe(my_category) # permite ver los archivos que hay en la carpeta
                my_recipe = choose_recipe(my_recipes) # permite elegir el archivo de la carpeta
                read_recipe(my_recipe) # mustra el contenido del txt
            case "2":
                list_categories = show_categories(info_rutes())
                my_category = choose_categories(list_categories)
                create_recipe(my_category) # crea un archivo para la carpeta elegida
            case "3":
                create_category(info_rutes()) # crea una carpeta
            case "4":
                list_categories = show_categories(info_rutes())
                my_category = choose_categories(list_categories) # muestra las carpetas
                my_recipes = show_recipe(my_category) # muestra los archivos dentro de la carpeta
                my_recipe = choose_recipe(my_recipes) # elije un archivo
                delete_recipe(my_recipe) # borra un archivo
            case "5":
                list_categories = show_categories(info_rutes())
                my_category = choose_categories(list_categories)
                delete_category(my_category)
            case "6":
                start = False
            case _:
                system("cls")
                print(f"It is not understood {name}\n")


if __name__ == '__main__':
    name = input("Cual es tu nombre: ").title()
    system("cls")
    print("*" * 51)
    print(f'{"*" * 17} Welcome {name} {"*" * 17}')
    print("*" * 51, "\n")

    print(f'the recipes are in the rute: {info_rutes()}')## solo muestra la ruta
    print(f'total recipes: {file_counter(info_rutes())}')## llama la funcion y le pasa la ruta
    user_menu() ## inicia con el menu
