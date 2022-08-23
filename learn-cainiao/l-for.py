# 2022.8.23
# for iterating_var in sequence:
#    statements(s)

for letter in 'Python':
    print("当前字母 ： %s" % letter)

fruits = ['banana','apple','mango']
for fruit in fruits:
    print('当前水果 ： %s' % fruit)
print("Good bye!")

# 函数 len() 返回列表的长度，即元素的个数。 range返回一个序列的数
for index in range(len(fruits)):
    print('当前水果 ： %s ' % fruits[index])
print("Good bye!")

# 循环使用 else 语句
# 迭代 10 到 20 之间的数字,找质数
for num in range(10,20):
    for i in range(2,num):
        if num % i == 0:        # 确定第一个因子
            j = num / i         # 计算第二个因子
            print('%d 等于 %d * %d ' % (num,i,j))
            break
    else:
        print('%d 是一个质数' % num)

# 循环嵌套
# 输出2~100之间的素数：
i = 2
while( i < 100 ):
    j = 2
    while( j <= (i/j) ):
        if not( i%j ): break
        j = j + 1
    if ( j > i/j ): print(i," 是素数")
    i = i + 1

print("Good bye!")