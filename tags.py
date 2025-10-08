import requests
from bs4 import BeautifulSoup

with open("sample.html", "r") as f:
    html_doc = f.read()

soup = BeautifulSoup(html_doc, 'html.parser')

# print(soup.prettify())
# print(soup.title.string, type(soup.title.string))
# print(soup.div)

# print(soup.find_all('div')[1])

# for links in soup.find_all('a'):
#     print(links.get('href'))
#     print(links.get_text())

# s = soup.find(id="link4")
# print(s.get("href"))

# print(soup.select("div.italic"))
# print(soup.select("span#italic_with_id"))
# print(soup.span.get('class'))

# print(soup.find(class_="italic"))


# for child in soup.find(id="container").children:
#     print(child)

# for parent in soup.find(class_="box").parents:
#     print(parent.name)

# cont = soup.find(class_="container")
# # print(cont)
# cont.name = "span"
# cont['class'] = "span"
# cont.string = "This is a span now"
# print(cont)

# ulTag = soup.new_tag("ul")
# liTag = soup.new_tag("li")
# liTag.string = "I am a list item"
# ulTag.append (liTag)

# liTag2 = soup.new_tag("li")
# liTag2.string = "I am another list item"
# ulTag.append (liTag2)

# soup.html.body.insert(0, ulTag)

# with open("modified.html", "w") as f:
#     f.write(str(soup))



# cont = soup.find(class_="container")
# print(cont.has_attr('class'))


def hasClass_notId(tag):
    return tag.has_attr('class') and not tag.has_attr('id')

results =soup.find_all(hasClass_notId)
print(results)