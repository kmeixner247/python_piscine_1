import matplotlib.pyplot as plt
import numpy as np
import PIL


def ft_load(path: str) -> np.ndarray:
    """ft_load(path: str) -> np.ndarray

Load an image into an RGB array and returns it.
Checks for valid path and if the file exists"""
    try:
        assert type(path) is str, "path must be a string"
        img_array = plt.imread(path)
        print("The shape of the image is:", img_array.shape)
    except AssertionError as msg:
        print("ft_load: AssertionError:", msg)
        quit()
    except FileNotFoundError:
        print("ft_load: FileNotFoundError: file %s not found" % path)
        quit()
    except PIL.UnidentifiedImageError:
        print("ft_load: UnidentifiedImageError: %s\
not a valid image or corrupted" % path)
        quit()
    return img_array
