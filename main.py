"""
Тестовый калькулятор
"""

def plus(a,b):
    return a+b
#Функция сложения

def minus(a,b):
    return a-b
#Функция разности

def multipl(a,b):
    return a*b
#Функция умножения

def div(a,b):
    if (type(a)==int and type(b)==int):
        return(a//b, a%b)
#Функция целочисленного деления


def hello():
    print(f"Hello, {input('What is your name? ')}!")
#Функция "ПРИВЕТ"


def cringe():
    print("Bruh...")


if __name__ == "__main__":
    print(plus(1,2))
    print(div(4,3))
