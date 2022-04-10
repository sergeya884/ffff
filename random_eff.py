import random
from PIL import Image, ImageFilter, ImageEnhance

#Путь до картинки
path="perfect/9.bmp"

#Функция размытия изображения
def blur(img,percent):
	return(img.filter(ImageFilter.BoxBlur(int(13*percent/100))))

#Функция поворота изображения на заданный угол
def rotation(img, angle):
	#Узнаем размеры исходного изображения
	width, height = img.size
	#Создаем шаблон белого фона
	dst_img = Image.new("L", (width, height), "white" )
	#Поворачиваем исходное изображение
	img = img.rotate(angle)
	#Подставляем измененное изображение на фон
	dst_img.paste(img, (0, 0), img)
	return(dst_img)

#Функция сжатия, растяжения картинки в процентном соотношении без изменения размера
def compr_stretch(img, width_percent, height_percent):
	#Узнаем размеры исходного изображения
	width, height = img.size
	#Создаем шаблон белого фона
	dst_img = Image.new("L", (width, height), "white" )
	#Считаем повые размеры как процент от старых
	new_width=int(width*(100-width_percent)/100)
	new_height=int(height*(100-height_percent)/100)
	#Меняем размер исходного изображения
	img = img.resize((new_width, new_height))
	#Подставляем измененное изображение на фон
	dst_img.paste(img, (120-int(new_width/2), 160-int(new_height/2)), img)
	return(dst_img)

#Функция параллельного переноса картинки в процентном соотношении от размеров
def transfer(img, width_percent, height_percent):
	#Узнаем размеры исходного изображения
	width, height = img.size
	#Создаем шаблон белого фона
	dst_img = Image.new("L", (width, height), "white" )
	#Перенос как процент от размеров
	new_width=int(width*width_percent/100)
	new_height=int(height*height_percent/100)
	#Переносим изображение относительно фона
	dst_img.paste(img, (120-int((new_width+width)/2), 160-int((new_height+height)/2)), img)
	return(dst_img)

#Функция изменения яркости factor от 0.5 до 1.5
def brightness(img, factor): 
	enhancer = ImageEnhance.Brightness(img)
	return(enhancer.enhance(factor))

#Функция добавления случайного шума, степень зашумленности от 0 до 50000
def noise(img, level):
	for numpix in range(0, level):
		x=random.randint(2,int(img.size[0]-3))
		y=random.randint(2,int(img.size[1]-3))
		r,g,b = img.getpixel((x, y))
		r=random.randint(r-50,r+50)
		g=random.randint(g-50,g+50)
		b=random.randint(b-50,b+50)
		for x_1 in range(x-random.randint(0,2),x+random.randint(0,2)):
			for y_1 in range(y-random.randint(0,2),y+random.randint(0,2)):
				img.putpixel((x_1,y_1),(r,g,b))
	return(img)

#Открываем исходное изображение	
for i in range(1,20):
	img = Image.open(path)
	img = img.convert('RGBA')
	img = rotation(img, random.randint(-10, 10))
	img = img.convert('RGBA')
	img = compr_stretch(img, random.randint(-20, 20), random.randint(-20, 20))
	img = img.convert('RGBA')
	img = transfer(img, random.randint(-20, 20), random.randint(-20, 20))
	img = img.convert('RGB')
	img = noise(img, random.randint(0, 50000))
	img = img.convert('RGBA')
	img = brightness(img, random.randint(5, 15)/10)
	img = blur(img, random.randint(0, 100))
	img = img.convert('L')
	path2='tests/'+str(i)+'.png'
	img.save(path2)
	


