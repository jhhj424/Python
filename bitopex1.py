'''
Created on 2018. 12. 18.
bitopex1.py : 비트 연산자 연습/ shift연산자 연습
@author: a
'''

a = ord('A') #아스키코드값 리턴
print(a)
mask = 0x0F # 16진수 F, 10진수 15값

print("%X & %X = %X" % (a,mask,a&mask))
'''
  'A' 41 : 01000001 : 65
 mask 0F : 00001111 : 15
 =======================
   &     : 00000001 : 1 
'''
print("%X | %X = %X" % (a,mask,a|mask))
'''
  'A' 41 : 01000001 : 65
 mask 0F : 00001111 : 15
 =======================
   |     : 01001111 : 4F 
'''
print("%X ^ %X = %X" % (a,mask,a^mask))
'''
  'A' 41 : 01000001 : 65
 mask 0F : 00001111 : 15
 =======================
   ^     : 01001110 : 4E 
'''

a = 100
result = 0
for i in range(1,5) :
    result = a << i
    print("%d << %d = %d" % (a,i,result))

for i in range(1,5) :
    result = a >> i
    print("%d << %d = %d" % (a,i,result))