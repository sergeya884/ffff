import random
from PIL import Image

#Путь до картинки
path="perfect/1.bmp"
#Функция добавления случайного шума, степень зашумленности от 0 до 50000
def noise(img, noise_quantity, noise_deviation):
	#Узнаем размеры исходного изображения
	width, height = img.size
	for numpix in range(0, int(noise_quantity*width*height/100)):
		#Случайный пиксель
		x=random.randint(2,int(img.size[0]-3))
		y=random.randint(2,int(img.size[1]-3))
		#Узнаем яркость
		bright = img.getpixel((x, y))
		#Случайно меняем яркость в заданном пределе
		bright=random.randint(bright-noise_deviation,bright+noise_deviation)
		#Меняем яркость квадрата со сторонами 1/100 от длины и ширины изображения с пикселем в центре
		for x_1 in range(x-random.randint(0,int(width/200)),x+random.randint(0,int(height/200))):
			for y_1 in range(y-random.randint(0,2),y+random.randint(0,2)):
				img.putpixel((x_1,y_1),bright)
	return(img)

img = Image.open(path)
img = img.convert('L')
img = noise(img, 50, 80)
img.show()

