from image import Image

new_image = Image.create(10,10)


new_image.set(5,4,9)

new_image.write_pgm("myimage.pgm")

