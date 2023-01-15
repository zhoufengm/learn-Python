# 2023.1.4
# 学习元组P42  4-13

# 自助餐食物元组
foods = ("noodles","salad","soup","crab","fish")
print("Original foods are :")
for food in foods:
    print(food)

# 修改元组的值，会报错
# foods[0] = "beaf"
# print(foods[0])

# 直接给元组变量赋值，相当于修改元组值
foods = ("noodles","salad","coke","beaf","fish")
print("Modified foods are :")
for food in foods:
    print(food)

