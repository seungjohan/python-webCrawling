import requests
from bs4 import BeautifulSoup


for year in range(2012, 2022) :
    url = "https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&qvt=0&query={}%EB%85%84%20%EC%98%81%ED%99%94%20%EC%88%9C%EC%9C%84".format(year)

    res = requests.get(url)
    res.raise_for_status

    soup = BeautifulSoup(res.text, "lxml")

    # images = soup.find_all("img", attrs={"class":"thum_msk"})
    img_tag = soup.select_one('div._content')

    images = img_tag.select('ul > li > div > a > img')

    for idx, image in enumerate(images):
        image_url = image["src"]

        if image_url.startswith("//"):
            image_url = "https" + image_url

        print(image["src"])

        image_res = requests.get(image_url)
        image_res.raise_for_status()

        with open("movie_{}_{}.jpg".format(year, idx + 1), "wb") as f:
            f.write(image_res.content)

        if idx >= 7:
            break


