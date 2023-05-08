# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    vector.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: fcanadas <fcanadas@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/05/06 16:25:03 by fcanadas          #+#    #+#              #
#    Updated: 2023/05/08 16:16:13 by fcanadas         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# import sys

# sys.tracebacklimit = 0

class Vector:
	def __init__(self, values:list):
		self.values = values
	
	@property
	def values(self):
		return self._values
	@values.setter
	def values(self, value):
		try:
			self._values = list(value)
			if len(self._values) > 1:
				for el in self._values:
					if len(el) != 1:
						raise ValueError ('There is more than one element in at least one of the lists')
					if not isinstance(el[0], float):
						raise TypeError('The element of each list within the list must be a float')
				self._shape = (len(self._values), 1)
			else:
				for el in self._values[0]:
					if not isinstance(el, float):
						raise TypeError('All the elements of the list within the list must be floats')
					self._shape = (1, len(self._values[0]))
		except AttributeError:
			raise AttributeError('The value must be one of the following:\n	-A list of n lists, each with a single float element\n	-A list of a single list of n float elements')

	@property
	def shape(self):
		return self._shape

	def _iscolumn(self):
		if len(self._values) == 1:
			return False
		return True

	def dot(self, vector):
		result = list()
		if not self._shape == vector.shape:
			raise ValueError('Vectors must be of the same shape')
		if self._iscolumn():
			for el1, el2 in zip(self._values, vector._values):
				result.append(el1[0]*el2[0])
			return result
		else:
			for el1, el2 in zip(self._values[0], vector._values[0]):
				result.append(el1*el2)
			return result
		
	def T(self):
		transp_vector = list()
		if self._iscolumn():
			col = list()
			for el in self._values:
				col.append(el[0])
			transp_vector.append(col)
			return Vector(transp_vector)
		else:
			for el in self._values[0]:
				transp_vector.append([el])
		return Vector(transp_vector)

	# Only vectors of the same dimension  
	def __add__(self, vector):
		result = list()
		if not self._shape == vector.shape:
			raise ValueError('Vectors must be of the same shape')
		if self._iscolumn():
			for el1, el2 in zip(self._values, vector._values):
				result.append(el1[0]+el2[0])
			return Vector([result])
		else:
			for el1, el2 in zip(self._values[0], vector._values[0]):
				result.append(el1+el2)
			return Vector([result])
	# def __radd__(self, vector):
		# result = list()
		# if not self._shape == vector.shape:
		# 	raise ValueError('Vectors must be of the same shape')
		# if self._iscolumn():
		# 	for el1, el2 in zip(self._values, vector._values):
		# 		result.append(el1[0]+el2[0])
		# 	return Vector([result])
		# else:
		# 	for el1, el2 in zip(self._values[0], vector._values[0]):
		# 		result.append(el1+el2)
		# 	return Vector([result])
	# Only vectors of the same dimension
	def __sub__(self, vector):
		result = list()
		if not self._shape == vector.shape:
			raise ValueError('Vectors must be of the same shape')
		if self._iscolumn():
			for el1, el2 in zip(self._values, vector._values):
				result.append(el1[0]-el2[0])
			return Vector([result])
		else:
			for el1, el2 in zip(self._values[0], vector._values[0]):
				result.append(el1-el2)
			return Vector([result])
	def __rsub__(self):
		0
	# Only Vector / scalar
	def __truediv__(self):
		0
	# Raise a NotImplementedError('Division of a scalar by a Vector is not defined here')
	def __rtruediv__(self):
		0
	# Only Vector * scalar
	def __mul__(self):
		0
	def __rmul__(self):
		0
	# Both should be identical.
	# def __str__(self):
	# 	0
	# def __repr__(self):
	# 	0