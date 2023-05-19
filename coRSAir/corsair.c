/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   corsair.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: fcanadas <fcanadas@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/05/10 18:22:25 by fcanadas          #+#    #+#             */
/*   Updated: 2023/05/17 12:30:58 by fcanadas         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "openssl/rsa.h"
#include "openssl/bn.h"
#include "openssl/pem.h"
#include "openssl/bio.h"
#include "openssl/x509.h"
#include "openssl/evp.h"

#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <unistd.h>
#include <fcntl.h>

#ifndef BUFFERSIZE
# define BUFFERSIZE 1024
#endif

int	parse_args(int argc, char **argv)
{
	if (argc != 4)
	{
		printf("ERROR: Wrong number of argumets");
		return (0);
	}
	if ((!strrchr(argv[1], '.') || strrchr(argv[1], '.') == argv[1])
		|| (!strrchr(argv[2], '.') || strrchr(argv[2], '.') == argv[2])
		|| (!strrchr(argv[3], '.') || strrchr(argv[3], '.') == argv[3]))
	{
		printf("ERROR: Some files could not be read");
		return (0);
	}
	if (strcmp(strrchr(argv[1], '.'), ".pem") != 0
		|| strcmp(strrchr(argv[2], '.'), ".pem") != 0
		|| strcmp(strrchr(argv[3], '.'), ".enc") != 0)
	{
		printf("ERROR: Some files extensions were wrong. ");
		printf("Please make sure to use two .pem certificates");
		printf(" followed by a .enc encrypted password");
		return (0);
	}
	return (1);
}

RSA	*get_rsa(char *file)
{
	BIO			*bio_file;
	X509		*cert;
	EVP_PKEY	*pub_key;
	RSA			*rsa;

	bio_file = BIO_new(BIO_s_file());
	if ((BIO_read_filename(bio_file, file)) != 1)
	{
		printf("ERROR: File could not be converted to BIO");
		exit (0);
	}
	cert = PEM_read_bio_X509(bio_file, NULL, 0, NULL);
	pub_key = X509_get_pubkey(cert);
	rsa = EVP_PKEY_get1_RSA(pub_key);
	BIO_free(bio_file);
	X509_free(cert);
	EVP_PKEY_free(pub_key);
	return (rsa);
}

int	main(int argc, char **argv)
{
	RSA				*private;
	RSA				*rsa_1;
	RSA				*rsa_2;
	BN_CTX			*ctx;
	BIGNUM			*one;
	BIGNUM			*n_1;
	BIGNUM			*n_2;
	BIGNUM			*e;
	BIGNUM			*d;
	BIGNUM			*p;
	BIGNUM			*q_1;
	BIGNUM			*phi_p;
	BIGNUM			*phi_q_1;
	BIGNUM			*phi_n;
	int				len;
	unsigned char	*buff_in;
	unsigned char	*buff_out;

	if (!parse_args(argc, argv))
		return (0);
	//Inicializo el buffer context para los cálculos con BIGNUM
	ctx = BN_CTX_new();
	//Inicializo las variables para obtener n1, n2 y e
	rsa_1 = RSA_new();
	rsa_2 = RSA_new();
	n_1 = BN_new();
	n_2 = BN_new();
	e = BN_new();
	//Obtengo los valores n1, n2 y e
	rsa_1 = get_rsa(argv[1]);
	rsa_2 = get_rsa(argv[2]);
	n_1 = (BIGNUM *)RSA_get0_n(rsa_1);
	n_2 = (BIGNUM *)RSA_get0_n(rsa_2);
	e = (BIGNUM *)RSA_get0_e(rsa_1);
	//Inicializo las variables para calcular los primos
	p = BN_new();
	q_1 = BN_new();
	//Calculo los primos
	BN_gcd(p, n_1, n_2, ctx);
	BN_div(q_1, NULL, n_1, p, ctx);
	//Inicializo las variables para calcular las funciones phi de Euler
	one = BN_new();
	BN_dec2bn(&one, "1");
	phi_p = BN_new();
	phi_q_1 = BN_new();
	phi_n = BN_new();
	//Calculo las funciones phi de Euler
	BN_sub(phi_p, p, one);
	BN_sub(phi_q_1, q_1, one);
	BN_mul(phi_n, phi_p, phi_q_1, ctx);
	//Con phi de n y e calculo el inverso modular d (exponente de la clave privada)
	d = BN_new();
	BN_mod_inverse(d, e, phi_n, ctx);
	//Con d, e y n, calculo la clave privada
	private = RSA_new();
	RSA_set0_key(private, n_1, e, d);
	buff_in = (unsigned char *)malloc(sizeof(char) * BUFFERSIZE);
	buff_out = (unsigned char *)malloc(sizeof(char) * BUFFERSIZE);
	len = read(open(argv[3], O_RDONLY), buff_in, BUFFERSIZE);
	RSA_private_decrypt(len, buff_in, buff_out, private, RSA_PKCS1_PADDING);
	printf("\n Mensaje encriptado: %s", buff_in);
	printf("\nMensaje desencriptado: %s", buff_out);
	//Libero todo
	BN_CTX_free(ctx);
	BN_free(n_1);
	BN_free(n_2);
	BN_free(e);
	BN_free(p);
	BN_free(q_1);
	BN_free(one);
	BN_free(phi_p);
	BN_free(phi_q_1);
	BN_free(phi_n);
	BN_free(d);
	free(buff_in);
	free(buff_out);
}
