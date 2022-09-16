# 函数代码块以 def 关键词开头，后接函数标识符名称和圆括号()

# 传不可变对象实例
def changeInt( a ):
    a = 10
    print('a = ',a)

b = 2
changeInt( b )
print('b = ',b)

# 传可变对象实例
def changeMe ( mylist ):
    mylist.append([1,2,3,4])
    print('mylist函数内取值：',mylist)
    return

mylist = [10,20,30]
changeMe(mylist)
print('mylist函数外取值：',mylist)

# 使用关键字参数允许函数调用时参数的顺序与声明时不一致，因为 Python 解释器能够用参数名匹配参数值。
def printinfo( name, age):
    print('Name: ',name)
    print('Age: ',age)
    return

printinfo(age=50,name='kimi')

# 默认参数
# 调用函数时，默认参数的值如果没有传入，则被认为是默认值。下例会打印默认的age，如果age没有被传入：
def printInfo( name, age = 35):
    print('Name : ',name)
    print('Age : ',age)
    return

printInfo(age = 50,name = 'miki')
printInfo(name = 'May')

# 不定长参数
def printinfo3( arg1 , *vartuple):
    # "打印任何传入的参数"
    print('arg1 : ',arg1)
    print('others : ')
    for var in vartuple:
        print(var)
    return

printinfo3(10)
printinfo3(70,60,50)


# return 语句
# return语句[表达式]退出函数，选择性地向调用方返回一个表达式。不带参数值的return语句返回None。
def sum( arg1 , arg2):
    total = arg1 + arg2
    print('函数内： ',total)
    return total

# 调用sum函数
total = sum(10,20)

# 全局变量和局部变量
total = 0 #这是一个全局变量
sum(40,20)
print('函数外全局变量total = ',total)