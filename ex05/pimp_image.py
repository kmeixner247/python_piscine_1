import numpy as np


def ft_invert(array: np.ndarray) -> np.ndarray:
    """ft_invert(array: np.ndarray) -> np.ndarray

inverts the colors of the input image by substracting all color channels from
255 and returns the inverted image as a new array"""
    changed = np.copy(array)
    try:
        assert type(array) is np.ndarray, "argument must be a np array"
        assert len(array.shape) == 3, "input must be a 3D array"
        assert array.shape[2] == 3, "input array must be RGB"
        height, width, channels = array.shape
        for i in range(height):
            for j in range(width):
                for k in range(channels):
                    changed[i][j][k] = 255 - array[i][j][k]
    except AssertionError as msg:
        print("ft_invert: AssertionError:", msg)
    return changed


def ft_red(array: np.ndarray) -> np.ndarray:
    """ft_red(array: np.ndarray) -> np.ndarray

sets the green and blue channels of the input image to 0, thus only leaving the
reds. Returns the transformed image as a new array"""
    changed = np.copy(array)
    try:
        assert type(array) is np.ndarray, "argument must be a np array"
        assert len(array.shape) == 3, "input must be a 3D array"
        assert array.shape[2] == 3, "input array must be RGB"
        height, width, channels = array.shape
        for i in range(height):
            for j in range(width):
                changed[i][j][1] = 0
                changed[i][j][2] = 0
    except AssertionError as msg:
        print("ft_red: AssertionError:", msg)
    return changed


def ft_green(array: np.ndarray) -> np.ndarray:
    """ft_green(array: np.ndarray) -> np.ndarray

sets the red and blue channels of the input image to 0, thus only leaving the
greens. Returns the transformed image as a new array"""
    changed = np.copy(array)
    try:
        assert type(array) is np.ndarray, "argument must be a np array"
        assert len(array.shape) == 3, "input must be a 3D array"
        assert array.shape[2] == 3, "input array must be RGB"
        height, width, channels = array.shape
        for i in range(height):
            for j in range(width):
                changed[i][j][0] = 0
                changed[i][j][2] = 0
    except AssertionError as msg:
        print("ft_green: AssertionError:", msg)
    return changed


def ft_blue(array: np.ndarray) -> np.ndarray:
    """ft_blue(array: np.ndarray) -> np.ndarray

sets the red and green channels of the input image to 0, thus only leaving the
blues. Returns the transformed image as a new array"""
    changed = np.copy(array)
    try:
        assert type(array) is np.ndarray, "argument must be a np array"
        assert len(array.shape) == 3, "input must be a 3D array"
        assert array.shape[2] == 3, "input array must be RGB"
        height, width, channels = array.shape
        for i in range(height):
            for j in range(width):
                changed[i][j][0] = 0
                changed[i][j][1] = 0
    except AssertionError as msg:
        print("ft_blue: AssertionError:", msg)
    return changed


def ft_grey(array: np.ndarray) -> np.ndarray:
    """ft_grey(array: np.ndarray) -> np.ndarray

sets each color channel of each pixel of the input image to the median of the
three channels. Returns the transformed image as a new array"""
    changed = np.copy(array)
    try:
        assert type(array) is np.ndarray, "argument must be a np array"
        assert len(array.shape) == 3, "input must be a 3D array"
        assert array.shape[2] == 3, "input array must be RGB"
        height, width, channels = array.shape
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
    except AssertionError as msg:
        print("ft_grey: AssertionError:", msg)
    return changed
