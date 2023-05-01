# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    sos.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: fcanadas <fcanadas@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/13 16:31:28 by fcanadas          #+#    #+#              #
#    Updated: 2023/04/15 14:07:31 by fcanadas         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ' ':'/'}

def translate_to_morse(s):
	list_to_tr = [x.upper() for x in list(s)]
	morse_tr = [MORSE_CODE_DICT[x] for x in list_to_tr]
	print(' '.join(morse_tr))

if __name__=="__main__":
	if len(sys.argv) < 2:
		quit(print("Please, enter any number of string arguments."))
	s = " ".join(sys.argv[1:])
	for x in s:
		if not x.upper() in MORSE_CODE_DICT:
			quit(print("ERROR: Please, use only alphanumeric characters and spaces"))
	translate_to_morse(s)