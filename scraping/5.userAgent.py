# smartphone, laptop 에게 보이는 화면 차이는
# 브라우저가 website에 접속할 때 주는 head 정보에 따라서 선택적으로 보여진다.

# 근데 사람이 아닌 웹스크래핑 또는 크롤링을 하는 컴퓨터가 접속한다고 하면
# 정보를 확인하고 접속을 차단할 수 있다.

# request를 이용해서 접속할 때 등이 있는데 이를 userAgent를 이용해서 해결할 수 있다.

import requests

url = "https://techblog.woowahan.com/"
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"}

res = requests.get(url, headers=headers)
# res = requests.get(url)
res.raise_for_status()

with open("woowahanblogwithuseragent.html", "w", encoding="utf8") as f:
    f.write(res.text)