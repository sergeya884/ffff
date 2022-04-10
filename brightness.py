from PIL import Image, ImageEnhance

#Путь до картинки
path="perfect/1.bmp"

#Функция изменения яркости factor от 0.5 до 1.5
def brightness(img, factor): 
	enhancer = ImageEnhance.Brightness(img)
	return(enhancer.enhance(factor))

#Открываем исходную картинку
img = Image.open(path)
#Меняем яркость изображения с фактором 0.5
img=brightness(img,0.5)
img.show()


