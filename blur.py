from PIL import Image
from PIL import ImageFilter

#Путь до картинки
path="perfect/1.bmp"

#Функция размытия изображения
def blur(img,percent):
	return(img.filter(ImageFilter.BoxBlur(int(13*percent/100))))

#Открываем исходное изображение	
img = Image.open(path)
img = img.convert('RGBA')
#размытие 40 процентов
img = blur(img, 40)
#Выводим изображение
img.show()
