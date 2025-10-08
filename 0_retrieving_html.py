import requests
import time
from fake_useragent import UserAgent

url = "https://timesofindia.indiatimes.com/world/pakistan/us-pakistan-deal-islamabad-to-receive-aim-120-missiles-compatible-with-its-f-16s-used-in-retaliation-to-balakot-strikes/articleshow/124374883.cms"


payload = { 'api_key': '94365bf6b6141c78e48c15910e453ca5', 'url': 'https://httpbin.org/' }
r = requests.get(url, params=payload)

def fetchAndSaveHTML():
    r = requests.get(url)
    with open("file.html", "w", encoding="utf-8") as f:
        f.write(r.text)


fetchAndSaveHTML()
print("✅ HTML saved successfully!")

# session = requests.Session()

# # ✅ Correct proxy dictionary format
# proxies = {
#     'http': 'http://14.251.13.0:8080',
#     'https': 'http://14.251.13.0:8080'
# }

# headers = {
#     'User-Agent': UserAgent().random,
#     'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8,hi;q=0.7',
#     'Accept-Encoding': 'gzip, deflate, br, zstd',
#     'Connection': 'keep-alive',
#     'Referer': 'https://www.amazon.in'
# }

# time.sleep(2)
# r = session.get(url, proxies=proxies, headers=headers)


