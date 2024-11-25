def pylonge_decorator(hi_msg, bye_msg):
    def inner_decorator(f):
        def wrapper(*args):
            print(hi_msg)
            f(*args)
            print(bye_msg)
        return wrapper
    return inner_decorator
