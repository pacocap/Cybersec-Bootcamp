# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    guess.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: fcanadas <fcanadas@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/13 17:55:07 by fcanadas          #+#    #+#              #
#    Updated: 2023/04/15 14:12:10 by fcanadas         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys, random

def game(sol):
	count = 0
	while True:
		att = input("What's your guess between 1 and 99?\n")
		count = count_att(count)
		if att == 'exit':
			print("Goodbye!")
			break
		elif not att.isdigit():
			print("That is not a number, please try again.")
		elif int(att) < 1 or int(att) > 99:
			print("Please type a number within the provided range.")
		elif int(att) == sol:
			win(int(att), count)
			break
		else:
			retry(int(att), sol)

def count_att(count):
    count += 1
    return count

def gen_sol():
	sol = random.randint(1, 99)
	return sol

def retry(att, sol):
	if att > sol:
		print("Too high! Try a lower number.")
	else:
		print("Too low! Try a higher number.")

def win(att, count):
	if att == 42:
		print("\"For a moment, nothing happened. Then, after a second or so, nothing continued to happen.\"")
	if count == 1:
		print("Wow!! You got it on your first try!")
	else:
		print("Congratulations! You found the secret number!\nYou needed only {} attempts :)\n".format(count))

if __name__=="__main__":
	print("\nWelcome to my Interactive Guessing Game!\nYou have to enter a number between 1 and 99 to find out the secret number.\nIf you want to exit the game, type 'exit'.\nGood luck!\n")
	game(gen_sol())