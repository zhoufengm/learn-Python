# 2023.1.5 学习if  elif else
# P49

'''
# 5-3
alien_color = 'red'   # 'green'   'yellow'  'red'
point = 0
if alien_color == 'green':
    point = 5
    print("恭喜玩家射杀绿色外星人，获得" + str(point) + "个点。")

print("很遗憾，本轮玩家没有射杀外星人成功，没有获得分数。")



# 5-4
alien_color = 'red'   # 'green'   'yellow'  'red'
point = 0
if alien_color == 'green':
    point = 5
    print("5-4-1 恭喜玩家射杀绿色外星人，获得" + str(point) + "个点。")
else:
    point = 10
    print("5-4-1 恭喜玩家射杀非绿色外星人，获得" + str(point) + "个点。")


alien_color = 'green'   # 'green'   'yellow'  'red'
point = 0
if alien_color == 'green':
    point = 5
    print("5-4-2 恭喜玩家射杀绿色外星人，获得" + str(point) + "个点。")
else:
    point = 10
    print("5-4-2 恭喜玩家射杀非绿色色外星人，获得" + str(point) + "个点。")


# 5-5
alien_color = 'red'
if alien_color == 'green':
    print("5-5-1 恭喜玩家射杀绿色外星人，获5个点。")
elif alien_color == 'yellow':
    print("5-5-1 恭喜玩家射杀黄色外星人，获得10个点。")
elif alien_color == 'red':
    print("5-5-1 恭喜玩家射杀红色外星人，获得15个点。")

alien_color = 'green'
if alien_color == 'green':
    print("5-5-2 恭喜玩家射杀绿色外星人，获5个点。")
elif alien_color == 'yellow':
    print("5-5-2 恭喜玩家射杀黄色外星人，获得10个点。")
elif alien_color == 'red':
    print("5-5-2 恭喜玩家射杀红色外星人，获得15个点。")

alien_color = 'yellow'
if alien_color == 'green':
    print("5-5-3 恭喜玩家射杀绿色外星人，获5个点。")
elif alien_color == 'yellow':
    print("5-5-3 恭喜玩家射杀黄色外星人，获得10个点。")
elif alien_color == 'red':
    print("5-5-3 恭喜玩家射杀红色外星人，获得15个点。")



# 5-6
age = 89
print("她的年龄是" + str(age) + "，")
if age < 2:
    print("她是婴儿。")
elif age < 4:
    print("她正蹒跚学步。")
elif age < 13:
    print("她是儿童。")
elif age < 20:
    print("她是青少年。")
elif age < 65:
    print("她是成年人。")
elif age >= 65 :
    print("她是老年人。")



# 5-7
favorite_fruits = ['bananas','apple','strawberry']
if 'bananas' in favorite_fruits:
    print("You really like bananas!")
if 'pear' in favorite_fruits:
    print("You really like pears!")
if 'apple' in favorite_fruits:
    print("You really like apples!")
if 'strawberry' in favorite_fruits:
    print("You really like strawberries!")
if 'puple' in favorite_fruits:
    print("You really like puples!")


# 2023.1.6 P51 5-8
users = ('admin','Joy','May','Lin','kate')
for user in users:
    if user == 'admin':
        print('Hello admin,would you like to see a status report?')
    else:
        print('Hello '+ user + ',thank you for logging in again.')

    

# 5-9
users = ['Lin','kate']
if users:   # 检查列表是否为空
    for user in users:
        users.remove
        print('Delete user ' + user)
else:
    print('We need to find some users!')



# 5-10
current_users = ['Jason','Joy','May','Lin','kate']
new_users = ['MAY','Lin','Ella','Jom','Canny']
for user in new_users:
    # 将名字转化为小写，进行不区分大小写判断
    if user.lower() in [x.lower() for x in current_users]:
        print(user + ' is used,please rename!')
    else:
        print(user + ' is correct!')

'''

# 5-11
for n in range(1,10):
    if n == 1:
        print(str(n) + "st")
    elif n == 2:
        print(str(n) + "nd")
    elif n == 3:
        print(str(n) + "rd")
    else:
        print(str(n) + 'th')
