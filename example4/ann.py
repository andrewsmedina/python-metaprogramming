from functools import wraps


def ensure(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        for attr, value in func.__annotations__:
            pass
        return func(*args, **kwargs)
    return wrapper


@ensure
def add(n1: 'positive', n2: 'negative'):
    return n1 + n2


@ensure
def sub(n1: 'positive', n2: 'negative'):
    return n1 - n2


print(add(10, 10))
