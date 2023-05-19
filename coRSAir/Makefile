# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: fcanadas <fcanadas@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/05/17 12:36:23 by fcanadas          #+#    #+#              #
#    Updated: 2023/05/17 12:38:03 by fcanadas         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

export LDFLAGS="-L/Users/fcanadas/.brew/opt/openssl@1.1/lib"
export CPPFLAGS="-I/Users/fcanadas/.brew/opt/openssl@1.1/include"
CFLAGS  =   -Werror -Wall -Wextra

all: 
	@clear
	gcc corsair.c $(CFLAGS) $(CPPFLAGS) $(LDFLAGS) -lssl -lcrypto -o corsair
	@./corsair ./src/cert1.pem ./src/cert2.pem ./src/passwd.enc