from PIL import Image
path="perfect/1.bmp"

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

#Открываем исходное изображение		
img = Image.open(path)
img = img.convert('RGBA')
#Переносим исходное изображение на -10 процентов по горизонтали и на 20 по вертикали
img=transfer(img, -10, 20)
img.show()

