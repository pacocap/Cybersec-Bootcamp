# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    book.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: fcanadas <fcanadas@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/05/03 12:36:58 by fcanadas          #+#    #+#              #
#    Updated: 2023/05/08 12:46:02 by fcanadas         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from datetime import datetime as d
from recipe import Recipe

class Book:
    
	def __init__(self, name:str, last_up:d, crea_date:d, rec_dic:dict):
		self.name = name
		self.last_up = last_up
		self.crea_date = crea_date
		self.rec_dic = rec_dic
	
	# BOOK NAME (str)
	@property
	def name(self):
		return self._name
	@name.setter
	def name (self, value):
		try:
			self._name = str(value)
		except ValueError:
			raise ValueError('The name of the book must be a string')
	
	# LAST UPDATE (d.datetime)
	@property
	def last_up(self):
		return self._last_up
	@last_up.setter
	def last_up(self, value):
		self._last_up = value
		if not isinstance(self._last_up, d):
			raise TypeError('The last update time must be in a valid date format')
	
	# CREATION DATE (d.datetime)
	@property
	def crea_date(self):
		return self._crea_date
	@crea_date.setter
	def crea_date(self, value):
		self._crea_date = value
		if not isinstance(self._crea_date, d):
			raise TypeError('The creation date must be in a valid date format')

	# RECIPE LIST (Recipe dictionary)
	@property
	def rec_dic(self):
		return self._rec_dic
	@rec_dic.setter
	def rec_dic(self, value):
		try:
			self._rec_dic = dict(value)
		except TypeError:
			raise TypeError('The recipe list must be a dictionary')
	
	# PRINTS A RECIPE AND RETURNS THE INSTANCE
	def get_recipe_by_name(self, name:str):
		if not isinstance(name, str):
			raise TypeError('ERROR: Name must be a string')
		if name in self._rec_dic:
			print (str(self._rec_dic[name]), '\n')
			return (self._rec_dic[name])
		print('Name provided not found. Please, try again.')

	# GET ALL RECIPE NAMES FOR A GIVEN REC_TYPE (just return)
	def get_recipes_by_type(self, rec_type:str):
		if not isinstance(rec_type, str):
			raise TypeError('ERROR: Recipe type must be a string')
		try:
			ret_recs = list()
			for rec in self._rec_dic:
				if self._rec_dic[rec].rec_type == rec_type:
					ret_recs.append(self._rec_dic[rec].name)
			return ret_recs
		except ValueError:
			raise ValueError('Type provided not found. Please, try again.')


	# ADD A RECIPE TO THE BOOK AND UPDATE last_up IN THE CLASS
	def add_recipe(self, recipe:Recipe):
		if not isinstance(recipe, Recipe):
			raise TypeError('ERROR: Recipe to add must be an object of the type Recipe')
		try:
			self._rec_dic.update({recipe.name: recipe})
			self._last_up = d.now()
		except ValueError:
			raise ValueError('Recipe could not be added. Please, try again.')