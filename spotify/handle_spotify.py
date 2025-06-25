from dotenv import load_dotenv
# import requests
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
# from pprint import pprint

load_dotenv()

class HandleSpotify:
    def __init__(self):
        self.client_id = os.environ["SPOTIFY_ID"]
        self.client_secret = os.environ["SPOTIFY_SECRET"]
        self.username = os.environ["USERNAME"]
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id= self.client_id,client_secret=self.client_secret,
        redirect_uri="https://example.com",
        scope="playlist-modify-private",
        show_dialog=True,
        cache_path="token.txt",
        username=self.username,
        requests_timeout=15))
    
    def get_song(self, song_list,artist):
        song_list = song_list
        artist = artist
        urls = []
        
        for i in range(0, len(song_list)):
            result = self.sp.search(q=f"track:{song_list[i]} artist:{artist[i]}", type="track")
            try:
                song_uri = result["tracks"]["items"][0]["uri"]
                # print(song_uri)
                urls.append(song_uri)
            except IndexError:
                print("Track number " + str(i + 1) + " cannot be found")
        
        return urls
    
    def create_playlist(self, song_list,artist, year):
        self.user_id = self.sp.current_user()["id"]
        song_list = song_list
        artist = artist
        
        self.urls = self.get_song(song_list, artist)
        
        playlist = self.sp.user_playlist_create(user= self.user_id, name=f"{year} Billboard top 100", public=False, description=f"Top 100 songs from {year}")
        
        self.sp.user_playlist_add_tracks(self.user_id, playlist["id"], self.urls)
        print(f"\n...Your playlist has been created, we managed to find a total of {len(self.urls)}/100 of the top 100 songs! ")