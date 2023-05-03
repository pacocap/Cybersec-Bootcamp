# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_otp.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: fcanadas <fcanadas@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/25 17:39:28 by fcanadas          #+#    #+#              #
#    Updated: 2023/05/01 09:42:58 by fcanadas         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import argparse, os, hmac, hashlib, time, struct, pyotp, base64
from cryptography.fernet import Fernet

def pargs():
	parser = argparse.ArgumentParser(description='A two-parts program destined to first encrypt a common secret key to send to the client, and then to decrypt it and generate a TOTP from it.')
	group = parser.add_mutually_exclusive_group(required=True) 
	group.add_argument('-g', '--generate', metavar='.hex')
	group.add_argument('-k', '--key', metavar='.key')
	group.add_argument('-d', '--delete', action='store_true')
	return parser.parse_args()

def valid_file_g(arg):
	try:
		with open(arg, 'r') as file:
			key_hex = file.read()
		try:
			if len(key_hex) == 64 and int(key_hex, 16):
				return True
		except:
			print('ERROR: All characters from key must be hexadecimal')
			return False
		print("ERROR: Key must be 64 hexadecimal characters long.")
		return False
	except:
		print('ERROR: File does not exist or could not be opened.')

def get_file(arg):
	return open(arg, 'rb').read()

def fernet_key():
	try:
		if args.generate:
			fer_key = Fernet.generate_key()
			open('.keyception.key', 'wb').write(fer_key)
			f = Fernet(fer_key)
		elif args.key:
			fer_key = open('.keyception.key', 'r').read()
			f = Fernet(fer_key)
			os.remove('.keyception.key')
		return f
	except:
		quit(print('ERROR: No encrypted key available.'))

def encrypt(key_sent):
	encr_key = f.encrypt(key_sent)
	return (encr_key)

def FTIER_create_encr_key_file(key_g):
	encr_key = encrypt(key_g)
	open('ft_otp.key', 'wb').write(encr_key)
	return(encr_key)

def decrypt(encr_key):
	decr_key = f.decrypt(encr_key)
	return decr_key

def create_hmac(shared_key):
	time_msg = int(time.time()//30)
	time_check = struct.pack(">Q", time_msg)
	hashed_key = hmac.digest(shared_key, time_check, hashlib.sha1)
	return hashed_key

def gen_otp(hashed_key):
	offset   =  hashed_key[19] & 0xf
	bin_code = (hashed_key[offset]  & 0x7f) << 24 | (hashed_key[offset+1] & 0xff) << 16 | (hashed_key[offset+2] & 0xff) <<  8 | (hashed_key[offset+3] & 0xff)
	return (bin_code % 1000000)

def FTIER_create_otp(key_k):
	decr_key = decrypt(key_k)
	hashed_key = create_hmac(decr_key)
	return gen_otp(hashed_key)

# def check_otp(key_k):
# 	decr_key = decrypt(key_k)
# 	totp = pyotp.TOTP(base64.b32encode(decr_key), interval=30)
# 	totp_gen = totp.now()
# 	return(totp_gen)

if __name__=='__main__':
	global f
	args = pargs()
	if args.generate or args.key:
		f = fernet_key()
	if args.generate:
		if valid_file_g(args.generate):
			try:
				create_encr_key_file(get_file(str(args.generate)))
				print('Key was successfully saved in ft_otp.key')
			except:
				print('ERROR: Key could not be encrypted.')
	elif args.key:
		try:
			print('Código de control:	', check_otp(get_file(args.key)))
			print('Código generado:	 {:06d}'.format(create_otp(get_file(args.key))))
		except:
			print('ERROR: OTP password generation failed.')
	elif args.delete:
		if os.path.isfile('ft_otp.key'):
			os.remove('ft_otp.key')
		if os.path.isfile('.keyception.key'):
			os.remove('.keyception.key')
