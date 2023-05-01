# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    operations.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: fcanadas <fcanadas@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/12 14:03:46 by fcanadas          #+#    #+#              #
#    Updated: 2023/04/15 12:12:15 by fcanadas         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def operations(a, b):
    a, b = int(a), int(b)
    sum, dif, prod = a + b, a - b, a * b
    print("Sum:		", sum)
    print("Difference:	", dif)
    print("Product:	", prod)
    if b == 0:
        div = "ERROR: Division by zero"
        mod = "ERROR: Module by zero" 
    else:
        div = a / b
        mod = a % b 
    print("Quotient:	", div)
    print("Remainder:	", mod)

if __name__=="__main__":
    if len(sys.argv) == 1:
        quit(print("Please, execute the function as follows: python3 operations.py <num_1> <num_2>"))
    elif len(sys.argv) > 3 or (len(sys.argv) < 3):
        quit(print("ERROR: Please, provide exactly 2 numbers to operate with"))
    try:
        a = int(sys.argv[1])
        b = int(sys.argv[2])
        operations(a, b)
    except:
        quit(print("Please, make sure you wrote a valid number"))
