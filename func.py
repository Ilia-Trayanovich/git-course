from deco import pylonge_decorator

@pylonge_decorator("Привет", "Пока")
def func(list):
    return [i**2 for i in list]
