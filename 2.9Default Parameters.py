# 2.9 Default Parameters
def say_hello(user_name="anonymous"):
    print("hello", user_name)


say_hello("nico")
say_hello()


def plus(a=0, b=0):
    print(a + b)


def minus(a=0, b=0):
    print(a - b)


def multiple(a=0, b=0):
    print(a * b)


def divide(a=0, b=1):
    print(a / b)


def power(a=0, b=0):
    print(a**b)


plus()
minus()
multiple()
divide()
power()
