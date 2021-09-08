import requests
import re
from bs4 import BeautifulSoup


url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=1=4&backgroundColor="

# user-agent
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"}

res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

# print(res.text)


# li tag 중에서 class가 search-product로 시작하는 모든 eles 를 가져오는 것
items = soup.find_all("li", attrs={"class": re.compile("^search-product")})
# print(items[0].find("div", attrs={"class":"name"}).get_text())

for item in items:

    # 광고 태그가 붙은 광고제품은 제외한다.
    ad_badge = item.find_all("span", attrs={"class":"ad-badge-text"})
    if ad_badge:
        print("    <Except the ad badge>")
        continue


    # 제품명
    name = item.find("div", attrs={"class":"name"}).get_text()

    # 삼성 제품은 제외를 해보자
    if "삼성전자" in name:
        print("     <Except the Samsung device>")
        continue

    # 가격
    price = item.find("strong", attrs={"class":"price-value"}).get_text()
    
    # 평점
    # rate = item.find("em", attrs={"class":"rating"}).get_text()
    rate = item.find("em", attrs={"class":"rating"})

    if rate:
        rate = rate.get_text()
    else:
        # rate="No rate value"
        print("    <Except the badge which has no rate>")
        continue


    # 평점 수 
    # rate_count  = item.find("span", attrs={"class":"rating-total-count"}).get_text()
    rate_count  = item.find("span", attrs={"class":"rating-total-count"})

    if rate_count:
        rate_count = rate_count.get_text()
        rate_count = rate_count[1:-1] # 평점수는 (x) 형태이기 때문에 x만 빼줘야한다.
    else:
        # rate_count="No total rate value"
        print("    <Except the badge which has no total rate value>")
        continue

    # 리뷰 100개 이상, 평점 4.5 이상의 상품만 조회하기
    if float(rate) >= 4.5 and int(rate_count) >= 1000 :
        print(name, price, rate, rate_count)
    
