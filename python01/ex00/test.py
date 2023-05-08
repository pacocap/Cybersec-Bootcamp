# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: fcanadas <fcanadas@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/05/03 12:37:03 by fcanadas          #+#    #+#              #
#    Updated: 2023/05/08 12:46:09 by fcanadas         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from datetime import datetime as d
from recipe import Recipe
from book import Book

if __name__=="__main__":
	# try:	
	# 	name = input('Type the name of the recipe:\n')
	# 	ck_lv = input('Type the difficulty level: ')
	# 	ck_time = input('Type a cooking time (expressed in minutes): ')
	# 	ingrs = list()
	# 	print('Type the ingredients, one by one:')
	# 	while True:
	# 		value = input()
	# 		if value == '':
	# 			break
	# 		ingrs.append(value)
	# 	rec_type = input('Indicate the recipe type: "starter", "lunch", "dessert":\n')
	# 	descr = input('Provide a description for the recipe:\n')
	# except:
	# 	print ('\nERROR: Some input not valid.\n')
	# else:
	# 	try:
	# 		recipe = Recipe(name, ck_lv, ck_time, ingrs, descr, rec_type)
	# 		print(str(recipe))
	# 	except ValueError:
	# 		print('New recipe could not be initialized. \n\n{use}\n'.format(use=Recipe.usage))

	try:
		recipe = Recipe('Cocido', 3, 45, ['garbanzos', 'patatas', 'apio', 'pollo'], 'Un cocido', 'lunch')
		recipe2 = Recipe('Bravas', 3, 45, ['patatas', 'salsa'], 'Las bravillas', 'lunch')
		recipe3 = Recipe('Tarta', 3, 45, ['galleta', 'mantequilla', 'huevo', 'azúcar'], 'Tartica', 'dessert')
		dictionary = {'cocido' : recipe}
		book = Book('Libro', d.now(), d.now(), dictionary)
		# print (str(recipe))
		# recipe2 = book.get_recipe_by_name('Cocido')
		# all_lunches = book.get_recipes_by_type('lunch')
		# print (str(recipe2))
		print(book.crea_date)
		print(book.last_up)
		print (book._rec_dic, '\n')
		book.add_recipe(recipe)
		print(book.crea_date)
		print(book.last_up)
		print(book._rec_dic, '\n')
		book.add_recipe(recipe2)
		print(book.crea_date)
		print(book.last_up)
		print(book._rec_dic, '\n')
		book.add_recipe(recipe3)
		print(book.crea_date)
		print(book.last_up)
		print(book._rec_dic, '\n')
		recipeT = book.get_recipe_by_name('Bravas')
		recipeT = book.get_recipe_by_name('Tarta')
		recipeT = book.get_recipes_by_type('dessert')
		print(recipeT)
		recipeT = book.get_recipes_by_type('lunch')
		print(recipeT)
		recipeT = book.get_recipes_by_type('pene')
		print(recipeT)

	except:
		print('NO')
