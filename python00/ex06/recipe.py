# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: fcanadas <fcanadas@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/13 09:21:06 by fcanadas          #+#    #+#              #
#    Updated: 2023/04/24 18:46:10 by fcanadas         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

cookbook = {
	'sandwich' : {
	'ingredients': ['ham', 'bread', 'cheese', 'tomatoes'],
	'meal' : 'lunch',
	'prep_time' : '10 minutes'
	},

	'cake' : {
    'ingredients': ['flour', 'sugar', 'eggs'],
	'meal' : 'dessert',
	'prep_time' : '60 minutes'
	},

	'salad' : {
    'ingredients': ['avocado', 'arugula', 'tomatoes', 'spinach'],
	'meal' : 'lunch',
	'prep_time' : '15 minutes'
	},	
}

def get_recipe():
	print("".rjust(50,'_'), "\n")
	name = input("Write the name of your new recipe:\n")
	n_ing = int(input("Enter the number of ingredients:\n"))
	ingr = []
	for x in range(0, n_ing):
		elem_ing = input("Write an ingredient:\n")
		ingr.append(elem_ing)
	meal = input("Enter the type of meal. Ex: 'breakfast', 'lunch', 'snack':\n")
	prep_time = input("Enter the estimated preparation time, measured in minutes\n")
	prep_time = " ".join([prep_time, "minutes"])
	new_recipe = {'ingredients': ingr, 'meal': meal, 'prep_time': prep_time}
	cookbook[name] = new_recipe
	print("".rjust(50,'_'), "\n")

def remove_recipe():
	print("".rjust(50,'_'), '\n')
	option = input("Enter the recipe name to delete: ")
	del cookbook[option]
	print("".rjust(50,'_'), '\n')

def print_recipe(name):
	if name in cookbook:
		print("\n	Ingredients list: {}\n	To be eaten for {}.\n	Takes {} of cooking.\n".format(cookbook[name]['ingredients'], cookbook[name]['meal'], cookbook[name]['prep_time']))
	else:
		name = input ("Enter an existing recipe name from the cookbook to get its information: ")
		print_recipe(name)
			
def print_cookbook():
	print("".rjust(50,'_'), '\n')
	print("List of recipes:\n")
	for k in cookbook:
		print(k)
	print("".rjust(50,'_'), '\n')

if __name__=="__main__":
	print("\nWELCOME TO COOKBOOK.\n\nList of options:\n	1 Add a recipe\n	2 Remove a recipe\n	3 Print a recipe\n	4 Print the cookbook\n	5 Quit\n")
	try:
		while True:
				option = input("Please, select a valid option from the list: ")
				if not option.isdigit():
					continue
				option = int(option)
				if option == 1:
					get_recipe()
				elif option == 2:
					remove_recipe()
				elif option == 3:
					print("".rjust(50,'_'), '\n')
					name = input("Enter a recipe name from the cookbook to get its information: ")
					print_recipe(name)
					print("".rjust(50,'_'), '\n')
				elif option == 4:
					print_cookbook()
				elif option == 5:
					print("".rjust(50,'_'), '\n')
					print("Goodbye!\n")
					break
	except:
		print()
