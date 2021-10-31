import sys
import os
from PIL import Image

#using sys modle, grab first and second argument

print('this is the folder path', sys.argv[0])

images_folder = 'C:/Users/ssbri/Coding/Python/Zero to Mastery Course/Pokedex/venv/images'
output_folder = 'C:/Users/ssbri/Coding/Python/Zero to Mastery Course/Pokedex/venv/new'

#if new folder exists, if not create it

if os.path.exists(output_folder):
  pass
else:
  os.makedirs(output_folder)


#loop through pokedex



for filename in os.listdir(images_folder):
  img = Image.open(rf'{images_folder}/{filename}')
  clean_name = os.path.splitext(filename)[0]
  img.save(rf'{output_folder}/{clean_name}.png', 'png')
  print('all done')



#convert images to png

#save to new folder

