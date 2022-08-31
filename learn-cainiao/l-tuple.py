#元组推导式
# 与列表类似，不同之处在于元组的元素不能修改
# 元组使用小括号，列表使用方括号
# 元组推导式可以利用 range 区间、元组、列表、字典和集合等数据类型，快速生成一个满足指定需求的元组。
# (expression for item in Sequence )
# 或
# (expression for item in Sequence if conditional )

#生成一个包含数字 1~9 的元组
a = (x for x in range (1,10))
print('a is : ',a)  # 返回的是生成器对象
print(tuple(a))     # 使用 tuple() 

# 创建空元组
tup4 = ()
# 元组中只包含一个元素时，需要在元素后面添加逗号
tup4 = (50,)
print(tup4)

# 元组中的元素值是不允许修改,可以对元组进行连接组合
tup1 = ('physics','chemistry',1997,2000)
tup2 = (1,2,3,4,5)
tup3 = "a","b","c","d"
print('tup1 = ' ,tup1)
print('tup2 = ' ,tup2)
print('tup3 = ' ,tup3)

# 以下修改元组元素操作是非法的。
# tup1[0] = 100

# 元组运算符
tup4 = tup1 + tup2
print('tup1 + tup2 = ',tup4)
print('the length of tup3 is ',len(tup3))
print('tup3 * 2 = ',tup3*2)
if 3 in tup2:
    print ('3 is in tup2')
else:
    print('3 is not in tup2')

for x in tup3:print(x)

# 元组索引，截取
print('tup1[1] = ',tup1[1])     #读取第二个元素
print('tup1[-1] = ',tup1[-1])   #方向读取，倒数第一个元素
print('tup1[1:] = ',tup1[1:])   #截取元素

# 删除元组
# 元组中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组
del tup4
# print(tup4)

# 元组内置函数
# print(cmp(tup1,tup2))   #Python 3已经弃用了此函数

print('the max in tup2 is ',max(tup2))
print('the min in tup2 is ',min(tup2))

list = {6,7}
tup4 = tup2 + tuple(list)
print('tup4 = ',tup4)
