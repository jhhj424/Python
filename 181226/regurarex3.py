'''
Created on 2018. 12. 26.

@author: a
regurarex3.py
'''
import re
string = "The quick brown fox jumps over the lazy dog."
string_list = string.split()
# r : row 문자형
# re.I : 대소문자 구분 없이
pattern = re.compile(r"The",re.I)
count = 0
for word in string_list:
    if pattern.search(word):
        count += 1
print("output #1 {0:d}".format(count))
# match_word : match_word 그룹 이름 설정
#              대소문자 구분 없이 The 문자를 match_word 그룹으로 설정
pattern = re.compile(r"(?P<match_word>The)",re.I)
print("output #2 :")
for word in string_list :
    if pattern.search(word):
        print("{0}".format(pattern.search(word).group("match_word")))
string_to_find = r"The"
pattern = re.compile(string_to_find,re.I)
print("output #3 : {0}".format(pattern.sub("a",string)))