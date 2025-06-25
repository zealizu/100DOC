import requests
from bs4 import BeautifulSoup

class ScrapeBillboard:
    def __init__(self, year):
        self.year = year
        self.url = f"https://www.billboard.com/charts/hot-100/{year}"
        self.header ={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36"
            }
        response = requests.get(url=self.url, headers=self.header)
        webpage = response.text
        # print(webpage)
        self.soup = BeautifulSoup(webpage, "html.parser")
    def get_song_list(self):
        songs = self.soup.select(selector="li #title-of-a-story")
        artists = self.soup.find_all(name="span", class_="a-font-primary-s")
        self.artists = [artist.getText().strip() for artist in artists]
        for i in self.artists:
            if i == "RIAA Certification:":
                self.artists.remove(i)
        self.song_list = [song.getText().strip() for song in songs]
        return self.song_list, self.artists