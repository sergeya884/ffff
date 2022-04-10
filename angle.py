from PIL import Image

src_im = Image.open("convert_per_img/1.png")
angle = 12
size = 240, 320

dst_im = Image.new("RGBA", (240,320), "white" )
im = src_im.convert('RGBA')
rot = im.rotate(angle).resize(size)
dst_im.paste( rot, (0, 0), rot )

dst_im.show()
