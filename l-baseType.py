# Python3 中有六个标准的数据类型：
# Number（数字）
# String（字符串）
# List（列表）
# Tuple（元组）
# Set（集合）
# Dictionary（字典）
# Python3 的六个标准数据类型中：
# 不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）；
# 可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）。
#学习链接 https://www.runoob.com/python3/python3-data-type.html

counter = 100          # 整型变量
miles   = 1000.0       # 浮点型变量
name    = "runoob"     # 字符串
print (counter)
print (miles)
print (name)

#允许同时为多个变量赋值
a, b, c = 1, 2, "runoob"
print (a)
print (b)
print (c)

#Number
a,b,c,d = 20,5.5,True,4+3j
print(d)
print(type(a),type(b),type(c),type(d))


#下面几句要在cmd执行
#a = 111
#isinstance(a,int)
#bool 是 int 的子类
#>>> issubclass(bool, int) 
# True
# >>> True==1
# True
# >>> False==0
# True
# >>> True+1
# 2
# >>> False+1
# 1
# >>> 1 is True
# False
# >>> 0 is False
# False

# 数值运算
# >>> 5 + 4  # 加法
# 9
# >>> 4.3 - 2 # 减法
# 2.3
# >>> 3 * 7  # 乘法
# 21
# >>> 2 / 4  # 除法，得到一个浮点数
# 0.5
# >>> 2 // 4 # 除法，得到一个整数
# 0
# >>> 17 % 3 # 取余
# 2
# >>> 2 ** 5 # 乘方
# 32

#string
str = 'Runoob'
print (str)          # 输出字符串
print (str[0:-1])    # 输出第一个到倒数第二个的所有字符
print (str[0])       # 输出字符串第一个字符
print (str[2:5])     # 输出从第三个开始到第五个的字符
print (str[2:])      # 输出从第三个开始的后的所有字符
print (str * 2)      # 输出字符串两次，也可以写成 print (2 * str)
print (str + "TEST") # 连接字符串

#List(列表)
list = ['abcd',786,2.23,'runoob',70.2]
tinylist = [123,'runoob']
print (list)            # 输出完整列表
print (list[0])         # 输出列表第一个元素
print (list[1:3])       # 从第二个开始输出到第三个元素
print (list[2:])        # 输出从第三个元素开始的所有元素
print (tinylist * 2)    # 输出两次列表
print (list + tinylist) # 连接列表

from tkinter import W

#翻转字符串,就是自己写函数  
# 假设列表 list = [1,2,3,4],  
# list[0]=1, list[1]=2 ，而 -1 表示最后一个元素 list[-1]=4 ( 与 list[3]=4 一样)
# inputWords[-1::-1] 有三个参数
# 第一个参数 -1 表示最后一个元素
# 第二个参数为空，表示移动到列表末尾
# 第三个参数为步长，-1 表示逆向   
def reverseWords(input):
    # 通过空格将字符串分隔符，把各个单词分隔为列表
    inputWords = input.split(" ")
    #inputWords=inputWords[-1::-1] 
     # 重新组合字符串
    i=0; j=len(inputWords)-1
    while i<j:
        t=inputWords[i]
        inputWords[i]=inputWords[j]
        inputWords[j]=t
        i += 1
        j -= 1
    return ' '.join(inputWords)
    
s = 'I like runoob'
rw = reverseWords(s)    #调用函数
print(rw)


#Tuple（元组）不支持元素修改，可以包含可变的对象，比如list列表
tuple = ('adcd',786,2.23,'runoob',70.2)
tinytuple = (123,'runoob')
print(tuple)            # 输出完整元组
print(tuple[0])         # 输出元组的第一个元素
print(tuple[1:3])       # 输出从第二个元素开始到第三个元素
print(tuple[2:])        # 输出从第三个元素开始的所有元素
print(tuple*2)          # 输出两次元组
print(tuple+tinytuple)  # 连接元组


#Set（集合）
#集合（set）是由一个或数个形态各异的大小整体组成的，构成集合的事物或对象称作元素或是成员。
#基本功能是进行成员关系测试和删除重复元素。
#使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
sits = {'google','taobao','runoob','facebook','zhihu','baidu','runoob'}
print(sits) #重复项不会输出，会自动去掉
#成员测试
if 'runoob' in sits:
    print('runoob在集合中')
else:
    print('runoob不在集合中')

#set可以进行集合运算
a = set('abcd')
b = set('alacf')
print(a)
print(a-b)       # a 和 b 的差集(项在a中，但不在b中)
print(a|b)       # a 和 b 的并集
print(a&b)       # a 和 b 的交集
print(a^b)       # a 和 b 中不同时存在的元素(项在a或b中，但不会同时出现在二者中)

#Dictionary（字典）无序的对象集合
#字典是一种映射类型，字典用 { } 标识，它是一个无序的 键(key) : 值(value) 的集合。
dict = {}
dict['one']="1-菜鸟教程"
dict[2]    ="2-菜鸟工具"
tinydict = {'name':'runoob','code':1,'site':'www.runoob.com'}
print(dict['one'])          # 输出键为 'one' 的值
print(dict[2])              # 输出键为 2 的值
print(tinydict)             # 输出完整的字典
print(tinydict.keys())        # 输出所有键
print(tinydict.values())      # 输出所有值

#字典推导式,每个x都平方在输出
#{x:x**2 for x in (2,4,6)}
#结果为{2: 4, 4: 16, 6: 36}