# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata01.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: fcanadas <fcanadas@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/12 16:58:47 by fcanadas          #+#    #+#              #
#    Updated: 2023/04/17 12:49:00 by fcanadas         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

kata = {
'Python': 'Guido van Rossum',
'Ruby': 'Yukihiro Matsumoto',
'PHP': 'Rasmus Lerdorf',
}

if __name__=="__main__":
	for key, value in kata.items():
		print (key, "was created by", value)