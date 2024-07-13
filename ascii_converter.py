#Goal: Convert images into ascii art.
#really its to ASCII-fy Tayama/Yamada-San
"""pre requisites: 
1. how do i format it to fit into a given size reliably
2. how do I know what ASCIII have more luminosity than others. 
3. how do I get each pixel (block) to have to take a given luminence.
.... mb I can compress the image to like 144p and then acess each pixel
"""
from PIL import Image, ImageOps

def scaled_dimensions(width, height, max_height):
    if round(height) <= max_height*1.2:
        return (round(width), round(height))
    else:
        return scaled_dimensions(width = width /2,height = height/2,max_height = max_height)
 
def asciiify(filename):

    chars = ["@", "J", "D", "%", "*", "P", "+", "Y", "$", ",", "."]
    im = Image.open(filename).convert("L")
    im = im.resize(scaled_dimensions(im.width, im.height, 300))
    im = ImageOps.exif_transpose(im) # gotta love stack overflow
    
    assert im is not None
    
    height, width,ascii_img ,pixels  = im.height, im.width, [], list(im.getdata())
    #idk what this error actually means. ngl

    for y  in range (0, height):
        row = pixels[y*width : y*(width) + width]

        for x in range(0, width):
            row[x] = chars[round(row[x]/23)-1]

        ascii_img.append(row)
        ascii_img[y] = ' '.join(ascii_img[y])
    
    ascii_img = '\n'.join(ascii_img)
    with open(f"{filename}_ascii.txt", "w") as f:
        f.write(ascii_img)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
asciiify("me being him.jpeg")


#WHY THE HELL IS AN IMG OF ME ROTATED
#FIXED THIS a while ago.  just didn't know any git beforehand.