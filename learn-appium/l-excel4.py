import os
import openpyxl
from openpyxl import load_workbook

path = r"E:\AutoCode\learn-Python\learn-appium"
os.chdir(path)
workbook = openpyxl.load_workbook("test.xlsx")
sheet = workbook["测试用例集"]


