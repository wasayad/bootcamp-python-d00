import sys
import re

cookbook = {'sandwich':
            {'ingredients': 'ham, bread, cheese and tomatoes',
                'meal': 'lunch',
                'prep_time': '10 minutes'},
            'cake': {'ingredients': 'flour, sugar and eggs',
                     'meal': 'dessert',
                     'prep_time': '60 minutes'},
            'salad':
            {'ingredients': 'avocado, arugula, tomatoes and spinach',
             'meal': 'lunch',
             'prep_time': '15 minutes'}
            }


def get_recipe(s):
    if string in cookbook:
        print("Ingredients :", cookbook[s]['ingredients'], "\nMeal :", end='')
        print(cookbook[s]['meal'], "\nPrep_time :", cookbook[s]['prep_time'])
    else:
        print("Error there's no", string, "recipe.")


def del_recipe(string):
    if (string in cookbook):
        del cookbook[string]
    else:
        print("Error there's no", string, "recipe.")


def add_recipe(s, ing, me, prep):
    if s in cookbook:
        print("Error there's already a", s, "recipe.")
    else:
        cookbook[s] = {'ingredients': ing,
                       'meal': me, 'prep_time': prep}


def get_all_recipe():
    string = list(cookbook)
    string = '\n'.join(string)
    print("Recipe of cookbook are :")
    print(string)


while 1:
    print("Please select an option by typing the corresponding number:")
    print("1: Add a recipe")
    print("2: Delete a recipe")
    print("3: Print a recipe")
    print("4: Print the cookbook")
    print("5: Quit")
    choice = input()
    if choice not in "12345":
        print("This option does not exist, please type the correct it.")
        print("To exit enter 5.")
    elif int(choice) is 1:
        print("Please write the recipe you wanna add:", end='')
        toadd = input()
        print("Please write the ingredients:", end='')
        ing = input()
        print("Please write the type of meal:", end='')
        me = input()
        print("Please write the time of preparation:", end='')
        prep = input()
        add_recipe(toadd, ing, me, prep)
    elif int(choice) is 2:
        print("Please write the recipe you wanna delete:", end='')
        todel = input()
        del_recipe(todel)
    elif int(choice) is 3:
        print("Please write the recipe you wanna read:", end='')
        toread = input()
        get_recipe(toread)
    elif int(choice) is 4:
        get_all_recipe()
    elif int(choice) is 5:
        exit()
