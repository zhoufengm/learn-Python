#20220725
#https://www.runoob.com/python3/python3-basic-syntax.html

import imp


str='123456789'

print(str)          #输出字符串
print(str[0:-1])    #输出第一个到倒数第二个的所有字符
print(str[0])       #输出字符串第一个字符
print(str[2:5])     #输出从第三个开始到第五个的字符
print(str[2:])      #输出从第三个开始后的所有字符
print(str[1:5:2])   #输出从第二个开始到第五个且每隔一个的字符（步长为2）
print(str*2)        #输出字符串两次
print(str+'你好')   #连接字符串
print('-----------------------')
print('hello\nrunstr')  #使用反斜杠（\）+n转义特殊字符
print(r'hello\nrunstr') #在字符串前面添加一个r，表示原始字符串，不会发生转义


#等待用户输入
#input("\n\n按下 enter 键后退出。")


#同一行显示多条语句
#使用交互式命令行执行,要打开cmd,输入python,在把语句复制过去回车，结果为
#runoob
#7      7 表示字符数，runoob 有 6 个字符，\n 表示一个字符，加起来 7 个字符。
import sys; x='runoob'; sys.stdout.write(x+'\n')


#print 输出
#print 默认输出是换行的，如果要实现不换行需要在变量末尾加上 end=""：
x="a"
y="b"
#换行输出
print(x)
print(y)
print('-------------')
#不换行输出
print(x, end=" ")
print(y, end=" ")


#import 与 from...import
import sys
print('===========python import mode============')
print('命令行参数为：')
for i in sys.argv:
    print(i)
print('\n python 路径为 ',sys.path)

#导入特定的成员
from sys import argv,path
print('===========python import mode============')
print('path:',path) # 因为已经导入path成员，所以此处引用时不需要加sys.path

#ctrl+/注释掉一整段

