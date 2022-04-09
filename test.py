import torchvision
from PIL import Image

def deal_single_img(path, deal_function):
	img2 = Image.open(path)
	origin_type = type(img2)
	img2 = deal_function(img2)
	target_type = type(img2)
	img2.show()
	print("{} => {}".format(origin_type, target_type))
	img2.save("tests/1.png")

path='./perfect_numbers/1.bmp'
dfunc = torchvision.transforms.RandomResizedCrop(200, scale=(0.1, 1), ratio=(0.5, 2))
deal_single_img(path, dfunc)
