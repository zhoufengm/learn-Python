# 字典推导式
# d = {key1 : value1, key2 : value2 }
# 键一般是唯一的，如果重复最后的一个键值对会替换前面的，值不需要唯一
#
# { key_expr: value_expr for value in collection }
# 或
# { key_expr: value_expr for value in collection if condition }

# 使用字符串及其长度创建字典：
listdemo = ['google','runoob','taobao']
# 将列表中各字符串值为键，各字符串的长度为值，组成键值对
newdict = {key:len(key) for key in listdemo}
print(newdict)
# 组成的字典为： {'google': 6, 'runoob': 6, 'taobao': 6}

# 提供三个数字，以三个数字为键，三个数字的平方为值来创建字典：
dic = {x:x**2 for x in (2,4,6)}
print(dic)
print(type(dic))

# 访问字典里的值
tinydict = {'Name':'Zara', 'Age':7, 'Class':'First'}
print("tinydict['Name']: ",tinydict['Name'])
print("tinydict['Age']: ",tinydict['Age'])
print("tinydict['Class']: ",tinydict['Class'])

# 修改或增加新的键/值对
tinydict['Age'] = 8             #更新
tinydict['School'] = 'Runoob'   #添加
print('更新后的tinydict : ',tinydict)

'''
# 删除字典元素
del tinydict['Class']   # 删除键是'Class'的条目
print('after delete class : ',tinydict)
tinydict.clear()        # 清空字典所有条目
print('after clear dict : ',tinydict)
del tinydict            # 删除字典,打印时会报错，提示该字典 is not defined
print('after delete dict : ',tinydict)
'''

# 字典内置函数&方法

# 计算字典元素个数，即键的总数
print('the length of tinydict is ',len(tinydict))

# 输出字典可打印的字符串表示
print('str(dict) : ',str(tinydict))

# 返回输入的变量类型，如果变量是字典就返回字典类型
print('the type of tinydict is ',type(tinydict))

# 返回一个字典的浅复制
student1 = tinydict.copy()
print('student1 : ',tinydict)

list1 = [1,2,3,4]
list2 = ['a','b']
# 不指定默认的键值，默认为 None
student2 = dict.fromkeys(list1)
print('student2 : ',student2)   #student2 :  {1: None, 2: None, 3: None, 4: None}
# 指定默认的键值
student3 = dict.fromkeys(list1,list2)
print('student3 : ',student3)   #student3 :  {1: ['a', 'b'], 2: ['a', 'b'], 3: ['a', 'b'], 4: ['a', 'b']}
student4 = dict.fromkeys(list1,20)
print('student4 : ',student4)   #student4 :  {1: 20, 2: 20, 3: 20, 4: 20}


# 返回指定键的值，如果值不在字典中返回default值
print("Name is %s" % tinydict.get('Name'))
print("Sex is %s" % tinydict.get('Sex'))    # 没有设置 Sex，也没有设置默认的值，输出 None


# 把字典 dict2 的键/值对更新到 dict 里
# dict.update(dict2)
tinydict2 = {'Sex':'female'}
tinydict.update(tinydict2)
print('tinydict : %s ' % tinydict) #tinydict : {'Name': 'Zara', 'Age': 8, 'Class': 'First', 'School': 'Runoob', 'Sex': 'female'}


# dict.values() 返回字典中的所有值
print(' value : %s ' % tinydict.values())   #value : dict_values(['Zara', 8, 'First', 'Runoob', 'female'])


# pop(key[,default])
# 删除字典给定键 key 所对应的值，返回值为被删除的值
site = {'name':'菜鸟教程','alexa':10000,'url':'www.runoob.com'}
element = site.pop('name')
print('删除元素为：',element)
print('字典为： ',site)
# 如果删除的键不存在会触发异常
# element = site.pop('nickname')
# 可以设置默认值来避免异常
element = site.pop('nickname','不存在的Key')
print('删除元素为：',element)
print('字典为： ',site)