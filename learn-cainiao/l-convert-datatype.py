#integer整型，float浮点型
#Python 会将较小的数据类型转换为较大的数据类型，以避免数据丢失
#可隐式转换
num_int = 123
num_flo = 1.23
num_new = num_int + num_flo
print('datatype of num_int；',type(num_int))
print('datatype of num_flo:',type(num_flo))
print('value of num_new:',num_new)
print('datatype of num_new:',type(num_new))


num_str = '456'
print('num_int数据类型为:',type(num_int))
print('类型转换前，num_str数据类型为：',type(num_str))
#整型和字符串类型运算结果会报错，输出 TypeError
#无法使用隐式转换,要使用显式转换
#print(num_int + num_str)
num_str = int(num_str)  #强制转换为整型
print('类型转换后，num_str数据类型为：',type(num_str))
num_sum = num_int + num_str
print('num_int + num_str的结果为：',num_sum)
print('num_sum数据类型为：',type(num_sum))


#int() 强制转换为整型：
x = int(1)      # x 输出结果为 1
y = int(2.8)    # y 输出结果为 2
z = int('3')    # z 输出结果为 3,'3.4'这种字符串不能转换为int
print('x y z :',x,y,z)

#float() 强制转换为浮点型：
a = float(2)        # 输出结果为2.0
b = float(2.5)      # 输出结果为2.5
c = float("4")      # 输出结果为4.0
d = float("2.4")    # 输出结果为2.4
print('a :',a)
print('b :',b)
print('c :',c)
print('d :',d)

#str() 强制转换为字符串类型：
e = str("s1")       # 输出结果为s1
f = str(2)          # 输出结果为2
g = str(3.6)        # 输出结果为3.6
print('e :',e)
print('f :',f)
print('g :',g)