from PIL import Image
import random

path="1.png"

# Функция вертикально-горизонтальных помех
def direct_noise(img, deviation):
    img = img.convert('L')
    width, height = img.size
    bright = random.randint( - deviation, deviation)

    # Горизонтальные помехи
    for y in range(0, height):
        for x in range(- random.randint(0, width), random.randint(0, width)):
            img.putpixel((x, y), img.getpixel((x, y)) + bright)
    # Вертикальные помехи
    for x in range(0, width):
        for y in range(- random.randint(0, height), random.randint(0, height)):
            img.putpixel((x, y), img.getpixel((x, y)) + bright)
    return(img)

# Открываем исходное изображение		
img = Image.open(path)
img = direct_noise(img, 20)
img.show()
