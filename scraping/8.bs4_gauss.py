import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list?titleId=335885"
res = requests.get(url)
res.raise_for_status

soup = BeautifulSoup(res.text, "lxml")

cartoons = soup.find_all("td", attrs={"class":"title"})
# title = cartoons[0].a.get_text()
# link = cartoons[0].a["href"]

# print(title)
# print("https://comic.naver.com" + link)

# 만화 제목과 링크 가져오기
for cartoon in cartoons:
    title = cartoon.a.get_text()
    link = "https://comic.naver.com" + cartoon.a["href"]
    print(title, link)


# 별점을 가지고 평균 평점 내보기
total_rates = 0

cartoonratings = soup.find_all("div", attrs={"class":"rating_type"})

for cartoonrating in cartoonratings:
    rate = cartoonrating.find("strong").get_text()
    print(rate)
    total_rates += float(rate)

print("total_score", total_rates)
print("median_score", total_rates / len(cartoonratings))
