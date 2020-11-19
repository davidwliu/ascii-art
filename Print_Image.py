from PIL import Image

im = Image.open("ascii-pineapple.jpg")
im.thumbnail((800, 200), Image.ANTIALIAS) # resizes original image to match cmd aspect ratio
width, height = im.size
pixel_matrix = list(im.getdata())


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


# construct brightness matrix
brightness_matrix = []

for pixel in pixel_matrix:
	brightness_matrix.append(round(Average(pixel)))


# construct ASCII matrix
ascii_matrix = []

for brightness_value in brightness_matrix:
	ascii_matrix.append(ToASCII(brightness_value))

# print ASCII matrix
for row in range(height):
	for col in range(width):
		for i in range(3):
			print(ascii_matrix[width*row + col], end="")
	print("")