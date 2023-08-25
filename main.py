# # 2.3 Recap
# my_name = "nico"
# age = 12
# dead = False
# print("Hello my name is", my_name)
# print("and I'm", age, "years old")
#
# # 2.4 Functions
# print(True)
# print("hello")
# print(12)
# print(True, "hello", 12)
#
#
# def say_hello():
#   print("hello how R U?")
#
# say_hello()
# say_hello()
# say_hello()
# print("hello world")

# # 2.5 Indentation
# def say_hello():
#   print("hello how R U?")
# def say_bye():
#   print("bye bye")
#
# say_hello()
# say_bye()

# 2.6 Parameters
# def say_hello(user_name):
#   print("hello", user_name, "how R U?")
#
# say_hello("hongku")

# 2.7 Multiple Parameters
# def say_hello(user_name, user_age):
#     print("hello", user_name)
#     print("you are", user_age, "years old")
#
# say_hello("hongku", 12)

# 2.8 Recap
# def tax_calculator(money):
#     print(money * 0.35)
#
# tax_calculator(15000000000000)
# tax_calculator(150)

# 2.9 Default Parameters
# def say_hello(user_name="anonymous"):
#     print("hello", user_name)
#
# say_hello("nico")
# say_hello()


# def plus(a=0, b=0):
#     print(a + b)
#
# def minus(a=0, b=0):
#     print(a - b)
#
# def multiple(a=0, b=0):
#     print(a * b)
#
# def divide(a=0, b=1):
#     print(a / b)
#
# def power(a=0, b=0):
#     print(a ** b)
#
# plus()
# minus()
# multiple()
# divide()
# power()

# 2.10 Return Values
def tax_calc(money):
    return money * 0.35


def pay_tax(tax):
    print("thank you for paying", tax)


to_pay = tax_calc(150000000)
pay_tax(to_pay)
# 위에 두줄과 아래 한 줄은 같음
pay_tax(tax_calc(150000000))
