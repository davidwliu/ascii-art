from PIL import Image
from colorama import init, Fore
init()

# ASCII chars used for each pixel
ASCII_string = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"


# brightness mappings
def Average(RGB):
	return (RGB[0] + RGB[1] + RGB[2])/3

def Lightness(RGB):
	return (max(RGB) + min(RGB)/2)

def Luminosity(RGB):
	return (0.21*RGB[0] + 0.72*RGB[1] + 0.07*RGB[2])

def ToASCII(brightness_value):
	stringIndex = round(brightness_value/255 * (len(ASCII_string)- 1))
	return ASCII_string[stringIndex]


# construct pixel matrix
def get_pixel_matrix(image):
	return list(image.getdata())


# construct brightness matrix
def get_brightness_matrix(pixel_matrix, brightness_setting = 'Average'):
	brightness_matrix = []

	if brightness_setting == 'Average':
		for pixel in pixel_matrix:
			brightness_matrix.append(round(Average(pixel)))
	elif brightness_setting == 'Lightness':
		for pixel in pixel_matrix:
			brightness_matrix.append(round(Lightness(pixel)))
	elif brightness_setting == 'Luminosity':
		for pixel in pixel_matrix:
			brightness_matrix.append(round(Luminosity(pixel)))

	return brightness_matrix


# construct ASCII matrix
def get_ascii_matrix(brightness_matrix):
	ascii_matrix = []

	for brightness_value in brightness_matrix:
		ascii_matrix.append(ToASCII(brightness_value))

	return ascii_matrix


# print ASCII matrix
def print_ascii_matrix(ascii_matrix, height, width, text_color):
	for row in range(height):
		for col in range(width):
			for i in range(3):
				print(text_color + ascii_matrix[width*row + col], end="")
		print("")


# construct inverted ascii matrix and print inverted ascii matrix
def inverted_ascii_matrix(brightness_matrix):
	inverted_ascii_matrix = []

	for brightness_value in brightness_matrix:
		inverted_ascii_matrix.append(ToASCII(255 - brightness_value))

	return inverted_ascii_matrix

def print_inverted_ascii_matrix(inverted_ascii_matrix, height, width):
	for row in range(height):
			for col in range(width):
				for i in range(3):
					print(inverted_ascii_matrix[width*row + col], end="")
			print("")

def invert_brightness(brightness_matrix, height, width):
	ascii_matrix = inverted_ascii_matrix(brightness_matrix)
	print_inverted_ascii_matrix(ascii_matrix, height, width)



#MAIN

im = Image.open("lincoln.jpg")
im.thumbnail((800, 200), Image.ANTIALIAS) # resizes original image to match cmd aspect ratio
width, height = im.size

pixel_matrix = get_pixel_matrix(im)
brightness_matrix = get_brightness_matrix(pixel_matrix, 'Luminosity')
ascii_matrix = get_ascii_matrix(brightness_matrix)
print_ascii_matrix(ascii_matrix, height, width, Fore.WHITE)
invert_brightness(brightness_matrix, height, width)