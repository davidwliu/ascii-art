from PIL import Image

im = Image.open("ascii-pineapple.jpg")

# construct pixel matrix
pixel_matrix = list(im.getdata())

print("Successfully constructed matrix!")
print("Pixel matrix size: " + str(im.width) + " x " + str(im.height))
print("Iterating through pixel contents:")

for elem in pixel_matrix:
	print(elem)