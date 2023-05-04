import numpy as np
from load_image import ft_load
import matplotlib.pyplot as plt


def ft_invert(array) -> np.ndarray:
    changed = np.copy(array)
    height, width, channels = array.shape
    for i in range(height):
        for j in range(width):
            for k in range(channels):
                changed[i][j][k] = 255 - array[i][j][k]
    return changed


def ft_red(array) -> np.ndarray:
    changed = np.copy(array)
    height, width, channels = array.shape
    for i in range(height):
        for j in range(width):
            changed[i][j][1] = 0
            changed[i][j][2] = 0
    return changed


def ft_green(array) -> np.ndarray:
    changed = np.copy(array)
    height, width, channels = array.shape
    for i in range(height):
        for j in range(width):
            changed[i][j][0] = 0
            changed[i][j][2] = 0
    return changed


def ft_blue(array) -> np.ndarray:
    changed = np.copy(array)
    height, width, channels = array.shape
    for i in range(height):
        for j in range(width):
            changed[i][j][0] = 0
            changed[i][j][1] = 0
    return changed


def ft_grey(array) -> np.ndarray:
    height, width, channels = array.shape
    changed = np.copy(array)
    for i in range(height):
        for j in range(width):
            r = array[i][j][0]
            g = array[i][j][1]
            b = array[i][j][2]
            if g <= r <= b or b <= r <= g:
                changed[i][j][0] = r
            elif r <= g <= b or b <= g <= r:
                changed[i][j][0] = g
            elif r <= b <= g or g <= b <= r:
                changed[i][j][0] = b
            changed[i][j][1] = changed[i][j][0]
            changed[i][j][2] = changed[i][j][0]
    return changed


def main():
    img = ft_load("landscape.jpg")
    changed = ft_grey(img)
    plt.imshow(changed)
    plt.show()


if __name__ == "__main__":
    main()
