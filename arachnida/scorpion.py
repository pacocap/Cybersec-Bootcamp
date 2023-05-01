# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    scorpion.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: fcanadas <fcanadas@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/17 14:55:54 by fcanadas          #+#    #+#              #
#    Updated: 2023/04/25 12:00:16 by fcanadas         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import argparse
from PIL import Image
from PIL.ExifTags import TAGS

def pargs():
	parser = argparse.ArgumentParser(description='Metadata Viewer\n')
	parser.add_argument('img')
	parser.add_argument('img_list', nargs='*')
	return parser.parse_args()

def format_exif(exif):
	
	for key, value in exif.items():
		exif[TAGS.get(key, value)] = exif[key]
		del exif[key]

def print_exif(exif):

	x = 0
	for key, value in exif.items():
		print('{k:<30}:{v}'.format(k=key, v=value))
	x += 1
	print('')

def print_meta(imgex):
	print('')
	print(f"{'Nombre':<30}:{imgex.filename.split('/')[-1]}")           # Solo el nombre, no la ruta
	print(f"{'Dimensiones':<30}:{imgex.size[0]}, {imgex.size[1]}")
	print(f"{'Formato':<30}:{imgex.format}")
	print(f"{'Modo':<30}:{imgex.mode}")
	print(f"{'Paleta':<30}:{imgex.palette}")
	print('')

def scorpion():
	try:
		for image in images:
			imgex = Image.open(image)
			exif_data = imgex.getexif()
			if exif_data:
				print_meta(imgex)
				format_exif(exif_data)
				print_exif(exif_data)
				print(''.ljust(100, '-'))
			else:
				print_meta(imgex)
				print('No EXIF data found.')
				print(''.ljust(100, '-'))
	except:
		print('Image could not be opened')

if __name__=='__main__':
	global images
	args = pargs()
	images = list()
	images.append(args.img)
	images += args.img_list
	scorpion()
