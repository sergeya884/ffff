import random
from PIL import Image

#Путь до картинки
path="perfect/7.bmp"

def shift(img, level_x, level_y):
	img = img.convert('RGB')
	width = img.size[0]
	height = int(img.size[1])
	i=0
	j=0
	if(level_x<=0): i=-level_x
	if(level_y<=0): j=-level_y
	#Сдвигаем по x
	for x in range(0, int(img.size[0])):
		for y in range(0,int(img.size[1])):
			r,g,b=img.getpixel((x, y))
			img.putpixel((x-j-int(level_y*y/height),y),(r,g,b))
	#Сдвигаем по y		
	for x in range(0, int(img.size[0])):
		for y in range(0,int(img.size[1])):
			r,g,b=img.getpixel((x, y))
			img.putpixel((x,y-i-int(level_x*x/width)),(r,g,b))
	#Теперь центрируем
	#Узнаем размеры исходного изображения
	width, height = img.size
	img = img.convert('RGBA')
	#Создаем шаблон белого фона
	dst_img = Image.new("L", (width, height), "white" )
	dst_img.paste(img, (j+int(level_y/2), i+int(level_x/2)), img)
	return(dst_img)

img = Image.open(path)
img = shift(img, -100, 100)
img.show()

