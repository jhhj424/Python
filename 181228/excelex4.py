'''
Created on 2018. 12. 28.

@author: a
xlsx : pip3 install openpyxl
xls  : pip install xlrd
excelex4.py : ssec1804.xls 파일에서 "1.남자", "1.여자" sheet를 가지고 있는
                파일 ssecl1804.xls 파일 생성하기
'''
from xlrd import open_workbook
from xlwt import Workbook #pip3 install xlwt

def makesheet(output_sheet):
    for row_index in range(worksheet.nrows) : #해당 sheet의 행의 수
        for column_index in range(worksheet.ncols): #해당 sheet의 열의 수
            output_sheet.write(row_index,column_index, #저장할 행과열의 인덱스
            worksheet.cell_value(row_index,column_index)) #저장할 행과열의 값
            print(worksheet.cell_value(row_index,column_index))
input_file = "ssec1804.xls"
output_file = "ssecl1804.xls"
output_workbook = Workbook() #출력된 excel 파일
# add_sheet("전체증감") : sheet를 추가. 이름 설정
output_sheet_male = output_workbook.add_sheet("남자")
output_sheet_female = output_workbook.add_sheet("여자")
# workbook : 입력된 excel 파일
with open_workbook(input_file) as workbook :
    #workbook excel 파일에서 sheet 이름이 "1.전체증감"인 sheet를 읽기
    worksheet = workbook.sheet_by_name("1.남자")
    makesheet(output_sheet_male)
    worksheet = workbook.sheet_by_name("1.여자")
    makesheet(output_sheet_female)    
output_workbook.save(output_file)