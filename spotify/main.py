from datetime import datetime
from scrap_billboard import ScrapeBillboard
from handle_spotify import HandleSpotify

while True:
    year_str:str = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:").strip()
    try:
        # Try converting the input string to a date
        year = datetime.strptime(year_str, "%Y-%m-%d")
        break  # Exit the loop if valid
    except ValueError:
        print("❌ Invalid date format or non-existent date. Please enter the date as YYYY-MM-DD.")

scrap = ScrapeBillboard(year_str)

song_list, artists = scrap.get_song_list()


handle_spotify = HandleSpotify()
# print(song_list)

# print(handle_spotify.get_song(song_list, artists))
handle_spotify.create_playlist(song_list, artists, year_str)