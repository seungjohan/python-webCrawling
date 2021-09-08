import requests
import re
from bs4 import BeautifulSoup

# 여러 페이지에 있는 정보들 가져오기 -> page number를 계속 바꿔주기

headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"}

for i in range(1, 6):
    print("Page :", i)
    url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={}&rocketAll=false&searchIndexingToken=1=4&backgroundColor=".format(i)
        
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    items = soup.find_all("li", attrs={"class": re.compile("^search-product")})
    for item in items:

        # 광고 태그가 붙은 광고제품은 제외한다.
        ad_badge = item.find_all("span", attrs={"class":"ad-badge-text"})
        if ad_badge:
            # print("    <Except the ad badge>")
            continue

        name = item.find("div", attrs={"class":"name"}).get_text()

        # 삼성 제품은 제외를 해보자
        if "삼성전자" in name:
            # print("     <Except the Samsung device>")
            continue

        price = item.find("strong", attrs={"class":"price-value"}).get_text()
        rate = item.find("em", attrs={"class":"rating"})

        if rate:
            rate = rate.get_text()
        else:
            # print("    <Except the badge which has no rate>")
            continue

        rate_count  = item.find("span", attrs={"class":"rating-total-count"})

        if rate_count:
            rate_count = rate_count.get_text()
            rate_count = rate_count[1:-1] 
        else:
            # print("    <Except the badge which has no total rate value>")
            continue

        link = item.find("a", attrs={"class":"search-product-link"})["href"]

        if float(rate) >= 4.5 and int(rate_count) >= 1000 :
            # print(name, price, rate, rate_count)
            print(f"Item: {name}")
            print(f"Price: {price}")
            print(f"Score: {rate}, (Number : {rate_count})")
            print("Going To : {}".format("https://www.coupang.com" + link))
            print("-"*100) # draw line