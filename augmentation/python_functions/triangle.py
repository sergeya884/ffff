from PIL import Image
import random

path="1.png"

# Функция рисования случайных треугольных затемнений
def triangle(img, deviation, quantity):
    img = img.convert('L')
    width, height = img.size
    
    # Пиксель со случайним x
    x_rand = random.randint(0, width)
    brigh_thick = random.randint(0, x_rand)
    bright = random.randint(-deviation, deviation)
    for k in range(0, quantity):
        j = random.randint(0, 3)
        if(j == 0):
            i = 0
            for x in range(0, width):
                i += 1
                if(i > width): break
                for y in range(0, i):
                    img.putpixel((x, y), img.getpixel((x, y)) + bright)
        if(j == 1):
            i = height
            for x in range(0, width):
                i -= 1
                if(i < 0): break
                for y in range(0, i):
                    img.putpixel((x, y), img.getpixel((x, y)) + bright)
        if(j == 2):
            i = 0
            for y in range(0, height):
                i += 1
                if(i > width): break
                for x in range(0, i):
                    img.putpixel((x, y), img.getpixel((x, y)) + bright)
        if(j == 3):
            i = width
            for y in range(0, height):
                i -= 1
                if(i < 0): break
                for x in range(0, i):
                    img.putpixel((x, y), img.getpixel((x, y)) + bright)
    return(img)

# Открываем исходное изображение		
img = Image.open(path)
img = triangle(img, 20, 5)
img.show()
