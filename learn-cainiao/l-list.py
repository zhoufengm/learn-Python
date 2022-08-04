#列表推导式list

# [表达式 for 变量 in 列表] 
# [out_exp_res for out_exp in input_list]
# 或者 
# [表达式 for 变量 in 列表 if 条件]
# [out_exp_res for out_exp in input_list if condition]

# out_exp_res：列表生成元素表达式，可以是有返回值的函数。
# for out_exp in input_list：迭代 input_list 将 out_exp 传入到 out_exp_res 表达式中。
# if condition：条件语句，可以过滤列表中不符合条件的值。

#过滤掉长度小于或等于3的字符串列表，并将剩下的转换成大写字母：
names = ['Bob','Tom','Alice','Jerry','Wendy','Smith']
new_names = [name.upper() for name in names if len(name)>3]
print(new_names)

#计算 30 以内可以被 3 整除的整数：
multiples = [i for i in range(30) if i % 3 == 0]
print(multiples)


# 字典推导式

# { key_expr: value_expr for value in collection }
# 或
# { key_expr: value_expr for value in collection if condition }

# 使用字符串及其长度创建字典：
listdemo = ['google','runoob','taobao']
# 将列表中各字符串值为键，各字符串的长度为值，组成键值对
newdict = {key:len(key) for key in listdemo}
print(newdict)
#组成的字典为： {'google': 6, 'runoob': 6, 'taobao': 6}

#提供三个数字，以三个数字为键，三个数字的平方为值来创建字典：
dic = {x:x**2 for x in (2,4,6)}
print(dic)
print(type(dic))


# 集合推导式
# { expression for item in Sequence }
# 或
# { expression for item in Sequence if conditional }

# 计算数字 1,2,3 的平方数：
setnew = {i**2 for i in (1,2,3)}
print(setnew)

#判断不是 abc 的字母并输出：
a = {x for x in 'abracadbara' if x not in 'abc'}
print(a)
print(type(a))



#元组推导式
#元组推导式可以利用 range 区间、元组、列表、字典和集合等数据类型，快速生成一个满足指定需求的元组。
# (expression for item in Sequence )
# 或
# (expression for item in Sequence if conditional )

#生成一个包含数字 1~9 的元组
a = (x for x in range (1,10))
print('a is : ',a)  # 返回的是生成器对象
print(tuple(a))     # 使用 tuple() 函数，可以直接将生成器对象转换成元组