'''
Created on 2018. 12. 27.

@author: a

pandasex2.py : pandas 모듈을 이용하여 csv 파일 생성하기 
'''
import pandas as pd
import sys
# supplier_data.csv pandas_out.csv
input_file = sys.argv[1] #supplier_data.csv
output_file = sys.argv[2] #pandas_out.csv

data_frame = pd.read_csv(input_file)
'''
    row 검색
    loc  : 정수형 인덱스로 설정
    iloc : 정수형 인덱스로 설정
    ix   : 인덱스의 형태가 정수형이 아니어도 됨. 3.6사용가능
'''
data_frame_in_set = \
    data_frame.loc[data_frame["Invoice Number"].str.startswith("001-"),:]
    # 위 문장 : data_frame 중에 Invoice Number인것을 str로 바꾸고 그것의 시작이 001로 시작하니?
# data_frame_in_set 변수가 저장된 내용을 csv 파일로 생성하기
data_frame_in_set.to_csv(output_file,index=False)