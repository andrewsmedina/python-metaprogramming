from functools import wraps


def ensure(func):
    @wraps
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return func


def add(n1: 'positive', n2: 'negative'):
    return n1 + n2


@ensure
def sub(n1: 'positive', n2: 'negative'):
    return n1 - n2


print(add(10, 10))
