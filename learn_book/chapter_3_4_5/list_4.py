# P41 4-10
# 列表切片
cubes = [value**3 for value in range(1,11)]
print(" The first three items in the list are : ",cubes[:3])

print("Three items from the middle of the list are :",cubes[3:6])

# 使用[-3:]始终打印列表最后三个元素
print("The last three items in the list are : ",cubes[-3:])


# 4-11
my_fruits = ['banana','apple','pear']

# friend_fruits = my_fruits   # 这种方式只是指向同一个列表

# 复制列表，变成两个不同列表
friend_fruits = my_fruits[:]

# 给两个列表添加不同元素
my_fruits.append('strawberry')
friend_fruits.append('grape')

# 直接打印
print('My favorite fruits are : ',my_fruits[:])

print("My friend's favorite fruits are : ")
# 使用for打印
for f in friend_fruits:
    print(f)