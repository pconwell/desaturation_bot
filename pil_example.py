from PIL import Image, ImageEnhance

#Open image using Image module
img = Image.open("./desat_before.jpg")

# desharpen and desaturate
img = ImageEnhance.Sharpness(img).enhance(.6)
img = ImageEnhance.Color(img).enhance(.4)
img.save("./desat_after.jpg")
