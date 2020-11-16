from images import Image
image = Image("smokey.gif")
(r, g, b) = image.getPixel(0, 0)


def grayscale(image):
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            (r, g, b) = image.getPixel(x, y)
            r = int(r * 0.299)
            g = int(g * 0.587)
            b = int(b * 0.114)
            lum = r + g + b
            image.setPixel(x, y, (lum, lum, lum))


average = (r + g + b) // 3


image.draw()
newImage = image.clone()
newImage.draw()
grayscale(newImage)
newImage.draw()
image.draw()