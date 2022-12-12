# 导入csv模块
import csv,os
'''
# 使用reader 打开csv文件
# utf-8-sig 避免首行(表头)出现额外字符  >>>  ['姓名', '工号', '员工发展基金', '员工签字']
# 使用utf-8     >>>  ['\ufeff姓名', '工号', '员工发展基金', '员工签字']
with open('./员工发展基金确认表.csv','r',encoding='utf-8-sig',newline='') as csv_file:
    # 将csv文件转化为reader对象，这为可迭代对象，才能读取每一行
    csv_reader = csv.reader(csv_file)
    # 遍历reader对象
    for row in csv_reader:
        # 打印csv文件中的每一行内容
        print(row)

# ['姓名', '工号', '员工发展基金', '员工签字']
# ['邱大仁', '1001', '300', '']




# 使用DictReader 打开csv文件
with open('./员工发展基金确认表.csv','r',encoding='utf-8-sig',newline='') as csv_file2:
    # 将csv文件转化为DictReader对象，这返回字典，每一行都是一个字典
    csv_dict = csv.DictReader(csv_file2)
    # 使用filednames属性，获取表头
    file_title = csv_dict.fieldnames
    # 打印表头信息，f表示格式化信息
    print(f'表头：{file_title}')
    # 遍历迭代打印每一行
    for row_dic in csv_dict:
        print(row_dic)

# 表头：['姓名', '工号', '员工发展基金', '员工签字']
# {'姓名': '邱大仁', '工号': '1001', '员工发展基金': '300', '员工签字': ''}



# os.sep 系统的目录分割线
# windows : \
# ios : /
# os.path.jion 拼接两个目录

info_dict = {'姓名': '邱大仁', '工号': '1001', '员工发展基金': '300', '员工签字': ''}
# 设置表头
headers = info_dict.keys()
# 这里编码如果是utf-8则写入的是乱码
# 徐小刚信息这里会自动创建文件
with open('徐小刚信息.csv','w',encoding='utf-8-sig',newline='') as target_file:
    result_file = csv.DictWriter(target_file,fieldnames=headers)
    # 写入表头
    result_file.writeheader()

 '''

# 
source_path = './员工发展基金确认表.xlsx'
# 文件目录
source_file_path = os.path.join(os.path)




