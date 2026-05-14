import spotipy
import os
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth

def auth_client():
    """
    Authenticate a Spotify client.
    """
    load_dotenv(verbose = True)
    CLIENT_ID = os.getenv("CLIENT_ID")
    CLIENT_SECRET = os.getenv("CLIENT_SECRET")
    REDIRECT_URI = os.getenv("REDIRECT_URI")
    SCOPE = os.getenv("SCOPE")
    authentication_manager = SpotifyOAuth(client_id = CLIENT_ID, 
                                        client_secret = CLIENT_SECRET,
                                        redirect_uri = REDIRECT_URI,
                                        scope = SCOPE)

    return spotipy.Spotify(auth_manager = authentication_manager, requests_timeout = (5, 60))