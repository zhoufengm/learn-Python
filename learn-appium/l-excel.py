import datetime

import xlrd
from xlrd import xldate_as_tuple

'''
# 获取Excel文件的位置并且读取进来
path = "/learn-appium"
data = xlrd.open_workbook(r'test1.xlsx')
table = data.sheets()[0]

# 创建一个空列表，存储Excel的数据
tables = []

# 将excel表格内容导入到tables列表中
def import_excel(excel):
    for rown in range(excel.nrows):
        array = {'road_name':'','bus_plate':'','road_tpye':'','site':''}
        array['road_name'] = table.cell_value(rown,0)
        array['bus_plate'] = table.cell_value(rown,1)
        if table.cell(rown,2).ctype == 3:
            data = xldate_as_tuple(table.cell(rown,2).value,0)
            array['timeline'] = datetime.datetime(*datetime.date)
        array['road_tpye'] = table.cell_value(rown,3)
        array['site'] = table.cell_value(rown,4)
        tables.append(array)

if __name__ == '__main__':
    # 将excel表格的内容导入到列表中
    import_excel(table)
    for i in tables:
        print(i)
'''

# # 逐行读取
# f = open("nameorder.txt")
# line = f.readline()
# while line:
#     print(line)
#     line = f.readline()
# f.close()



# # 一行一行读取，不用另外关文件
# for line in open("nameorder.txt"):
#     print(line)



# # 一次性读取全部内容
# f = open("nameorder.txt","r")
# lines = f.readlines()
# for line in lines:
#     print(line)


# 一次性读取，捕捉异常
f = open("nameorder.txt")
try:
    # some_text = f.read(5) #读取固定字节
    all_text = f.read()
    print(all_text)
finally:
    print("文件读取完成！")
    f.close()
