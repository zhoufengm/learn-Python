# 2023.1.7 P55 6-2

'''
# 6-1
people = {
    'first_name':'Zhou',
    'last_name':'May',
    'age':20,
    'city':'Xiamen'
}
print(people)



# 6-2
favorite_num = {
    'May':7,
    'Canny':8,
    'Jom':1,
    'Ella':6,
    'Kate':9
}
print("May's favorite number is " + str(favorite_num['May']) + ".")
print("Canny's favorite number is " + str(favorite_num['Canny']) + ".")
print("Jom's favorite number is " + str(favorite_num['Jom']) + ".")
print("Ella's favorite number is " + str(favorite_num['Ella']) + ".")
print("Kate's favorite number is " + str(favorite_num['Kate']) + ".")


# 外星人位置跟踪
alien_0 = {
    'x_position': 0,
    'y_position': 25,
    'speed' :'medium'
}
# 向右移动外星人
# 根据外星人的速度决定将其移动多远
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 5
else:
    # 这个外星人速度很快
    x_increment = 10

# 新位置等于老位置加上增量
alien_0['x_position'] =  alien_0['x_position'] + x_increment
# 打印新的位置
print("New x_position is " + str(alien_0['x_position']))



# 6-4
rivers = {
    'huanghe':'China',
    'Nile':'Egypt',
    'amazon river':'Brazil'
}

# 一次性打印两个信息
for river,country in rivers.items():
    print("The " + river.title() + " flows through " + country + '.')

# 打印河流名称
print("All rivers :")
for river in rivers.keys():
    print(river.title())

# 打印国家名称
print("All country:")
for country in rivers.values():
    print(country)

'''

# 6-6
favorite_language ={
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'java',
}
people = ['sarah','may','phil']
for p in people:
    if p in favorite_language.keys():
        print(p.title()+ "感谢你参加调查。")
    else:
        print(p.title()+ "邀请你下次参加调查。")