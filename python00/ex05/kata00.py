# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata00.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: fcanadas <fcanadas@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/12 16:58:42 by fcanadas          #+#    #+#              #
#    Updated: 2023/04/15 13:11:54 by fcanadas         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

kata = (123, 41, 1)

if __name__=="__main__":
	flag = True
	if isinstance(kata, int):
		print("The number is:", kata)
	elif len(kata) > 1:
		for i in kata:
			if not isinstance(i, int):
				flag = False
		if flag:
			print("The", len(kata), "numbers are:", ', '.join(str(x) for x in kata))
 