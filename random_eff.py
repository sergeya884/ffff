import random
from PIL import Image, ImageFilter, ImageEnhance

#НАСТРОЙКИ-----------------------
shift_level = 60            # максимальный уровень сдвига в процентах
rotation_level = 10         # предельный угол поворота в градусах
compr_stretch_level_x = 20  # максимальное сжатие по x в процентах от ширины 
compr_stretch_level_y = 20  # максимальное сжатие по y в процентах от длины
transfer_level = 20         # максимальный перенос в процентах от размеров
noise_quantity = 60         # количество шума в процентах от количества пикселей 
noise_deviation= 80         # степень отклонения яркости цвета в шуме от 0 до 255
brightness_level= 50        # максимальный уровень изменения яркости в процентах
blur_level=100              # максимальный уровень размытия в процентах
#--------------------------------

#Путь до картинки
path = input("Введите путь до файла: ")

#Функция размытия изображения
def blur(img,percent):
	return(img.filter(ImageFilter.BoxBlur(int(16*percent/100))))

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
	dst_img.paste(img, (int((width-new_width)/2), int((height-new_height)/2)), img)
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
	dst_img.paste(img, (int(new_width/2), int(new_height/2)), img)
	return(dst_img)

#Функция изменения яркости
def brightness(img, factor): 
	enhancer = ImageEnhance.Brightness(img)
	return(enhancer.enhance(factor))

#Функция добавления случайного шума
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
		#Меняем яркость квадрата со сторонами 1/50 от длины и ширины изображения с пикселем в центре
		for x_1 in range(x-random.randint(0,int(width/150)),x+random.randint(0,int(height/150))):
			for y_1 in range(y-random.randint(0,2),y+random.randint(0,2)):
				img.putpixel((x_1,y_1),bright)
	return(img)

#Функция сдвига вдоль x
def shift(img, level):
	img = img.convert('L')
	width, height = img.size
	level = int(width/2*level/100)
	j=0
	if(level<=0): j=-level
	#Сдвигаем по x
	for x in range(0, int(img.size[0])):
		for y in range(0,int(img.size[1])):
			bright=img.getpixel((x, y))
			img.putpixel((x-j-int(level*y/height),y),bright)
	
	#Теперь центрируем
	#Узнаем размеры исходного изображения
	width, height = img.size
	img = img.convert('RGBA')
	#Создаем шаблон белого фона
	dst_img = Image.new("L", (width, height), "white" )
	dst_img.paste(img, (j+int(level/2), 0), img)
	return(dst_img)


for i in range(0,int(input("Введите число изменненых изображений: "))):
	img = Image.open(path)
	img = shift(img, random.randint(-shift_level, shift_level))
	img = img.convert('RGBA')
	img = rotation(img, random.randint(-rotation_level, rotation_level))
	img = img.convert('RGBA')
	img = compr_stretch(img, random.randint(-compr_stretch_level_x, compr_stretch_level_x), random.randint(-compr_stretch_level_y, compr_stretch_level_y))
	img = img.convert('RGBA')
	img = transfer(img, random.randint(-transfer_level, transfer_level), random.randint(-transfer_level, transfer_level))
	img = img.convert('L')
	img = noise(img, random.randint(0, noise_quantity), noise_deviation)
	img = brightness(img, random.randint(100-brightness_level, 100+brightness_level)/100)
	img = blur(img, random.randint(0, blur_level))
	img = img.convert('L')
	path2='tests/'+str(i)+'.png'
	img.save(path2)
	


