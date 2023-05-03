def slice_me(family: list, start: int, end: int) -> list:
    """slice_me(family: list, start: int, end: int) -> list

Prints the dimensions of the 2D array, then slices it depending
on the start and end inputs, prints the new dimensions and returns
the sliced array"""
    try:
        width = len(family[start])
        height = len(family)
        for n in family:
            assert len(n) is width, "invalid array shape"
        print("My shape is : (%d, %d)" % (height, width))
        sliced = family[start:end]
        print("My new shape is : (%d, %d)" % (len(sliced), len(sliced[0])))
    except IndexError:
        print("slice_me: IndexError: list index out of range")
        quit()
    except AssertionError as msg:
        print("slice_me: AssertionError:", msg)
        quit()
    return sliced
