import requests
from bs4 import BeautifulSoup


url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status()

# 우리가 가져온 html을 lxml parser를 이용해 bs 객체로 만든 것
# soup 변수가 모든 정보를 가지고 있다.
soup = BeautifulSoup(res.text, "lxml")

print(soup.title)
print(soup.title.get_text())

# soup 이 가지고 있는 html 객체 정보중에서 첫번째로 발견되는 a 태그 element를 반환
print(soup.a)

# a element 의 속성 (attribute), dictionary 형태로 출력
print(soup.a.attrs)

# a element 의 'href' 속성 '값' 정보를 출력
print(soup.a["href"])


# find
# soup에 있는 모든 객체 중에서 a element에 해당하는데 class의 속성 중에서 Nbtn_upload에 해당하는 첫번째 element를 반환하라
# Class = "Nbtn_upload" 인 a element 를 찾아줘
print(soup.find("a", attrs={"class":"Nbtn_upload"}))
# 이것도 가능, 그렇지만 태그 div, a 등을 명확히 명시하면 더 정확해진다.
# Class="Nbtn_upload" 인 어떤 element를 찾아줘
print(soup.find(attrs={"class":"Nbtn_upload"})) 


print(soup.find("li", attrs={"class":"rank01"}))

rank1 = soup.find("li", attrs={"class":"rank01"})
print(rank1.a)


# x_path에서 배웠던 부모-자식-형제 노드간의 이동
# next
rank1 = soup.find("li", attrs={"class":"rank01"})
print(rank1.a.get_text())
print(rank1.next_sibling) # print 안됨
print(rank1.next_sibling.next_sibling) # 태그 사이에 줄바꿈 등의 뭔가 처리가 되서 그럴 수 있음.

rank2 = rank1.next_sibling.next_sibling
rank3 = rank2.next_sibling.next_sibling
print(rank3.a.get_text())

# 반대로 뒤로, previous
rank2 = rank3.previous_sibling.previous_sibling
print(rank2.a.get_text())

# 부모노드로 올라가기
print(rank1.parent)


# next_sibling을 두 번 쓰기가 애매하고, 사이트마다 처리가 다르기 때문에 일반적으로 쓸 수 있는 방법
rank2 = rank1.find_next_sibling("li") # rank1 = soup.find("li", attrs={"class":"rank01"}), rank1이 Li태그를 찾고 있다. -> Li
print(rank2.a.get_text())

rank3 = rank2.find_next_sibling("li")
print(rank3.a.get_text())
rank2 = rank3.find_previous_sibling("li")
print(rank2.a.get_text())


# 한꺼번에 일처리할려고 할 때, 순위 한 번에 1-10등까지 전부 뽑아내고 싶을 때
print(rank1.find_next_siblings("li"))


# a tag 를 찾는데 text를 통해 비교해볼 수도 있다.
# text는 <a></a>사이에 있기 때문에 이 사이에 있는 것을 찾아서 가져온다.
webtoon = soup.find("a", text="나만 보여!-31화")
print(webtoon)