last_input = ""
last_function = ""


def last_call(func):
    def wrapper(*args, **kwargs):
        global last_input
        global last_function
        if last_input == args and last_function == func:
            return "Already seen this input!"
        last_input = args
        last_function = func
        return func(*args, **kwargs)
    return wrapper


@last_call
def f(x):
    return x ** 2


@last_call
def f1(x):
    return x + 5


if __name__ == '__main__':
    print(f(2))
    print(f(2))
    print((f1(2)))
    print(f(x=3))
