__import__("os").system("pip --quiet install Pillow -q")  
from PIL import Image, ImageOps, ImageFilter 

import urllib.request 

# found this proc here, it pastes images together: https://note.nkmk.me/en/python-pillow-concat-images/
def concat_img(im1, im2, im3):
     res = Image.new('RGB', (im1.width, im1.height + im2.height + im3.height)) 
     res.paste(im1, (0, 0)) 
     res.paste(im2, (0, im1.height)) 
     res.paste(im3, (0, im1.height + im2.height))
     return res

# get a random picture
x = 'https://picsum.photos/300/400/'
file = urllib.request.urlopen(x).read()

# write file so PIL can use it
with open('file.png', 'wb') as f: 
    f.write(file)
f.close()

# change image with PIL
f2 = Image.open('file.png').convert('RGB') 
f2_invert = ImageOps.invert(f2) 
f2_blur = f2.filter(ImageFilter.BoxBlur(5))

# save and show all

concat_img(f2, f2_invert, f2_blur).save('file.png')

