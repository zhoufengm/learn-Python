import xlrd
# 读取指定路径的excel文档，返回一个工作簿对象
workbook = xlrd.open_workbook("test2.xlsx")
print(workbook)
# >>>  <xlrd.book.Book object at 0x00000279074AAF20>


# 打印当前的工作表的名称，以列表形式返回
sheet_lst = workbook.sheet_names()
print(sheet_lst)
# >>> ['测试用例集', '启动APP', '个人信息', '退出APP', '测试结果明细']

# 读取指定sheet表的内容
tp = workbook.sheet_by_name(sheet_lst[0])
# tp2 = workbook.sheet_by_index(0)
# 获取选定sheet的总行数
print(tp.nrows)
# 获取选定sheet的总列数
print(tp.ncols)



# 打印sheet所有的内容，可以把表格内容看做一个二维数组
for i in range(tp.nrows):
    for j in range(tp.ncols):
        # print(tp.row(i)[j].value,end=" ")
        # 使用单元格
        print(tp.cell(i,j).value,end=" ")
    print()