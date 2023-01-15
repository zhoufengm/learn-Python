# 2023.1.4 第五章 
# P46 5-1 条件语句

'''
# 5-1 布尔表达式
car = 'subaru'
print("Is car == 'subaru' ? I predict True.")
print(car == 'subaru')

print("Is car == 'audi' ? I predict False.")
print(car == 'audi')

# 5-2
print('a' == 'A')
print('b1' == 'b1')
print('hhh' != 'hh')


str1 = 'nnnn'
str2 = 'NNNn'
print(str1 == str2)
# lower()将字符串全部转化为小写
print(str1 == str2.lower())
'''

# 数字比较

a = 1
b = 5

# 不等号
if a == b:
    print(" a == b")
elif a < b:
    print(" a < b")
else:
    print(" a > b")

# and or
if a < 10 and b < 10:
    print("a,b都小于10")
elif a >= 10 and b >=10:
    print("a,b都大于或等于10")
else:
    print("a,b一大一小")

# 包含 in   not in
num = [23,45,19,80]
if 25 in num:
    print('found 25')
else:
    print('Not found 25')

if 80 not in num:
    print('Not found 80')
else:
    print('Found 80')