# # 2.3 Recap
# my_name = "nico"
# age = 12
# dead = False
# print("Hello my name is", my_name)
# print("and I'm", age, "years old")


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
# def tax_calc(money):
#     return money * 0.35
#
# def pay_tax(tax):
#     print("thank you for paying", tax)
#
# to_pay = tax_calc(150000000)
# pay_tax(to_pay)
# # 위에 두줄과 아래 한 줄은 같음
# pay_tax(tax_calc(150000000))


# 2.11 Return Recap
# my_name = "nico"
# my_age = 12
# my_color_eyes = "brown"
#
# print(
#     f"Hello. I'm {my_name}, I have {my_age} years in the earth, {my_color_eyes} is my eye color"
# )


# def make_juice(fruit):
#     return f"{fruit}+🥤"
#
# def add_ice(juice):
#     return f"{juice}+🧊"
#
# def add_sugar(iced_juice):
#     return f"{iced_juice}+🍭"
#
# juice = make_juice("🍎")
# cold_juice = add_ice(juice)
# perfect_juice = add_sugar(cold_juice)
#
# print(perfect_juice)


# 3.0 If
# a = "nico"
# if 10 == "nico":  # a = 10  10을 a에 넣겠다.
#     print("Correct!")


# 3.1 Else & Elif
# password_correct = False
# if password_correct:
#     print("Here is your money")
# else:
#     print("Wrong password")

# winner = 10
# if winner > 10:
#     print("Winner is greater than 10")
# elif winner <= 10:
#     print("Winner is less than 10")
# else:
#     print("Winner is 10")


# 3.2 Recap
# winner = 50           # >, <, >=, <=, ==, !=
# if winner != 10:
#     print("If")
# elif winner <= 25:
#     print("elif")
# elif winner == 0:
#     print("elif 2")
# elif winner == 50:
#     print("elif 3")
# else:
#     print("Else")


# 3.3 And & Or
# age = int(input("How old are you?"))
# if age < 18:
#     print("You can't drink.")
# elif age >= 18 and age <= 35:  # 18 <= age <= 35:
#     print("You drink beer!")
# elif age == 60 or age == 70:
#     print("Birthday party!!")
# else:
#     print("Go ahead!")
#
# True and True == True
# True and False == False
# False and True == False
# False and False == False
#
# True or True == True
# True or False == True
# False or True == True
# False or False == False


# 3.4 Python Standard Library
# https://docs.python.org/ko/3/library/index.html

"""
from random import randint

user_choice = int(input("choose number."))
pc_choice = randint(1, 50)

if user_choice == pc_choice:
    print("You won!")
elif user_choice > pc_choice:
    print("Lower! Cpmputer chose", pc_choice)
elif user_choice < pc_choice:
    print("Higher! Computer chose", pc_choice)
"""

# 3.5 While

# distance = 0
#
# while distance < 20:
#     print("I'm running", distance, "km")
#     distance = distance + 1

# 3.6 Python Casino

# from random import randint
#
# print("Welcome to Python Casino")
# pc_choice = randint(1, 100)
#
# playing = True
#
# while playing:
#     user_choice = int(input("Choose number (1-100) :"))
#     if user_choice == pc_choice:
#         print("You won!")
#         playing = False
#     elif user_choice > pc_choice:
#         print("Lower!")
#     elif user_choice < pc_choice:
#         print("Higher!")

# 3.7 Recap

# from random import randint
#
# print("Welcome to Python Casino")
# pc_choice = randint(1, 100)
#
# playing = True
#
# while playing:
#     user_choice = int(input("Choose number (1-100) :"))
#     if user_choice == pc_choice:
#         print("You won!")
#         playing = False
#     elif user_choice > pc_choice:
#         print("Lower!")
#     elif user_choice < pc_choice:
#         print("Higher!")

# 4.0 Methods
#  data structure : 데이터를 구조화 할때 사용 3종
# 1. list
# 2. tuple
# 3. dictionary

# days_of_week = "Mon, Tue, Wed, Thu, Fri"
# print (days_of_week)

# days_of_week = ["Mon","Tue","Wed","Thur","Fri"]
# print(days_of_week)

# name = "nico"
# print(name.endswith("o"))

# 4.1 Lists

# days_of_week = ["Mon","Tue","Wed","Thur","Fri", 1, 2, 3, True, False, "hi", "black", [1, 2, 3, [False, True]]]
#
# print(days_of_week)
#
# days_of_week.append("Sat")
# print(days_of_week)
#
# days_of_week.append("Sun")
# print(days_of_week)
#
# print(days_of_week[1])
# print(days_of_week[2])

# 4.2 Tuples

