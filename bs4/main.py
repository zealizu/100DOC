from bs4 import BeautifulSoup
import requests
# with open("100DOC/bs4/website.html", "r") as file:
#     contents = file.read()

# soup = BeautifulSoup(contents, "html.parser")
# print(soup.title)
# print(soup.title.string)

# anchor = soup.find_all(name="a")

# for tag in anchor:
#     # print(tag.getText())
#     print(tag.get("href"))
    

# heading = soup.find(name="h1", id= "name")
# print(heading)

# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)

# company_url = soup.select(selector="p a")
# print(company_url)

response = requests.get("https://news.ycombinator.com/news")
# response.raise_for_status()
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

article_tag = soup.select(selector=".title .titleline a")
article_text = []
article_links = []
article_score = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_ ="score")]


for i in range(0, len(article_tag)-1):
    if i % 2 == 0:
        article_text.append(article_tag[i].getText())
        article_links.append(article_tag[i].get("href"))

# print(article_text)
# print(article_links)
highest_upvote_index = article_score.index(max(article_score))

print(highest_upvote_index)
print(article_text[highest_upvote_index])
print(article_links[highest_upvote_index])
print(article_score[highest_upvote_index])


