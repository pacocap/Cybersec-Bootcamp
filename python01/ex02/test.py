# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: fcanadas <fcanadas@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/05/06 16:25:00 by fcanadas          #+#    #+#              #
#    Updated: 2023/05/08 16:10:55 by fcanadas         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from vector import Vector

if __name__=="__main__":
	vector1 = Vector([[0.0, 1.0, 2.0, 3.0]])
	# vector2 = Vector([[1.0, 1.0, 1.0, 1.0]])
	# vector3 = Vector([[0.0], [1.0], [2.0], [3.0]])
	# vector4 = Vector([[1.0], [1.0], [1.0], [1.0]])
	# print(vector1.shape)
	# print(vector1.values)
	# print(vector1.shape)
	# print(vector1.T().values)
	# print(vector1.T().shape)
	# print(vector2.values)
	# print(vector2.shape)
	# print(vector2.T().values)
	# print(vector2.T().shape)
	print(vector1 + Vector([1.0, 1.0, 1.0, 1.0]).values)
	# print((vector3 + vector4).values)
	# print((vector1 - vector2).values)
	# print((vector3 - vector4).values)
	# print(Vector([[1.0, 2.0], [3.0]]).T().values)
	# print(vector1.dot(vector2))