# days = ("Mon", "Tue", "Wed")    # 튜플은 내부 데이터를 변경하지 못한다. .count랑 .index만 사용 가능.
#
# print(days[-2])  # 튜플은 괄호가 리스트랑 반대. 만들때는 ( ) 뭔가 할때는 [ ] 를 쓴다.

# 4.3 Dicts

# player={
#      'name':'nico',
#      'age':12,
#      # 'alive':True
#      'fav_food': ["🍕","🍔"]
#  }
#
# print(player)
# print(player.get('age'))
# print(player.get('fav_food'))
# print(player['fav_food'])
#
# print(player)
# player.pop('age')  # age를 지움
# print(player)
#
# print(player)
# player['xp']=1500  # 추가
# print(player)
#
# print(player)
# player['fav_food'].append("☕")
# print(player.get('fav_food'))
# print(player['fav_food'])

# 4.4 Recap
# # 콤마 다음으로 오는건 메소드
# print("nico".endswith("a"))
#
# # 리스트 [변경 가능]
# numbers =[5,3,1,5,7,3,"True", True, 12]
# numbers.append(["🍕","🍔"])
# print(numbers)
# print(numbers[-1])

# # 튜플 (변경 제한)
# numbers=(1,2,3,4,5,True,"xxxxx")
# print(numbers[-1])

# # 딕셔너리 {key:value}
# player={
#     "name":"nico",
#     "age":12,
#     "alive":True,
#     "fav_food": ("🍕","🍔"),
#     "friend":{
#         "name":"lynn",
#         "fav_food":["🍎"]
#     }
# }
# player["fav_food"]="🥐"
# player.pop("alive")
# print(player["friend"]["fav_food"])
# player["friend"]["fav_food"].append("🍌")
# print(player["age"])
# print(player["friend"]["fav_food"])
# print(player["fav_food"])
# print(player)

## 4.5 For Loops (07:26)
# websites = ("google.com", "airbnb.com", "twitter.com", "facebook.com", "tiktok.com")
#
# for potato in websites:
#     print("potato is equals to", potato)
#     print("hello", potato)

## 4.6 URL Formatting
# websites = (
#     "google.com",
#     "airbnb.com",
#     "https://twitter.com",
#     "facebook.com",
#     "https://tiktok.com",
# )
# for website in websites:
#     if not website.startswith(
#         "https://"
#     ):  # => if website.startswith("https://")==False:
#         website = f"https://{website}"
#     print(website)

# 4.7 Requests
# https://www.pypi.org  Python Standard Library에 포함되지 않은 package를 찾는 곳.

# import requests
#
# websites = (
#     "google.com",
#     "airbnb.com",
#     "https://twitter.com",
#     "facebook.com",
#     "https://tiktok.com",
# )
# for website in websites:
#     if not website.startswith(
#         "https://"
#     ):  # => if website.startswith("https://")==False:
#         website = f"https://{website}"
#     print(website)

# # 4.8 Status Codes
# # https://developer.mozilla.org/ko/docs/Web/HTTP/Status     http의 상태 코드
# # HTTP Status 코드 정리글입니다.
# # https://www.whatap.io/ko/blog/40
# #
# # 1XX : Information responses
# # 2XX : Successful responses
# # 3XX : Redirection messages
# # 4XX : Client error responses
# # 5XX : Server error reponses
#
# from requests import get
#
# websites = (
#     "google.com",
#     "airbnb.com",
#     "https://twitter.com",
#     "facebook.com",
#     "https://tiktok.com",
# )
#
# results = {}
#
# for website in websites:
#     if not website.startswith(
#         "https://"
#     ):  # => if website.startswith("https://")==False:
#         website = f"https://{website}"
#     response = get(website)
#     if response.status_code == 200:
#         results[website] = "OK"
#     else:
#         results[website] = "FAILED"
# print(results)

# 4.9 Recap
from requests import get

websites = (
    "google.com",
    "airbnb.com",
    "https://twitter.com",
    "facebook.com",
    "https://tiktok.com",
)

results = {}

for (
    website
) in (
    websites
):  # 현재 실행중인 item에 접근하는 방법으로 variable(website)을 만든다. 한번에 모두 가져오는게 아닌 한개씩 가져온다.
    if not website.startswith(
        "https://"
    ):  # => if website.startswith("https://")==False:
        website = f"https://{website}"  # f를 사용해 번수를 안에 넣을 수 있음
    response = get(website)
    if response.status_code >= 500:
        results[website] = "서버에러응답"
    elif response.status_code >= 400:
        results[website] = "클라이언트 에러 응답"
    elif response.status_code >= 300:
        results[website] = "리다이렉션 메시지"
    elif response.status_code >= 200:
        results[website] = "성공응답"
    elif response.status_code >= 100:
        results[website] = "정보응답"
    else:
        results[website] = "FAILED"
print(results)

# 5.1 Introduction (03:02)
