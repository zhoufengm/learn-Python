#运算符
# 算术运算符    + - * / %(返回除法余数) **（次幂) //(向下取接近商的整数)
'''
a = 21
b = 10
c = 0
print('a = ',a)
print('b = ',b)
c = a + b
print('c = a+b = ',c)
c = a - b
print('c = a-b = ',c)
c = a * b
print('c = a*b = ',c)
c = a / b
print('c = a/b = ',c)
c = a % b
print('c = a%b = ',c)
c = a // b
print('c = a//b = ',c)
#修改a,b的值
a = 2
b = 3
c = a**b
print('--------修改a,b------------')
print('a = ',a)
print('b = ',b)
print('c = a**b = ',c)

# 比较（关系）运算符    ==   !=   >   <   >=   <=
a = 21
b = 10
c = 0
print('a = ',a)
print('b = ',b)
if ( a == b):
    print('a == b')
else:
    print('a != b')

if( a != b):    
    print('a != b')
else:
    print('a == b')

if ( a < b):
    print('a < b')
else:
    print('a >= b')

if (a >= b):
    print('a >= b')
else:
    print('a < b')


# 赋值运算符    =   +=  -=   *=  /=  %=  **=  //=  :=(海象运算符)
a = 21
b = 10
c = a + b
print('a = ',a)
print('b = ',b)
print('c = ',c)
c += a      # c = c + a
print('c += a',c)
c *= a      # c = c * a
print('c *= a ',c)
c /= a      # c = c / a
print('c /= a',c)
c = 2
c %= a      # c = c % a
print('c修改为2后，c %= a ',c)
a = 3
c **= a     #c = c**a
print('a修改为3后，c **= a ',c)
c //= a     #c = c//a
print('c //= a ',c)


# 位运算符，把数字看作二进制来进行计算
# &	    按位与运算符：参与运算的两个值,如果两个相应位都为1,则该位的结果为1,否则为0	
# |	    按位或运算符：只要对应的二个二进位有一个为1时，结果位就为1。	
# ^	    按位异或运算符：当两对应的二进位相异时，结果为1	
# ~	    按位取反运算符：对数据的每个二进制位取反,即把1变为0,把0变为1。~x 类似于 -x-1	
# <<	左移动运算符：运算数的各二进位全部左移若干位，由"<<"右边的数指定移动的位数，高位丢弃，低位补0。
# >>	右移动运算符：把">>"左边的运算数的各二进位全部右移若干位，">>"右边的数指定移动的位数

a = 60           # 60 = 0011 1100 
b = 13           # 13 = 0000 1101 
c = 0
c = a & b        # 12 = 0000 1100
print('c = a & b =',c)
c = a | b        # 61 = 0011 1101 
print('c = a | b =',c)
c = a ^ b        # 49 = 0011 0001
print('c = a ^ b =',c)
c = ~a           # -61 = 1100 0011
print('c = ~a',c)
c = a << 2        # 240 = 1111 0000
print('c = a << b =',c)
c = a >> 2        # 15 = 0000 1111 
print('c = a >> b =',c)


# 逻辑运算符    and   or    not
#a = 10
a = 0
b = 20
print('a = ',a,'\t b = ',b)
if (a and b):
    print('a,b 都为true')
else:
    print('a,b 有一个不为true')
if ( a or b ):
    print('a,b 都为true,或者a,b 有一个为true')
else:
    print('a,b 都不为true')

if not (a and b):
    print('a和b都为false,或者其中一个变量为false')
else:
    print('a,b都为true')


# 成员运算符    in      not in
a = 10
b = 20
list = [1,2,3,4,5]
print('a = ',a,'\t b = ',b)
print('list = ',list)
if (a in list):
    print('a在列表中')
else:
    print('a不在列表中')
if (b not in list):
    print('b不在列表中')
else:
    print('b在列表中')

#修改a的值
a = 2
print('a = ',a,'\t b = ',b)
print('list = ',list)
if (a in list):
    print('a在列表中')
else:
    print('a不在列表中')


# 身份运算符    is      is not
# is 用于判断两个变量引用对象是否为同一个， == 用于判断引用变量的值是否相等
a = 20
b = 20
print('a = ',a,'\t b = ',b)
if (a is b):
    print('a和b有相同的标识')
else:
    print('a和b没有相同的标识')
if (id(a) == id(b)):
    print('a和b有相同的标识')
else:
    print('a和b没有相同的标识')

#修改b的值
b = 30
print('a = ',a,'\t b = ',b)
if (a is b):
    print('a和b有相同的标识')
else:
    print('a和b没有相同的标识')
if (a is not b):
    print('a和b没有相同的标识')
else:
    print('a和b有相同的标识')
'''


# 运算符优先级
from operator import truediv


a = 20
b = 10
c = 15
d = 5
e = 0
print('a = ',a,'\tb = ',b,'\tc = ',c,'\td = ',d)
e = ( a + b ) * c / d       #( 30 * 15 ) / 5 = 90.0
print('( a + b ) * c / d = ',e)
e = ( a + b ) * ( c / d )   # (20+10) * (15/5)=90
print(' ( a + b ) * ( c / d ) = ',e)
e = a + ( b * c ) / d       #  20 + (150/5)
print('a + ( b * c ) / d = ',e)

x = True
y = False
z = False
if x or y and z:    #先计算 y and z 并返回 False ，然后 x or False 返回 True
    print('yes')
else:
    print('no')

#优先级高到低 not x     and     or
