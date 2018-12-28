'''
Created on 2018. 12. 19.

@author: a

1. 홍길동 씨의 주민등록번호는 881120-1068234이다. 홍길동씨의 주민등록 번호를 연월일(YYYYMMDD) 부분과 그 뒤의 숫자 부분으로 나누어 출력해보자.<br>

881120
1068234

2. 주민등록번호 뒷자리의 맨 첫 번째 숫자는 성별을 나타낸다. 주민등록번호에서 성별을 나타내는 숫자를 출력해보자.

1

3. [1, 3, 5, 4, 2]라는 리스트를 [5, 4, 3, 2, 1]로 만들어보자.

[5, 4, 3, 2, 1]

4. ['Life', 'is', 'short'] 라는 리스트를 Life is short라는 문자열로 만들어 출력해 보자. join()

Life is short


5. d = {"A":90, "B":80, "C":70}
딕셔너리 d에서 'B'에 해당되는 값을 추출하고 삭제해 보자.
B를 추출한 후 딕셔너리 {'A': 90, 'C': 70}
B에 해당되는 값 80

6. 
e = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
e 리스트에서 중복된 숫자들을 제거해 보자.
[1, 2, 3, 4, 5]

'''

# 1번문제
print("[1번문제]")
bi = "881120-1068234"
for i in range(len(bi)) :
    if bi[i] == "-" :
        print()
    else :
        print(bi[i], end="")
print()
### 2번째풀이
print(bi[:6])
print(bi[7:])
        
# 2번문제
print("[2번문제]")
print(bi[-7])

# 3번문제
print("[3번문제]")
arr = [1, 3, 5, 4, 2]
arr1 = [1, 3, 5, 4, 2]
a = 0
for i in range(len(arr)) :
    for i in range(len(arr)-1) :
        if arr[i] > arr[i+1] :
            t = arr[i]
            arr[i] = arr[i+1]
            arr[i+1] = t
arr.reverse()
print(arr)
#2번째풀이
arr1.sort(key=None, reverse=True)
print(arr1)

# 4번문제
print("[4번문제]")
list1 = ['Life', 'is', 'short']
print(" ".join(list1))

# 5번문제
print("[5번문제]")
d = {"A":90, "B":80, "C":70}
print("'B'에 해당되는 값 : ",d.get("B"))
d.pop("B")
print(d)
print("B를 추출한 후 딕셔너리{}".format(d)) # format : {} 안에 딕셔너리 값을 넣을수있음

# 6번문제
print("[6번문제]")
e = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
e = list(set(e))
print(e)