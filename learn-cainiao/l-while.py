# 2022.8.23
# while 判断条件(condition)：
#     执行语句(statements)……

#打印10以内的奇数
from re import I


a = 1
while a < 10:
    print(a)
    a += 2

#把一组数按奇偶分成两组
numbers = [12,37,4,26,8,95]
even = []
odd = []
while len(numbers) > 0:
    number = numbers.pop()
    if(number % 2 == 0):
        even.append(number)
    else:
        odd.append(number)
print('even = ',even)
print('odd = ',odd)


count = 0
while (count < 9):
    print('The count is : ',count)
    count += 1
print("Good bye!")


# continue 和 break 用法
i = 1
while i < 10:
    i += 1
    if i % 2 > 0:
        continue    # 非双数时跳过输出
    print(i)        # 输出双数2、4、6、8、10

i = 1
while 1:
    print(i)        # 输出1~10
    i += 1
    if i > 10:      # 当i大于10时跳出循环
        break


count = 0
while count < 5:
    print(count," is less than 5")
    count = count + 1
else :
    print(count," is not less than 5")


#类似 if 语句的语法，如果你的 while 循环体中只有一条语句，你可以将该语句与while写在同一行
flag = 1
#while(flag): print("Given flag is really true!")
print("Good bye!")
#无限循环你可以使用 CTRL+C 来中断循环