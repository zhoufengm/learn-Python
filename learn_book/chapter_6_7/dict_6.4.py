# 2023.1.11 P61 6.4

'''
# 6-7 人
people1 = {
    'first_name':'Zhou',
    'last_name':'May',
    'age':30,
    'city':'Xiamen'
}

people2 = {
    'first_name':'Chen',
    'last_name':'Joke',
    'age':20,
    'city':'Shanghai'
}

people3 = {
    'first_name':'Lin',
    'last_name':'Canny',
    'age':25,
    'city':'Shenzhen'
}

# 将三个人存储在一个列表中
people = []
people.append(people1)
people.append(people2)
people.append(people3)

print(people)



# 6-8 宠物
pet1 = {
    'name' : '大咪',
    'owner' : 'papi',
    'age' : 8,
    'type' : '田园猫'
}

pet2 = {
    'name' : '中分',
    'owner' : '花花',
    'age' : 4,
    'type' : '田园猫'
}

pet3 = {
    'name' : '克鲁克呀',
    'owner' : '未名',
    'age' : 6,
    'type' : '狗'
}

pets = []
pets.append(pet1)
pets.append(pet2)
pets.append(pet3)

for pet in pets:
    print(pet)
'''

'''
# 6-9 字典嵌套列表 喜欢的地方
favorite_places = {
    'May':['Beijing','hainan','chongqi'],
    'Lin':['xianggan','aomen'],
    'Jom':['taiguo','xinjiapo','malaixiya']
}

for name,place in favorite_places.items():
    print(name + "'s favorite places are ")
    for p in place:
        print("\t" + p.title())


# 使用sys.stdout.write()方法打印，不会自动换行
import sys

# 6-10 喜欢的数字
favorite_num = {
    'May': [7,3],
    'Canny':[1,8,9],
    'Jom':[0,1],
    'Ella':[6],
    'Kate':[]
}
for name,numbers in favorite_num.items():
    if len(numbers) == 0:
        print(name + " doesn't have favorite number.")
    elif len(numbers) == 1:
        print(name + "'s favorite number is " + str(numbers[0]) + ".")
    else:
        sys.stdout.write(name + "'s favorite number are ")
        for n in numbers:
            sys.stdout.write(str(n) + " ")
        print(".")

'''

# 6-11 字典嵌套字典 城市
cities = {
    '厦门' : {
        '国家':'中国',
        '人口':'528万',
        '事实':'郑成功'
    },
    '悉尼':{
        '国家':'澳大利亚',
        '人口':'503万',
        '事实':'悉尼歌剧院'
    },
    '清莱':{
        '国家':'泰国',
        '人口':'3.3万',
        '事实':'白庙'
    }

}
for city,info in cities.items():
    country = info['国家']
    population = info['人口']
    fact = info['事实']
    print(city + "属于" + country + ",人口约" + population + ",有个著名的" + fact + "。") 
