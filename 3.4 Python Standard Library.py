# 3.4 Python Standard Library
# https://docs.python.org/ko/3/library/index.html

from random import randint

user_choice = int(input("choose number."))
pc_choice = randint(1, 50)

if user_choice == pc_choice:
    print("You won!")
elif user_choice > pc_choice:
    print("Lower! Cpmputer chose", pc_choice)
elif user_choice < pc_choice:
    print("Higher! Computer chose", pc_choice)
