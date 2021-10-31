'''
from PIL import Image, ImageFilter

img = Image.open('venv/images/pikachu.jpg')
filtered_img = img.filter(ImageFilter.SMOOTH)
print(img.format)
print(img.mode)
print(img.size)
filtered_img.save("blur.png", 'png')

gray_img = img.convert('L')
gray_img.save("grayscale.png", 'png')
gray_img.show()

'''
