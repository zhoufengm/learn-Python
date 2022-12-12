'''
20221206 学习Python编程：从入门到实践 
第3章
'''

'''
# P22 2.3
name = "eric"
message1 = "Hello " + name +",would you like to learn some Python today?" 
print(message1)

# 调整名字大小写
print("全大写： " + name.upper())
print("全小写： " + name.lower())
print("首字母大写： " + name.title())

# 名言
# 使用\" 输出双引号
message2 = "Albert Einstein once said, \"A person who never made a mistake never tried anything new.\""
print(message2)
message3 = "One of Python's strengths is its deverse community."
print(message3)

famous_person = "Albert einstein"
message4 = famous_person.title() + " once said, \"A person who never made a mistake never tried anything new.\""
print(message4)

# 剔除人名中的空白
name2 = "  May    "
print(name2)
print(name2.rstrip())
print(name2.lstrip())
print(name2.strip())

name3 = " \tMay  \n"
print("直接打印：" + name3)
print("去掉末尾空白字符：" + name3.rstrip())
print("去掉开头空白字符" + name3.lstrip())
print("去掉头尾空白字符" + name3.strip())


##############################################

# P24 2.4

print(2+6)
print(9-1)
print(2*4)
print(int(24/3.0))
num = 7
print("My favourite number is " + str(num) + ".")


##############################################

# P27 3.1.3
# 姓名
names = ['jom','may','eason','canny']
print(names[0].title())
print(names[1].title())
print(names[2].title())
print(names[3].title())

# 问候语
print("Hello " + names[0].title())
print("How are you " + names[1].title() + " ?")

# 自己的列表
by_4 = ['bicycles','motorcycle','car','bus']
print("I would lick to own a " + by_4[2] +" .")

'''
##############################################

# P30 3.2
# 嘉宾名单
guests = ['Canny','Lisa','Joy']
print("我将邀请 " + guests[0] + ", " + guests[1]  + "和" + guests[2] + " 来参加我的宴会。")

print("太可惜了" + guests[1] + "不能来参加宴会了。")
del guests[1]
print("再次邀请：")
print(guests)
print("我买了大桌子，可以再邀请三个人参加宴会。")
guests.insert(1,'Eason')    # insert可以指定添加的位置
guests.append('May')
guests.append('Lida')   # append添加在末尾
print(guests)
print("三位嘉宾分别是：" + guests[2] + ", " + guests[3]  + "和" + guests[4])
print("太遗憾了，桌子无法及时送达，我只能邀请两位嘉宾。")
del guests[4]
guests.pop(2)
guests.remove('May')
print("最终邀请名单：" + guests[0] + ", " + guests[1])

# P32 3.3列表排序
travel_lists = ['xinjiang','chongqing','qinghai','yunnan','xianggan','taiwan']
'''
# 打印列表
print(travel_lists)

# 使用sorrted临时排序列表
print(sorted(travel_lists))

# 再次打印列表，列表还是原始顺序
print(travel_lists)

# 使用sorrted()按与字母顺序相反的顺序打印列表
print(sorted(travel_lists,reverse=True))

# 再次打印列表，列表还是原始顺序
print(travel_lists)


# 使用reverse()修改列表元素排序
travel_lists.reverse()
print(travel_lists)

# 再次使用reverse()修改列表元素排序
travel_lists.reverse()
print(travel_lists)


# 使用sort()修改列表，按字母顺序a~z排序
travel_lists.sort()
print(travel_lists)

# 使用sort()修改列表，按字母顺序相反的顺序排序（z~a）
travel_lists.sort(reverse=True)
print(travel_lists)
'''

# 打印列表长度（元素个数）
print(len(guests))

# 索引超出长度，报错
# print(guests[4])

# -1可以定位列表最后一个元素，只在列表为空时报错
print(guests[-1])