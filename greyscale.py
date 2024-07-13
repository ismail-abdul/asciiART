import PIL
from PIL import Image
import PIL.ImageShow
#i wanna be able to greyscale an image

"""
1. Create Image object from image file. 
2. access individual pixels. app this is slow. smn along the lines of using some numpyy tricks to change the pixel values in the array that holds the pixel values. its cus of the python interpreter overhead.
3. calc greyscale
    via luminosity equation 
4. reset rgb values to greyscale for each val
5. save a copy of file in new folder called greyscale
6. show image in new window
"""

def main():
    show_image("npc.png")

def show_image(fileName):
    im = Image.open(fileName)
    #print(im.format, im.size, im.mode)
    #im.show("The real Zuck.")
    grey_im = im.convert("L")
    grey_im.save("greyscale_zuck.png")
    grey_im.close()
    im.close()
main()

def greyscale(filename):
    im = Image.open(filename)
    return im.convert("L")

