"""
Тестовый калькулятор
"""

def plus(a,b):
    return a+b


def minus(a,b):
    return a-b


def multipl(a,b):
    return a*b


def div(a,b):
    if (type(a)==int and type(b)==int):
        return(a//b, a%b)

if __name__ == "__main__":
    print(plus(1,2))
    print(div(4,3))
