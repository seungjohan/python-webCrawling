import requests
import re


res = requests.get("http://www.google.co.kr")
print("responseCode :", res.status_code)

# if res.status_code == requests.status_codes.ok:
#     print("No Error")
# else:
#     print("Error")

res.raise_for_status()


