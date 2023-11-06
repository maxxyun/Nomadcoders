# 4.4 Recap
# 콤마 다음으로 오는건 메소드
print("nico".endswith("a"))

# 리스트 [변경 가능]
numbers = [5, 3, 1, 5, 7, 3, "True", True, 12]
numbers.append(["🍕", "🍔"])
print(numbers)
print(numbers[-1])

# 튜플 (변경 제한)
numbers = (1, 2, 3, 4, 5, True, "xxxxx")
print(numbers[-1])

# 딕셔너리 {key:value}
player = {
    "name": "nico",
    "age": 12,
    "alive": True,
    "fav_food": ("🍕", "🍔"),
    "friend": {"name": "lynn", "fav_food": ["🍎"]},
}
player["fav_food"] = "🥐"
player.pop("alive")
print(player["friend"]["fav_food"])
player["friend"]["fav_food"].append("🍌")
print(player["age"])
print(player["friend"]["fav_food"])
print(player["fav_food"])
print(player)
