'''
Created on 2018. 12. 27.

@author: a
pandasex4.py : pandas 파일에서 column 조회하기
'''
import pandas as pd
import sys
#supplier_data.csv pandas_out4.csv
input_file = sys.argv[1]#supplier_data.csv
output_file = sys.argv[2]#pandas_out4.csv

df = pd.read_csv(input_file)
print(df)
#df_col = df.iloc[:,[0,3]] #0번열과, 3번열을 조회
df_col = df.loc[:,["Supplier Name","Cost"]] #0번열과, 3번열을 조회

df_col.to_csv(output_file,index=False)