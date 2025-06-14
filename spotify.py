import json
import spotipy
import os
from spotipy.oauth2 import SpotifyOAuth

class Spotify:
    def __init__(self):
        self.auth_manager = SpotifyOAuth(open_browser=False)
        self.get_access_token()
        self.connection = None
        self.connect()
        self.total_tracks = 0
        self.tracks = []
        

    def get_access_token(self):
        self.token_info = self.auth_manager.refresh_access_token(os.getenv('REFRESH_TOKEN'))

    def connect(self):
        print("Attempting Spotify connection...")
        try:
            self.connection = spotipy.Spotify(auth=self.token_info["access_token"])
            print("Connected to Spotify.")
        except Exception as e:
            raise Exception(f"Error during connection: {e}")

    def make_request(self, limit, offset):
        results = self.connection.current_user_saved_tracks(limit=limit, offset=offset)
        return results
    
    def run_loop(self, items, results, limit, offset):
        tracks_populate = []
        while (items):
            for item in items:
                track = item['track']
                track_info = {
                    'name': track['name'],
                    'artists': [artist['name'] for artist in track['artists']]
                }
                tracks_populate.append(track_info)
                self.percentage = (len(tracks_populate) / self.total_tracks) * 100
                print(f"Saved track: {track_info} ({self.percentage:.2f}% complete)")
            
            offset += limit
            results = self.make_request(limit=limit, offset=offset)
            items = results['items']
        return tracks_populate
    
    def generate_json_file(self):
        with open('saved_tracks.json', 'w', encoding='utf-8') as f:
            json.dump(self.tracks, f, ensure_ascii=False, indent='\t')
        print(f"Saved {len(self.tracks)} tracks to 'saved_tracks.json'")

    def runner(self):
        limit = 50
        offset = 0
        results = self.make_request(limit=limit, offset=offset)
        self.total_tracks = results['total']
        print(f'Total tracks: {self.total_tracks}')
        items = results['items']
        self.tracks = self.run_loop(items=items, results=results, limit=limit, offset=offset)
        self.generate_json_file()


if "__main__" == __name__:
    spotify = Spotify()
    spotify.runner()
