def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        print("Sprinkles are added!!")
        func(*args, **kwargs)
    return wrapper

def add_syrup(func):
    def wrapper(ice_cream_flavour,syrup_flavour):
            print(f"{syrup_flavour} Syrup is added!!")
            func(ice_cream_flavour)
    return wrapper

@add_syrup
@add_sprinkles
def ice_cream(flavour):
    print(f"Here is your ice cream of {flavour} flavour!")

@add_sprinkles
def ice_cream2(flavour):
    print(f"Here is your ice cream of {flavour} flavour!")

ice_cream("chocolate","vanilla")

ice_cream2("chocolate")
