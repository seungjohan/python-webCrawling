import csv
import requests
from bs4 import BeautifulSoup

url = "https://coinmarketcap.com/ko/rankings/exchanges/"

filename = "Ranking of best selling bitcoin.csv"
f = open(filename, "w", encoding="utf-8-sig", newline="")
writer = csv.writer(f)

title = "순위,이름,거래 점수,거래량(24시간),평균 유동성,주별 방문,#마켓,#코인,지원 화폐,거래량 그래프(7일)".split(",")
writer.writerow(title)

res = requests.get(url)
res.raise_for_status
soup = BeautifulSoup(res.text, "lxml")

data_rows = soup.find("table", attrs={"class":"h7vnx2-2 kDGuD cmc-table"}).find("tbody").find_all("tr")
for row in data_rows:
    columns = row.find_all("td")

    if len(columns) <= 1:
        continue

    data = [column.get_text().strip() for column in columns]
    writer.writerow(data)