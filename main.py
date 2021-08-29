from PIL import Image

def imgPixelValues(im):
    for y in range(im.height):
        for x in range(im.width):
            coordinate = (x, y)
            print(im.getpixel(coordinate))

if __name__ == "__main__":
    with Image.open("testImage1.png") as im:
        imgPixelValues(im)