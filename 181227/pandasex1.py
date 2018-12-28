'''
Created on 2018. 12. 27.

@author: a

pandasex1.py : pandas를 이용하여 csv 파일 읽고,저장하기
                카페에서 supplier_data.csv 파일을 다운받기

'''
import pandas as pd
import sys
# supplier_data.csv pandas_out.csv
input_file = sys.argv[1] #supplier_data.csv
output_file = sys.argv[2] #pandas_out.csv

data_frame = pd.read_csv(input_file)

important_dates = ["1/20/14","1/30/14"]
# loc : 위치를 지정하기
# isin : 포함하니?
data_frame_in_set = \
    data_frame.loc[data_frame["Purchase Date"].isin(important_dates),:]
# data_frame_in_set 변수가 저장된 내용을 csv 파일로 생성하기
data_frame_in_set.to_csv(output_file,index=False)