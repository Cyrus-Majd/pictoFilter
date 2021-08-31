from PIL import Image
import numpy as np

def imgPixelValues(im):
    for y in range(im.height):
        for x in range(im.width):
            coordinate = (x, y)
            print(im.getpixel(coordinate))

def compartmentalize():
    array = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]
    array = np.random.randint(0, 100, (16, 16))
    # Get the shape of the array
    shape = array.shape
    # Get the number of rows and columns in the array
    rows = shape[0]
    cols = shape[1]
    # Get the number of 2x2 squares in the array
    squares = rows / 4
    # Create an empty list to hold the coordinates
    coords = []
    # Loop through the number of squares
    for i in range(int(squares)):
        # Get the top left corner of the square
        x = int(i / cols) * 2
        y = (i % cols) * 2
        # Get the bottom right corner of the square
        x2 = x + 2
        y2 = y + 2
        # Append the coordinates to the list
        coords.append

    print(coords)
    

if __name__ == "__main__":
    compartmentalize()
    # with Image.open("test2.png") as im:
    #     imgPixelValues(im)