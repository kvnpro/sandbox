import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id="20f6ce7caf344872b2052e19833e24af",
        client_secret="b5ae1df58aa3469088f70e9d27560027",
        redirect_uri="http://localhost:8888/callback",
        scope="user-library-read",
    )
)

results = sp.current_user_saved_tracks()
for idx, item in enumerate(results["items"]):
    track = item["track"]
    print(idx, track["artists"][0]["name"], " – ", track["name"])
