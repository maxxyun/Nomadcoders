# 5.5 Keyword Arguments

job = soup.find_all('section', class_="jobs")

find_all에는 많은 arguments가 있음(name, attrs, recursive, string, limit..)
class가 job인 section을 다 찾으라고 하는거.
class뒤에 _를 붙인 이유는 class라는 단어는 이미 python에서 사용 (import = 1 이런거 안됨)


def say_hello(name, age):
    print(f"Hello {name} you are {age} years old")


say_hello("nico", 12)
say_hello(age=12, name="nico")