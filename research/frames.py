import PIL
import os
import os.path
from PIL import Image

f = r'c://Users/Soumyadip Nandi/Desktop/Level 2 vs level 4/chicago data/library/auto/frames'
for file in os.listdir(f):
    f_img = f+"/"+file
    img = Image.open(f_img)
    img = img.resize((64,64))
    img.save(f_img)


