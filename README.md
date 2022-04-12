Разработка программы аугментации обучающей выборки и обучения на ней нейросети.

Агафонов Сергей задача 5 на собеседование ИППИ АД.


random_eff.py основная программа, создание заданного числа изображений со случайной комбинацией эффектов.

perfect_car_numbers папка с идеальными цифрами из автомобильных номеров.

number папка с папками для готовых изображений по классам. 

perfect_numbers папака с идеальными цифрами с клавиатуры. 

test папка для тестовых измененных изображений. 

Пример. 

![](https://github.com/sergeya884/img_augmentation/blob/main/tests/0.png) ![](https://github.com/sergeya884/img_augmentation/blob/main/tests/43.png) ![](https://github.com/sergeya884/img_augmentation/blob/main/tests/20.png) ![](https://github.com/sergeya884/img_augmentation/blob/main/tests/49.png)

Варианты изменения картинки:

1)поворот вокруг центра : rotation.py

2)параллельный перенос : transfer.py

3)сжатие растяжение вертикально, горизонтально : rsize.py

4)изменение яркости : brightness.py

6)шум : noise.py

7)размытие : blur.py

8)сдвиг : shift.py
