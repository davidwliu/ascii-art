from PIL import Image

im = Image.open("ascii-pineapple.jpg")

print("Successfully loaded image!")
print("Image size: " + str(im.width) + " x " + str(im.height))