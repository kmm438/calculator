import math


def addition(a, b):
    return a + b


def subtract(a, b):
    return b - a


def multiply(a, b):
    return a * b


def divide(a, b):
    return round((b / a), 9)


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

    def multiply(self, a, b):
        self.result = multiply(a, b)
        return self.result

    def divide(self, a, b):
        self.result = divide(a, b)
        return self.result

    def square(self, a):
        self.result = square(a)
        return self.result

    def sqrt(self, a):
        self.result = sqrt(a)
        return self.result