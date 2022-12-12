'''
# 练习一：随机数
# 直接导入random
import random
number1 = random.randint(1,100)
print(number1)

# 导入random 并给它取一个新名字rd
import random as rd
number2 = rd.randint(100,200)
print(number2)


# 练习二：open读写文件
#打开并写入文件
file1 = open('./exercise.txt','w',encoding='utf-8')
file1.write('盈趣的使命是：')
file1.close

#读取并关闭文件
file2 = open('./exercise.txt','r')
content = file2.read()
print(content)
file2.close


# 练习四：with open 读写文件
# open打开文件，并追加内容，需要手动关闭内容
file3 = open('./exercise.txt','a',encoding='utf-8')
file3.write('打造乐趣生活')
file3.close

# with open 打开文件，读取内容，不需要手动关闭文件
with open('./exercise.txt','r') as file4:
    content  = file4.read()
    print(content)
    


# 练习五：打开csv文件,读取每一行的内容
# 导入csv模块
import csv
# 使用utf-8-sig编码，表头不会多出一些额外字符
with open('员工发展基金确认表.csv','r',encoding='utf-8-sig',newline='') as file5:
    # 将csv文件转化为reader对象，该对象里面的每一个元素都是一个列表
    csv_reader = csv.reader(file5)
    print('使用reader读取文件内容如下：')
    for row in csv_reader:
        print(row)


# 练习六：使用DictReader打开文件，获取表头
with open('E:/study/员工发展基金确认表.csv','r',encoding='utf-8-sig',newline='') as file6:
    # 将csv文件转化为DictReader对象。该对象里面的每一个元素都是一个字典
    csv_dictreader = csv.DictReader(file6)
    # 使用filednames属性获取表头
    header = csv_dictreader.fieldnames
    print(f'该文件表头为：{header}')
    print('使用DictReader读取文件内容如下：')
    for row in csv_dictreader:
        print(row)


# 练习七：使用DictWriter写入
import csv
dict_info = {'姓名': '徐小刚', '工号': '1005', '员工发展基金': '100', '员工签字': ''}
# 设置表头(将字典keys获取设置为表头)
headers = dict_info.keys()
with open('徐小刚信息.csv','w',encoding='utf-8-sig',newline='') as file7:
    # 将文件转化为DictWriter对象,并设置表头
    file7_dictwriter = csv.DictWriter(file7,fieldnames=headers)
    # 使用writerheader方法，写入表头
    file7_dictwriter.writeheader()
    # 写入内容
    file7_dictwriter.writerow(dict_info)

'''
# 课后练习
# 导入csv模块、os库
import csv,os
# 设置员工发展基金确认表的路径
sourcefile_path = os.path.dirname(__file__)
# 设置存放拆分结果文件的文件夹（员工发展基金文件夹）的路径。
result_path = os.path.join(sourcefile_path,'员工发展基金')
# 打开员工发展基金确认表
with open('员工发展基金确认表.csv','r',encoding='utf-8-sig',newline='') as sourcefile:
    # 将文件对象转换为DictReader对象
    source_dictreader = csv.DictReader(sourcefile)
    # 将csv文件的表头读取出来
    headers = source_dictreader.fieldnames

    # 循环处理确认表中除表头外的每一行数据
    for row in source_dictreader:
        # 根据获取的员工名字拼接出新文件名
        staff_file = row['姓名']+'.csv'
        # 拼接新文件路径
        staff_path = result_path + os.sep + staff_file
        # 创建新文件并添加数据
        with open(staff_path,'w',encoding='utf-8-sig',newline='') as target_file:
            # 将文件对象转换为DictWriter对象
            target_dictwriter = csv.DictWriter(target_file,fieldnames=headers)
            # 写入表头
            target_dictwriter.writeheader()
            # 写入数据
            target_dictwriter.writerow(row)


