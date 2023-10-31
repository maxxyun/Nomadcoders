# 2.10 Return Values
def tax_calc(money):
    return money * 0.35


def pay_tax(tax):
    print("thank you for paying", tax)


to_pay = tax_calc(150000000)
pay_tax(to_pay)
# 위에 두줄과 아래 한 줄은 같음
pay_tax(tax_calc(150000000))
