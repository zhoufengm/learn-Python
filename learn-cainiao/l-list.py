#列表推导式list

# [表达式 for 变量 in 列表] 
# [out_exp_res for out_exp in input_list]
# 或者 
# [表达式 for 变量 in 列表 if 条件]
# [out_exp_res for out_exp in input_list if condition]

# out_exp_res：列表生成元素表达式，可以是有返回值的函数。
# for out_exp in input_list：迭代 input_list 将 out_exp 传入到 out_exp_res 表达式中。
# if condition：条件语句，可以过滤列表中不符合条件的值。
'''
#过滤掉长度小于或等于3的字符串列表，并将剩下的转换成大写字母：
names = ['Bob','Tom','Alice','Jerry','Wendy','Smith']
new_names = [name.upper() for name in names if len(name)>3]
print(new_names)

#计算 30 以内可以被 3 整除的整数：
multiples = [i for i in range(30) if i % 3 == 0]
print(multiples)
'''

# 使用 del 语句来删除列表的元素
list = ['pyssics','chemistry',1997,200]
print(list)
del list[2]
print('after deleting value at index 2 : ',list)

# 使用 append() 添加元素
list.append('Google')
print('after append value : ',list)

#元素读取
print('list[2] :',list[2])      #读取第三个元素
print('list[-2] :',list[-2])    #读取倒数第二个元素
print('list[1:] :',list[1:])    #从第二个元素开始截取列表
print('list len : ',len(list))

list2 = [1,4,6,2,34,7,9,4]
print('the max value in list2 : ',max(list2))
print('the min value in list2 : ',min(list2))

# 统计某个元素在列表中出现的次数
print('count value 4 : ',list2.count(4))

# 从列表中找出某个值第一个匹配项的索引位置
print('the index of value 6 :',list2.index(6))

# list.insert(index, obj)
# 将对象插入列表
list2.insert(0,5)
print('after insert value 5 in index 0: ',list2)

# 移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
list2.pop(-1)   #移除最后一个元素
list2.pop(1)    #移除第二个元素
print('after pop value : ',list2)

# 反向列表中元素
list2.reverse()     #不能直接放在print函数里，会返回None
print('reverse list2 :',list2)

# list.sort(cmp=None, key=None, reverse=False)
# 对原列表进行排序
# cmp ：可选参数, 如果指定了该参数会使用该参数的方法进行排序。
# key ： 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
# reverse ：排序规则，reverse = True 降序， reverse = False 升序（默认）

list2.sort()
print('after sort false: ',list2)
list2.sort(reverse=True)
print('after sort true: ',list2)

# 列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
list2.extend(list)
print('after extend list :',list2)

# 移除列表中某个值的第一个匹配项
list2.remove(4)
print('after remove 4 : ',list2)



'''

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


'''