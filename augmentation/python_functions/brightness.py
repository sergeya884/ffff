from PIL import Image, ImageEnhance

# Путь до картинки
path="perfect_number/1.bmp"

# Функция изменения яркости
def brightness(img, brightness_level): 
    enhancer = ImageEnhance.Brightness(img)
    return(enhancer.enhance(brightness_level/100))

# Открываем исходную картинку
img = Image.open(path)
# Меняем яркость изображения с фактором 0.5
img=brightness(img,50)
img.show()


