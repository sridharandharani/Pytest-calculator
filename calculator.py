def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y):
    return x/y


if __name__ == "__main__":
    a = int(input("Enter 1st num"))
    b = int(input("Enter 2nd num "))

    addition = add(a, b)
    subraction = sub(a, b)
    multiply = mul(a, b)
    divide = div(a, b)

    print(addition)
    print(subraction)
    print(multiply)
    print(divide)

