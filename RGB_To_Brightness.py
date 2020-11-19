from PIL import Image

im = Image.open("ascii-pineapple.jpg")
pixel_matrix = list(im.getdata())

# brightness mappings
def Average(RGB):
	return (RGB[0] + RGB[1] + RGB[2])/3

def Lightness(RGB):
	return (max(RGB) + min(RGB)/2)

def Luminosity(RGB):
	return (0.21*RGB[0] + 0.72*RGB[1] + 0.07*RGB[2])


# construct brightness matrix
brightness_matrix = []

for pixel in pixel_matrix:
	brightness_matrix.append(round(Average(pixel)))

print("Successfully constructed brightness matrix!")
print("Brightness matrix size: " + str(im.width) + " x " + str(im.height))
print("Iterating through pixel brightnesses:")

for elem in brightness_matrix:
	print(elem)