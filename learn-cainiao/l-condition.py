
# if 判断条件：
#     执行语句……
# else：
#     执行语句……

#判断奇偶
a = 1
while a < 7 :
    if( a % 2 == 0 ):
        print(a," is even")
    else:
        print(a," is odd")
    a += 1

#if 基本用法
flag = False
name = 'luren'
if name == 'python':
    flag = True
    print ('welcome boss')
else :
    print(name)


#当判断条件为多个值时,可以用elif
num = 3
if num == 3:
    print('boss')
elif num == 2:
    print('user')
elif num == 1 :
    print('worker')
elif num < 0 :
    print('error')
else:
    print('roadman')


# 由于 python 并不支持 switch 语句，所以多个条件判断，只能用 elif 来实现，
# 如果判断需要多个条件需同时判断时，可以使用 or （或），表示两个条件有一个成立时判断条件成功；
# 使用 and （与）时，表示只有两个条件同时成立的情况下，判断条件才成功。
num = 9
if num >= 0 and num <= 10:   # 判断值是否在0~10之间
    print('hello ',num)

num = 10
if num < 0 or num > 10 :    # 判断值是否在小于0或大于10
    print('hello ',num)
else:
    print('undefine')

num = 8
# 判断值是否在0~5或者10~15之间
if (num >= 0 and num <=5) or (num >= 10 and num <= 15):
    print('hello ',num)
else:
    print('undefine')


v = 100
if (v == 100 ): print ("var = 100")
print("Good bye!")

