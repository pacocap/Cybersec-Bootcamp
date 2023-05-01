# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    exec.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: fcanadas <fcanadas@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/11 16:21:55 by fcanadas          #+#    #+#              #
#    Updated: 2023/04/11 16:39:25 by fcanadas         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

if(len(sys.argv)<2):
	print("")
else:
    sys.argv.pop(0)
    string = " ".join(sys.argv)
    print(string.swapcase()[::-1], end="\n\n")