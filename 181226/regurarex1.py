'''
Created on 2018. 12. 26.

@author: a
regurarex1.py : 정규식 사용하기
'''

data = '''
    park 800905-1234567
    kin  700905-1234567
    choi 850101-a123456
'''

result = []
for line in data.split("\n") :
    # line : park 800905-1234567
    word_result = []
    for word in line.split(" "):
        if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit():
            word = word[:6] + "-" + "*******"
        word_result.append(word)#[park,800905-*******]
    result.append(" ".join(word_result))# [park 800905-*******]
print("\n".join(result))