# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    whois.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: fcanadas <fcanadas@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/11 16:32:52 by fcanadas          #+#    #+#              #
#    Updated: 2023/04/11 17:09:26 by fcanadas         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def errors():
	if (len(sys.argv) < 2):
		return(1)
	elif not (sys.argv[1].isdigit()):
		print("AssertionError: argument is not an integer")
		return(1)
	elif (len(sys.argv) != 2):
		print("AssertionError: more than one argument are provided")
		return(1)
if (errors()):
	quit()
if (int(sys.argv[1]) == 0):
	print("I'm Zero.\n")
elif (int(sys.argv[1]) % 2 == 0):
	print("I'm Even.\n")
else:
	print("I'm Odd.\n")