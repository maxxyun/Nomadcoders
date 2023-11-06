# 4.3 Dicts {}

player = {
    "name": "nico",
    "age": 12,
    # 'alive':True
    "fav_food": ["🍕", "🍔"],
}

print(player)
print(player.get("age"))
print(player.get("fav_food"))
print(player["fav_food"])

print(player)
player.pop("age")  # age를 지움
print(player)

print(player)
player["xp"] = 1500  # 추가
print(player)

print(player)
player["fav_food"].append("☕")
print(player.get("fav_food"))
print(player["fav_food"])
