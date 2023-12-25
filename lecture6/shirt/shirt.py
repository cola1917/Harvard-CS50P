from PIL import Image, ImageOps
import sys
import os
extension = ['.jpg', '.jpeg', '.png']
count_argv = len(sys.argv)
# print(sys.argv)
if count_argv < 3:
    sys.exit('Too few command-line arguments')
elif count_argv > 3:
    sys.exit('Too many command-line arguments')

input_ex = os.path.splitext(sys.argv[1])[-1]
output_ex = os.path.splitext(sys.argv[2])[-1]

if input_ex != output_ex:
    sys.exit('Input and output have different extensions')
elif input_ex not in extension or output_ex not in extension:
    sys.exit('Invalid output')

try:
    shirt = Image.open("shirt.png")
    with Image.open(sys.argv[1]) as im:
        # print(im.size)
        # shirt = ImageOps.fit(shirt, im.size)
        im = ImageOps.fit(im, shirt.size)
        # print(shirt.size)
        im.paste(shirt, shirt)
        im.save(sys.argv[2])


except FileNotFoundError:
    sys.exit("File does not exist.")


