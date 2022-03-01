

def smart_div(func):

    def inner(a, b):
        if b == 0:
            print('cant devide with zero')
            return
        return func(a, b)
    return inner


@smart_div
def div(a, b):
    return a/b

print(div(20, 10))
