# импортируем необходимые пакеты
from keras.models import load_model
import argparse
import pickle
import cv2
import os

path = 'images/'
pers=0
for filename in os.listdir(path):
    print("-----------------------------------------")
    print(filename)
    # загружаем входное изображение и меняем его размер на необходимый
    image = cv2.imread(path + filename)
    output = image.copy()
    image = cv2.resize(image, (30, 50))
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # масштабируем значения пикселей к диапазону [0, 1]
    image = image.astype("float") / 255.0
    
    # сглаживаем изображение и добавляем размер пакета
    image = image.flatten()
    image = image.reshape((1, image.shape[0]))
    	
    # загружаем модель и бинаризатор меток
    #print("[INFO] loading network and label binarizer...")
    model = load_model('output_good/simple_nn.model')
    lb = pickle.loads(open("output_good/simple_nn_lb.pickle", "rb").read())
    	
    # делаем предсказание на изображении
    preds = model.predict(image)
    	
    # находим индекс метки класса с наибольшей вероятностью соответствия
    i = preds.argmax(axis=1)[0]
    label = lb.classes_[i]
    
    # рисуем метку класса + вероятность на выходном изображении
    text = "{}: {:.2f}%".format(label, preds[0][i] * 100)
    print(text)
    if label == filename[:-7]: 
        print('Ok')
        pers = pers + 1
    print(pers)
