# regular experience

import re

p = re.compile("ca.e") 
# . : (ca.e) , 하나의 문자를 의미 > care, cafe, case | (x) caffe
# ^ : (^de) , 문자열의 시작 > desk, desination | (x) fade
# $ : (se$) , 문자열의 끝 > case, base | (x) face

m1 = p.match("case") # 비교할려는 값과 match하는지
m2 = p.match("casse")
print(m1.group()) # match되지 않으면 에러가 발생
# print(m2.group())

if m2:
    print(m2.group())
else:
    print("It's not matched")

m = p.match("cafe")
m = p.match("careless") # match : 주어진 문자열의 처음부터 일치하는지 확인 -> error 없음

def print_match(m):
    if m:
        print("m.group():", m.group()) #일치하는 문자열 반환
        print("m.string():", m.string) #입력받는 문자열, 함수가 아니라 변수이므로 -> 괄호 X
        print("m.start():", m.start()) #일치하는 문자열의 시작 index
        print("m.end():", m.end()) #일치하는 문자열의 끝 index
        print("m.span():", m.span()) #일치하는 문자열의 시작 / 끝 index
    else:
        print("It's not matched")

# print_match(m)


m3 = p.search("good care") # search : 주어진 문자열 중에 일치하는게 있는지 확인
# careless 도 care가 포함되어있으므로 care 가 출력됨.
print_match(m3)

m4 = p.findall("careless cafe") # findadll : 일치하는 모든 것을 리스트 형태로 반환
print(m4)


#1. p = re.complie("원하는 형태")
#2. m = p.match("비교할 문자열") : 주어진 문자열의 처음부터 일치하는지 확인
#3. m = p.search("비교할 문자열") : 주어진 문자열 중에 일치하는게 있는지 확인
#4. m = p.findall("비교할 문자열") : 일치하는 모든 것을 "리스트" 형태로 반환

# 원하는 형태 : 정규식
# . : (ca.e) , 하나의 문자를 의미 > care, cafe, case | (x) caffe
# ^ : (^de) , 문자열의 시작 > desk, desination | (x) fade
# $ : (se$) , 문자열의 끝 > case, base | (x) face

#w3school -> run python > RegEX
#python re , 공식문서페이지에서 찾아보기 Module Contents 등등...