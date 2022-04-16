import random
import os
import sys
from PIL import Image, ImageFilter, ImageEnhance

#НАСТРОЙКИ-----------------------
width = 60                  # ширина картинки на выходе
height = 100                # высота картинки на выходе
triangle_deviation = 20     # отклонение яркости в треугольных помехах
triangle_quantity = 5       # количество треугольных помех
direct_level = 80           # Отклонение яркости вертикально-горизонтального шума
shift_level = 50            # максимальный уровень сдвига в процентах
rotation_level = 5          # предельный угол поворота в градусах
compr_stretch_level_x = 20  # максимальное сжатие по x в процентах от ширины 
compr_stretch_level_y = 20  # максимальное сжатие по y в процентах от длины
transfer_level = 20         # максимальный перенос в процентах от размеров
noise_quantity = 60         # количество шума в процентах от количества пикселей 
noise_deviation = 60        # степень отклонения яркости цвета в шуме от 0 до 255
brightness_level = 30       # максимальный уровень изменения яркости в процентах
blur_level = 30             # максимальный уровень размытия в процентах
#--------------------------------


# Функция размытия изображения
def blur(img,percent):
    return(img.filter(ImageFilter.BoxBlur(int(13*percent/100))))

# Функция поворота изображения на заданный угол
def rotation(img, angle):
    img = img.convert('RGBA')
    # Узнаем размеры исходного изображения
    width, height = img.size
    # Создаем шаблон белого фона
    dst_img = Image.new("L", (width, height), "white" )
    # Поворачиваем исходное изображение
    img = img.rotate(angle)
    # Подставляем измененное изображение на фон
    dst_img.paste(img, (0, 0), img)
    return(dst_img)

# Функция сжатия, растяжения картинки в процентном соотношении без изменения размера
def compr_stretch(img, width_percent, height_percent):
    img = img.convert('RGBA')
    # Узнаем размеры исходного изображения
    width, height = img.size
    # Создаем шаблон белого фона
    dst_img = Image.new("L", (width, height), "white")
    # Считаем повые размеры как процент от старых
    new_width = width*(100-width_percent)//100
    new_height = height*(100-height_percent)//100
    # Меняем размер исходного изображения
    img = img.resize((new_width, new_height))
    # Подставляем измененное изображение на фон
    dst_img.paste(img, ((width - new_width)//2, (height - new_height)//2), img)
    return(dst_img)

# Функция параллельного переноса картинки в процентном соотношении от размеров
def transfer(img, width_percent, height_percent):
    img = img.convert('RGBA')
    # Узнаем размеры исходного изображения
    width, height = img.size
    # Создаем шаблон белого фона
    dst_img = Image.new("L", (width, height), "white" )
    # Перенос как процент от размеров
    new_width = width*width_percent//100
    new_height = height*height_percent//100
    # Переносим изображение относительно фона
    dst_img.paste(img, (new_width//2, new_height//2), img)
    return(dst_img)

# Функция изменения яркости
def brightness(img, brightness_level): 
    enhancer = ImageEnhance.Brightness(img)
    return(enhancer.enhance(brightness_level/100))

# Функция добавления случайного шума
def noise(img, noise_quantity, noise_deviation):
    img = img.convert('L')
    # Узнаем размеры исходного изображения
    width, height = img.size
    for numpix in range(0, noise_quantity*width*height//100):
        # Случайный пиксель
        x=random.randint(2, img.size[0]-3)
        y=random.randint(2, img.size[1]-3)
        # Узнаем яркость
        bright = img.getpixel((x, y))
        # Случайно меняем яркость в заданном пределе
        bright=random.randint(bright-noise_deviation,bright+noise_deviation)
        # Меняем яркость квадрата со стороной от 1 до 5 с пикселем в центре
        for x_1 in range(x, x + random.randint(0, 3)):
            for y_1 in range(y, y + random.randint(0,3)):
                img.putpixel((x_1, y_1), bright)
    return(img)

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

# Функция для вывода с заменой старой информации
def update_msg(text):
    message = f'\r{text}'
    sys.stdout.write(message)
    sys.stdout.flush()

path_to_perfect = input("Введите путь до изображений: ") + '/'
number_of_images = int(input("Введите число изменненых изображений: "))+1;
path_to_save = input("Введите название директории для хранения измененных изображений: ") + '/'
os.mkdir(path_to_save)

for filename in os.listdir(path_to_perfect):
    # Узнаем имя класса как название файла
    name = os.path.splitext(filename)[0]
    print("\nкласс:", name)
    # Создаем папку для изображений класса
    path_to_dir = path_to_save + name + "/"
    os.mkdir(path_to_dir)
    # Создаем основу для будущего пути до картинки
    path_to_img = path_to_dir + name + "_0000"
    j=10
    
    # Переменные для вывода процента готовности
    ready = number_of_images//100
    ready_percent = 0

    # Открываем идеальное изображение
    per_img = Image.open(path_to_perfect + filename)
    per_img = per_img.resize((width, height))

    # Циклическое сохранение случайно измененных параметров
    for i in range(1, number_of_images):
        img = per_img
        #img.show()
        img = brightness(img, random.randint(100-brightness_level, 100+brightness_level))
        img = triangle(img, random.randint(0, triangle_deviation), random.randint(0, triangle_quantity))
        img = direct_noise(img, random.randint(0, direct_level))
        img = shift(img, random.randint(-shift_level, shift_level))
        img = rotation(img, random.randint(-rotation_level, rotation_level))
        img = compr_stretch(img, random.randint(-compr_stretch_level_x, compr_stretch_level_x), random.randint(-compr_stretch_level_y, compr_stretch_level_y))
        img = transfer(img, random.randint(-transfer_level, transfer_level), random.randint(-transfer_level, transfer_level))
        img = noise(img, random.randint(0, noise_quantity), noise_deviation)
        img = brightness(img, random.randint(100-brightness_level, 100+brightness_level))
        img = triangle(img, random.randint(0, triangle_deviation), random.randint(0, triangle_quantity))
        img = blur(img, random.randint(0, blur_level))
        img = img.convert('L')
        
        # Каждую степень 10 нам надо убрать ноль в имени класса
        if i == j:
            j *= 10
            path_to_img = path_to_img[:-1]
        # Выводим процент готовых картинок
        if i == ready:
            ready += number_of_images//100
            ready_percent += 1
            update_msg(str(ready_percent) + "%")
        
        # Сохраняем изображение
        path_to_img_2 = path_to_img + str(i) + '.png'
        #img.show()
        img.save(path_to_img_2)
print('\n')
	


