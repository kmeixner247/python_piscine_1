def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    """give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]

Calculates and returns an array of BMIs from the given height and weight arrays.
Gives Assertion Errors in case of mismatching arrays, zero heights or invalid types"""
    try:
        assert type(height) is list, "height array must be a list"
        assert type(weight) is list, "weight array must be a list"
        assert len(height) == len(weight), "height and weight have different sizes"
        bmis = [w / (h**2) for (w, h) in zip(weight, height)]
    except TypeError:
        print("give_bmi: TypeError: arrays contain invalid types")
        quit()
    except ZeroDivisionError:
        print("give_bmi: ZeroDivisionError: height cannot include any zero")
        quit()
    except AssertionError as msg:
        print("give_bmi: Assertion Error:", msg)
        quit()
    return bmis

def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """apply_limit(bmi: list[int | float], limit: int) -> list[bool]
    
Returns a list of booleans, where each element represents whether the respective
element in the bmi list if bigger than the limit"""
    try:
        assert type(limit) is int, "limit variable must be int"
        assert type(bmi) is list, "bmi variable must be a list"
        bools = [b > limit for b in bmi]
    except TypeError:
        print("apply_limit: Type Error: invalid type in bmi list")
        quit()
    except AssertionError as msg:
        print("apply_limit: Assertion Error:", msg)
        quit()
    return bools