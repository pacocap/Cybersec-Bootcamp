# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    filterwords.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: fcanadas <fcanadas@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/13 14:01:10 by fcanadas          #+#    #+#              #
#    Updated: 2023/04/17 15:03:14 by fcanadas         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys, string

def filter_words(s, n):
	s = s.translate(str.maketrans('', '', string.punctuation))
	words = [x for x in s.split() if len(x) > n]
	print(words)

if __name__=="__main__":
	if len(sys.argv) != 3:
		quit(print("ERROR: Please provide exactly two arguments"))
	elif not isinstance(sys.argv[1], str) or not sys.argv[2].isdigit():
		quit(print("ERROR: Arguments must be a string and an integer, in that order"))
	filter_words(sys.argv[1], int(sys.argv[2]))