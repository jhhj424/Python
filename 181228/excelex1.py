'''
Created on 2018. 12. 28.

@author: a
xlsx : pip3 install openpyxl
xls  : pip install xlrd
excelex1.py : xlsx 형식의 excel 파일 읽기
'''
import openpyxl

filename="sales_2015.xlsx"

book=openpyxl.load_workbook(filename)

sheet = book.worksheets[0]
#모든 데이터가 출력되도록 수정하기
data=[]
# for row in sheet.rows :
#     print("row=",row)
#     data.append([row[0].value,row[1].value])

for row in sheet.rows :
    line = []
    for l,d in enumerate(row) :
        line.append(d.value)
    data.append(line)
    
print(type(data))
print(data)
#enumerate : 열거하다, 자료형중 리스트, 튜플 등을 열거하는 기능
for i,a in enumerate(data) :
    if (i>=10) :
        break
    print(i+1,a[0],a[1])