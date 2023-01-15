# 2023.1.13 
# P63 7.1

'''
# 7-1 汽车租赁
message = input("请问您要租赁什么样的汽车？")
print("好的，我们这边有" + message + "汽车。")



# 7-2 餐馆定位
order = input("请问几人用餐？")
# 使用int将字符串类型转换为int型
order = int(order)
if order > 8:
    print("对不起，暂时没有空桌，请稍等。")
else:
    print("好的，这边有空桌，请用餐。")
'''

# 7-3 10的整数倍
# 使用%取余数判断
num = input("请输入一个大于0的数字：")
num = int(num)
if num > 0:
    if num % 10 == 0:
        print(str(num) + "是10的倍数。")
    else:
        print(str(num) + "不是10的倍数。")
else:
    print("输入的数字不正确。")
