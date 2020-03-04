import math


def addition(a, b):
    return a + b


def subtract(a, b):
    return b - a


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def square(a):
    return a * a


def sqrt(a):
    return math.sqrt(a)


class Calculator:
    result = 0

    def __init__(self):
        #x = 2 + 2;
        #self.result = x;
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = subtract(a, b)
        return self.result
