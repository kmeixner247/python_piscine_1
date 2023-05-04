import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load


def main():
    """main function of rotate.py. Loads specified image, slices it to
specified sizes, rotates it by 90 degrees and displays it"""
    img = ft_load("animal.jpeg")
    img = img[100:500, 450:850, :1]
    print("The shape of the image is:", img.shape, "or", img.shape[:-1])
    print(img)
    height, width = img.shape[:-1]
    transposed = np.zeros((width, height))
    for i in range(height):
        for j in range(width):
            transposed[j, i] = img[i, j]
    print("new shape after transpose:", transposed.shape[:-1])
    print(transposed)
    plt.imshow(transposed, cmap='gray')
    plt.show()


if __name__ == "__main__":
    main()
