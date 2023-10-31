# 3.0 If
a = "nico"
if 10 == "nico":  # a = 10  10을 a에 넣겠다.
    print("Correct!")


3.1 Else & Elif
password_correct = False
if password_correct:
    print("Here is your money")
else:
    print("Wrong password")

winner = 10
if winner > 10:
    print("Winner is greater than 10")
elif winner <= 10:
    print("Winner is less than 10")
else:
    print("Winner is 10")