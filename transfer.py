from PIL import Image
path="perfect_number/1.bmp"

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

# Открываем исходное изображение		
img = Image.open(path)
# Переносим исходное изображение на -10 процентов по горизонтали и на 20 по вертикали
img=transfer(img, -10, 20)
img.show()

