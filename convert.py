import torchvision
from PIL import Image

for i in range(0,10):	
	path='./perfect_numbers/'+str(i)+'.bmp'
	img = Image.open(path) 
	grayscale = img.convert('L')
	#grayscale.show()
	path2='convert_per_img/'+str(i)+'.png'
	grayscale.save(path2)
