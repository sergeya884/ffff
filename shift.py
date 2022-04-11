import random
from PIL import Image

# Путь до картинки
path="perfect_number/7.bmp"

# Функция сдвига вдоль x
def shift(img, level):
    img = img.convert('L')
    width, height = img.size
    level = width//2 * level//100
    j = 0
    if(level <= 0): j = -level
    # Сдвигаем по x
    for x in range(0, img.size[0]):
        for y in range(0, img.size[1]):
            bright=img.getpixel((x, y))
            img.putpixel((x - j - level * y//height, y), bright)
	
    # Теперь центрируем
    # Узнаем размеры исходного изображения
    width, height = img.size
    img = img.convert('RGBA')
    # Создаем шаблон белого фона
    dst_img = Image.new("L", (width, height), "white" )
    dst_img.paste(img, (j + level//2, 0), img)
    return(dst_img)

img = Image.open(path)
img = shift(img, 70)
img.show()

