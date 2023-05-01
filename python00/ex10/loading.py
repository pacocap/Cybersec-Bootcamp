# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    loading.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: fcanadas <fcanadas@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/13 19:33:36 by fcanadas          #+#    #+#              #
#    Updated: 2023/04/17 09:40:05 by fcanadas         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys, time

def ft_progress(lst):
	start_time = time.time()
	ref_time = 0
	print("")
	for i, item in enumerate (lst):
		if len(lst) > 1:
			if item == lst[1]:
				ref_time = time.time() - start_time
		else:
			ref_time = time.time() - start_time
		elapsed_time = time.time() - start_time
		timer = ((lst[len(lst) - 1] - item)) * ref_time
		if (timer < 0):
			timer *= -1
		progr = (i + 1) / len(lst)
		pos_fill = '#' * int(30 * progr) + ' ' * (30 - int(30 * progr))
		print("\r	ETA:  {:7.2f}s   [{:>4.0%}][{}]   {:4}/{}  |  elapsed time {:.2f}s"
			.format(
			timer,
			(i + 1)/len(lst),
			pos_fill,
			i + 1,
			len(lst),
			elapsed_time
			),
			end=''
			)
		yield i
        
def main1():
	listy = range(1)
	ret = 0
	for elem in ft_progress(listy):
		ret += (elem + 3) % 5
		time.sleep(0.01)
	print()
	print(ret)

def main2():
	listy = range(3333)
	ret = 0
	for elem in ft_progress(listy):
		ret += elem
		time.sleep(0.005)
	print()
	print(ret)

if __name__=="__main__":
	main1()