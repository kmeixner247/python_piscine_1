import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load


def zoom(img: np.ndarray, p1: tuple, p2: tuple) -> np.ndarray:
    """zoom(img: np.ndarray, p1: tuple, p2: tuple) -> np.ndarray

returns a subset of img, sliced from point p1 to point p2.
Checks if p2 is to the bottom right of p1 and if p1 and p2 are valid coords"""
    try:
        assert type(img) is np.ndarray, "not a valid img"
        assert type(p1) is tuple, "p1 must be tuple"
        assert type(p2) is tuple, "p2 must be tuple"
        assert len(p1) == 2 and len(p2) == 2, "p1 and p2 must be 2D coord"
        (h1, w1), (h2, w2) = p1, p2
        assert 0 <= h1 < h2 <= img.shape[0], "p1 and p2 must be valid coords"
        assert 0 <= w1 < w2 <= img.shape[1], "p1 and p2 must be valid coords"
        assert h1 < h2 and w1 < w2, "p2 must be to the\
bottom right of p1"
    except AssertionError as msg:
        print("zoom: AssertionError:", msg)
        quit()
    return img[h1:h2, w1:w2, :1]


def main():
    """main function of zoom.py. Loads an image, slices it to specified
sizes and displays the image"""
    img = ft_load("animal.jpeg")
    print(img)
    zoomed = zoom(img, (-1, 450), (500, 850))
    print("New shape after slicing:", zoomed.shape, "or", zoomed.shape[:-1])
    print(zoomed)
    plt.imshow(zoomed, cmap='gray')
    plt.show()


if __name__ == "__main__":
    main()
