'''
Created on 2018. 12. 28.

@author: a
xlsx : pip3 install openpyxl
xls  : pip install xlrd
excelex2.py : 
'''
from xlrd import open_workbook

input_file = "ssec1804.xls"
workbook = open_workbook(input_file)

print("worksheets의 갯수:",workbook.nsheets)
for worksheet in workbook.sheets() :
    print("worksheet 이름:",worksheet.name,"\n행수:",worksheet.nrows,
          "\n컬럼수:",worksheet.ncols)