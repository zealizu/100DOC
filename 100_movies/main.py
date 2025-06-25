import requests
from bs4 import BeautifulSoup
response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")

webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")

movies = soup.find_all(name="h3", class_="title")
movies_title = [(movie.getText()).encode('latin1').decode('utf-8') for movie in movies]
movies_title.reverse()

with open("100DOC/100_movies/movies.txt", "a") as file:
    for i in movies_title:
        file.write(f"{i}\n")
    

print(movies_title)