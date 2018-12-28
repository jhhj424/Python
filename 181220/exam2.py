'''
Created on 2018. 12. 20.

@author: a
exam2.py
'''
instr = input('문자열을 입력하세요:')
if instr.isdigit() :
    print("숫자입니다.")
elif instr.isalpha() :
    print("글자입니다.")
elif instr.isalnum() :
    print("글자 + 숫자입니다.")
else :
    print('모르겠습니다.')
    
if instr.islower() :
    print("소문자입니다")
elif instr.isupper() :
    print("대문자입니다.")
elif instr.isspace() :
    print("공백입니다.")
else :
    print("구분못합니다.")