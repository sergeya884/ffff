from PIL import Image
path="perfect/1.bmp"

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

#Открываем исходное изображение		
img = Image.open(path)
img = img.convert('RGBA')
#Изменяем исходное изображение на -10 процентов по горизонтали и на 20 по вертикали
img=compr_stretch(img, -10, 20)
img.show()

