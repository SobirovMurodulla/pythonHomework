def check(func):
    def wrapper(a, b):
        if b == 0:
            return "Denominator can't be zero"
        return func(a, b)
    return wrapper

@check
def div(a, b):
    return int(a / b)

a1,b1 = map(int,input().split())
print(div(a1,b1))