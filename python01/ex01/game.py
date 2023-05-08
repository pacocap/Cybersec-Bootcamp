# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    game.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: fcanadas <fcanadas@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/05/06 15:58:29 by fcanadas          #+#    #+#              #
#    Updated: 2023/05/08 11:39:09 by fcanadas         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class GoTCharacter:
	def __init__(self, first_name, is_alive):
		self.first_name = first_name
		self.is_alive = is_alive

class Stark(GoTCharacter):
	'''A class representing the Stark family. Or when bad things happen to good people.'''
	def __init__(self, first_name=None, is_alive=True):
		super().__init__(first_name=first_name, is_alive=is_alive)
		self.fam_name = 'Stark'
		self.house_words = 'Winter is Coming'

	def print_house_words(self):
		print(self.house_words)

	def die(self):
		self.is_alive = False

class Lannister(GoTCharacter):
	'''A class representing the Lannister family. Or when money takes over the world.'''
	def __init__(self, first_name=None, is_alive=True):
		super().__init__(first_name=first_name, is_alive=is_alive)
		self.fam_name = 'Lannister'
		self.house_words = 'Hear me roar'