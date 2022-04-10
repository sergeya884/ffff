from PIL import Image
path="perfect/1.bmp"

#Функция сжатия, растяжения картинки в процентном соотношении без изменения размера
def compr_stretch(img, width_percent, height_percent):
	#Создаем шаблон белого фона
	dst_img = Image.new("L", (240,320), "white" )
	#Узнаем размеры исходного изображения
	width, height = img.size
	#Считаем повые размеры как процент от старых
	new_wight=int(width*(100-width_percent)/100)
	new_height=int(height*(100-height_percent)/100)
	#Меняем размер исходного изображения
	img = img.resize((new_wight, new_height))
	#Подставляем измененное изображение на фон
	dst_img.paste(img, (120-int(new_wight/2), 160-int(new_height/2)), img)
	return(dst_img)

#Открываем исходное изображение		
img = Image.open(path)
img = img.convert('RGBA')
#Изменяем исходное изображение на -10 процентов по горизонтали и на 20 по вертикали
img=compr_stretch(img, -10, 20)
img.show()

