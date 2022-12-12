'''
    学习列表排序
    P32
'''

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
guests = ['Canny','Lisa','Joy']
print(len(guests))
print(guests[4])