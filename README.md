Аугментация обучающей выборки растровых примеров.

Агафонов Сергей задача 5 на собеседование ИППИ АД.

Цель: написать программу аугментации изображения и создать из одной идеальной фотографии на класс обучающую выборку для классификатора. Обучить классификатор и проверить его эффективность на реальных данных.

Все, что касается аугментации лежит в папке augmentation. Все, что касается классификатора в папке classifier.

1. В качестве инструмента для изменения изображения была выбрана библиотека PILLOW языка python, так как она обладает большим набором функций. Итоговая программа генерирует заданное число изображений на каждое идеальное изображение, лежащее в исходной папке. Генерация случайна, но в заданных настройками рамках.

Реализованы следующие варианты изменения изображения:

1)поворот вокруг центра : rotation.py                     ![](https://github.com/sergeya884/img_augmentation/blob/main/photo/rotation.png)

2)параллельный перенос : transfer.py                      ![](https://github.com/sergeya884/img_augmentation/blob/main/photo/transfer.png)

3)сдвиг : shift.py                                        ![](https://github.com/sergeya884/img_augmentation/blob/main/photo/shift.png)

4)сжатие растяжение вертикально, горизонтально : rsize.py ![](https://github.com/sergeya884/img_augmentation/blob/main/photo/rsize.png)

5)изменение яркости : brightness.py                       ![](https://github.com/sergeya884/img_augmentation/blob/main/photo/brightness.png)

6)случайный шум : noise.py                                ![](https://github.com/sergeya884/img_augmentation/blob/main/photo/noise.png)

7)вертикально-горизонтальный шум : direct_noise.py        ![](https://github.com/sergeya884/img_augmentation/blob/main/photo/direct_noize.png)

8)треугольные изменения яркости : triangle.py             ![](https://github.com/sergeya884/img_augmentation/blob/main/photo/triangle.png)

9)размытие : blur.py                                      ![](https://github.com/sergeya884/img_augmentation/blob/main/photo/blur.png)

В итоге получаем подобный набор файлов

![](https://github.com/sergeya884/img_augmentation/blob/main/photo/aug_exmp.png)

2. Было рассмотрено несколько наборов идеальных изображений, в итоге я остановился на задаче распознавания цифр с автомобильных номеров.

Для оценки эффективности были в ручную вырезанны цифры номеров автомобилей с реальных фотографий

![](https://github.com/sergeya884/img_augmentation/blob/main/photo/test_files)

Идеальные изображения ![](https://github.com/sergeya884/img_augmentation/blob/main/photo/in.png) 

Примеры из обучающей выборки ![](https://github.com/sergeya884/img_augmentation/blob/main/photo/1.png) ![](https://github.com/sergeya884/img_augmentation/blob/main/photo/2.png) ![](https://github.com/sergeya884/img_augmentation/blob/main/photo/3.png)

Примеры из тестовой выборки ![](https://github.com/sergeya884/img_augmentation/blob/main/photo/five_01.png) ![](https://github.com/sergeya884/img_augmentation/blob/main/photo/nine_01.png) ![](https://github.com/sergeya884/img_augmentation/blob/main/photo/one_03.png)

3. Итоги обучения такие. После обучения с аугментацией процент правильных ответов 96, что весьма неплохо, учитывая простоту самой нейросети и наличия целых 10 классов. Обучение только на идеальных примерах дало результат в 62 процентов правильных ответов. Аугментация работает и значительно улучшает результат. 

Кроме того провел исследование об эффективности каждого метода аугментации отдельно. Первая цифра процент успеха у нейросети обученной на всех изменениях кроме указанного, вторая цифра только с указанным. blur 94% 79%, brightness 90% 62%, rsize 91% 81%, direct_noise 90% 83%, noise 93% 64%, rotation 94% 68%, shift 95% 65%, transfer 91% 88%, triangle 93% 64%


