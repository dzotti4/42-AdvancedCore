def NULL_not_found(object: any) -> int:
    """Print what kind of null value object is; return 1 if it is none."""
    if object is None:
        print(f"Nothing: {object} {type(object)}")
    elif type(object) is float and object != object:
        print(f"Cheese: {object} {type(object)}")
    elif type(object) is int and object == 0:
        print(f"Zero: {object} {type(object)}")
    elif type(object) is str and object == "":
        print(f"Empty: {type(object)}")
    elif object is False:
        print(f"Fake: {object} {type(object)}")
    else:
        print("Type not Found")
        return 1
    return 0
