# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    count.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: fcanadas <fcanadas@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/11 17:14:37 by fcanadas          #+#    #+#              #
#    Updated: 2023/04/15 12:18:16 by fcanadas         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys, string

def text_analyzer(*args):
	'''\n	This function counts the number of upper characters,
	lower characters, punctuation and spaces in a given text.'''
	args = list(args)
	if (len(args) > 0):
		str = args[0]
	if (isinstance(str, int)):
		print("AssertionError: argument is not a string")
	else:
		up, low, pun, spa, tot = 0, 0, 0, 0, 0
		for char in str:
			if (char.isupper()):
				up += 1
			elif (char.islower()):
				low += 1
			elif (char in string.punctuation):
				pun += 1
			elif (char.isspace()):
				spa += 1
			tot += 1
		print("The text contains {} character(s):\n- {} upper letter(s)\n- {} lower letter(s)\n- {} punctuation mark(s)\n- {} space(s)".format(tot, up, low, pun, spa))

if __name__=="__main__":
	if (len(sys.argv) > 2):
		quit(print("Error: Please provide only one argument"))
	elif (len(sys.argv) == 2):
		text_analyzer(sys.argv[1])
	else:
		try:
			text_analyzer(input("Please, provide a string:\n"))
		except:
			quit