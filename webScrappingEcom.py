import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from pandas import DataFrame
# url = "https://timesofindia.indiatimes.com/world/pakistan/us-pakistan-deal-islamabad-to-receive-aim-120-missiles-compatible-with-its-f-16s-used-in-retaliation-to-balakot-strikes/articleshow/124374883.cms"

url="https://www.amazon.in/s?k=earbuds+buds&crid=3BAPXNMX3WUHY&sprefix=ear%2Caps%2C442&ref=nb_sb_ss_mvt-t11-ranker_2_3"

headers = {
    "User-Agent": UserAgent().random,  # random browser agent
    "Accept-Language": "en-IN,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive"
}

proxies = {
"http": "http://scraperapi:APIKEY@proxy-server.scraperapi.com:8001"
}

r = requests.get(url, headers=headers, proxies=proxies)
with open("file.html", "w", encoding="utf-8") as f:
    f.write(r.text)

soup = BeautifulSoup(r.text, 'html.parser')
# span = soup.find_all("div", class_="puisg-col-inner")
# # print(soup.prettify())

# # print(span, type(span))
# price = soup.find_all("span", class_="a-price-whole")
# for s in span:
#     print(s.get_text() + "\n")
#     print(s.children)

# for price in price:
#     print(price.string + "\n")

# for s in span:
#     print(s.text + "\n")

# print(span.title, type(span.title))

# print("✅ HTML saved successfully!")

products = soup.find_all("div", {"data-component-type": "s-search-result"})
data = {"Title": [], "Price": []}

for product in products:
    # Extract title
    title_tag = product.find("span")
    title = title_tag.get_text(strip=True) if title_tag else "N/A"

    data["Title"].append(title)

    # Extract price
    price_tag = product.find("span", class_="a-price-whole")
    price = price_tag.get_text(strip=True) if price_tag else "N/A"
    data["Price"].append(price)

    df = DataFrame(data)
    df.to_csv("products.csv", index=False)
    print(f"🛒 {title} — ₹{price}\n") 