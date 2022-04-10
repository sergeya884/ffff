from PIL import Image
#Путь до картинки
path="perfect/1.bmp"

#Функция поворота изображения на заданный угол
def rotation(img, angle):
	#Создаем шаблон белого фона
	dst_img = Image.new("L", (240,320), "white" )
	#Поворачиваем исходное изображение
	img = img.rotate(angle)
	#Подставляем измененное изображение на фон
	dst_img.paste(img, (0, 0), img)
	return(dst_img)

#Открываем исходное изображение	
img = Image.open(path)
img = img.convert('RGBA')
#Поворот на 1.5 градуса
img = rotation(img, 1.5)
#Выводим изображение
img.show()
