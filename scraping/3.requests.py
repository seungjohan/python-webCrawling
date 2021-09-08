import requests

res = requests.get("https://www.google.com/")
# res2 = requests.get("http://nadocoding.tistory.com")

print("ResponseCode :", res.status_code) # 200이면 정상
# print("ResponseCode2 :", res2.status_code)


# if res.status_code == requests.codes.ok:
#     print("It's fine")
# else:
#     print("It has some problems. [ErrorCode ", res.status_code, "]")

# == 같은 의미
# 스크래핑을 할 때 올바로 코드를 가져왔으면 문제가 없고, 문제가 있으면 에러를 내는 것
res.raise_for_status()


print(len(res.text))
print(res.text)

# 바로 file로 만들어서 볼 수 있는 방법
with open("mygoogle.html", "w", encoding="utf8") as f:
    f.write(res.text)