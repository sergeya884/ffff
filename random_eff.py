import random
import os
import sys
from PIL import Image, ImageFilter, ImageEnhance

#НАСТРОЙКИ-----------------------
width = 60                  # ширина картинки на выходе
height = 100                # высота картинки на выходе
shift_level = 80            # максимальный уровень сдвига в процентах
rotation_level = 5          # предельный угол поворота в градусах
compr_stretch_level_x = 20  # максимальное сжатие по x в процентах от ширины 
compr_stretch_level_y = 20  # максимальное сжатие по y в процентах от длины
transfer_level = 20         # максимальный перенос в процентах от размеров
noise_quantity = 40         # количество шума в процентах от количества пикселей 
noise_deviation = 80        # степень отклонения яркости цвета в шуме от 0 до 255
brightness_level = 50       # максимальный уровень изменения яркости в процентах
blur_level = 50             # максимальный уровень размытия в процентах
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
        for x_1 in range(x - random.randint(0, 2),x + random.randint(0, 2)):
            for y_1 in range(y - random.randint(0,2),y + random.randint(0,2)):
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

# Функция для вывода с заменой старой информации
def update_msg(text):
    message = f'\r{text}'
    sys.stdout.write(message)
    sys.stdout.flush()


path = input("Введите путь до изображений: ")
number_of_images = int(input("Введите число изменненых изображений: "))+1;

for filename in os.listdir(path):
    # Узнаем имя класса как название файла
    name = os.path.splitext(filename)[0]
    print("\nкласс:", name)
    # Создаем папку для изображений класса
    path2 = "numbers/" + name + "/"
    os.mkdir(path2)
    # Создаем основу для будущего пути до картинки
    path2 = path2 + name + "_0000"
    j=10
    
    # Переменные для вывода процента готовности
    ready = number_of_images//100
    ready_percent = 0

    # Циклическое сохранение случайно измененных параметров
    for i in range(1, number_of_images):
        img = Image.open(path + filename)
        img = img.resize((width, height))
        img = shift(img, random.randint(-shift_level, shift_level))
        img = rotation(img, random.randint(-rotation_level, rotation_level))
        img = compr_stretch(img, random.randint(-compr_stretch_level_x, compr_stretch_level_x), random.randint(-compr_stretch_level_y, compr_stretch_level_y))
        img = transfer(img, random.randint(-transfer_level, transfer_level), random.randint(-transfer_level, transfer_level))
        img = noise(img, random.randint(0, noise_quantity), noise_deviation)
        img = brightness(img, random.randint(100-brightness_level, 100+brightness_level))
        img = blur(img, random.randint(0, blur_level))
        img = img.convert('L')
        
        # Каждую степень 10 нам надо убрать ноль в имени класса
        if i == j:
            j *= 10
            path2 = path2[:-1]
        # Выводим процент готовых картинок
        if i == ready:
            ready += number_of_images//100
            ready_percent += 1
            update_msg(str(ready_percent) + "%")
        
        # Сохраняем изображение
        path3 = path2 + str(i) + '.png'
        img.save(path3)
print('\n')
	


