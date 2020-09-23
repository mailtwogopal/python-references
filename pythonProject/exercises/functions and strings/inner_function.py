def outer(a, b):
    def inner(e, f):
        return e + f

    c = inner(a, b)
    return c + 5


print(outer(2, 3))
