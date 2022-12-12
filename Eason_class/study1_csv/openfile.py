


file2 = open('./stu.xlsx','a',encoding='utf-8')
file2.write('kkkkk')
file2.close()

# with open 打开文件后不用手动关闭文件
with open('./stu.xlsx','r',encoding='utf-8') as file3:
    count = file3.read()
    print(count)