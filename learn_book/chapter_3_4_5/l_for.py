# 学习for循环和range函数
'''
# 2023.1.3
# P36 4-1
fruits = ['banana','apple','pear']
for fruit in fruits:
    print('I like ' + fruit + '.')
print('I really like fruits!')

# P36 4-2
animals = ['dog','cat','rabbit']
for animal in animals:
    print('A ' + animal + ' would make a great pet.')
print('Any of these animals would make a great pet!')
'''

'''
# P38 4-3
# 打印数字1-20（含）
for i in range(1,21):
    print(i)
'''

'''
# 打印数字1-1000000（含）
# 若输出时间太长，可以按ctrl+C停止输出，或关闭输出窗口
numbers = []
for i in range(1,1000001):
    # print(i)    # 输出1000000个数字大约需要3分钟
    numbers.append(i)

# 核实列表最大最小值
min = min(numbers)
max = max(numbers)
print('min： ' , min)
print('max： ' , max )

# 4-5 计算列表和，2s不到出结果sum = 500000500000
sum = 0
for i in numbers:
    sum = sum + i
print('sum: ' , sum)
'''

'''
# 4-6 使用步长创建1~20的奇数列表
odd_number = range(1,21,2)
for i in odd_number:
   print(i)

# 4-7 使用步长创建3~30内能被3整除的数列表
odd_number = range(3,30,3)
for i in odd_number:
   print(i)
'''

# 4-8 创建立方列表
cubes = []
for i in range(1,11):
    cubes.append(i**3)

# 4-9 列表解析
# cubes = [value**3 for value in range(1,11)]

print("打印1~10的立方数：")
for i in cubes:
    print(i)