from PIL import Image, ImageFilter

im = Image.open("Tofik.jpg")
#im.show()

im2 = Image.open("Tofik2.jpg")

im3 = Image.blend(im2, im, 0.9)
#im3.show()

maskImg = Image.open("Tofik.jpg")
maskImg = maskImg.convert("L")

im4 = Image.composite(im2, im, maskImg)
#im4.show()

im4.rotate(90).save('TofikRotate.jpg')
#im4.show()

im.filter(ImageFilter.GaussianBlur(15)).save("TofikBLUR.jpg")