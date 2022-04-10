import random
from PIL import Image

#Путь до картинки
path="perfect/1.bmp"
#Функция добавления случайного шума, степень зашумленности от 0 до 50000
def noise(img, level):
	for numpix in range(0, level):
		x=random.randint(1,int(img.size[0]-2))
		y=random.randint(1,int(img.size[1]-2))
		r,g,b=img.getpixel((x, y))
		r=random.randint(r-50,r+50)
		g=random.randint(g-50,g+50)
		b=random.randint(b-50,b+50)
		for x_1 in range(x-random.randint(0,2),x+random.randint(0,2)):
			for y_1 in range(y-random.randint(0,2),y+random.randint(0,2)):
				img.putpixel((x_1,y_1),(r,g,b))
	return(img)

img = Image.open(path)
img = noise(img, 50000)
img = img.convert('L')
img.show()

