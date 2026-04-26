import random as rand
from typing import List, Dict
from spotipy.client import Spotify    

def get_tracks(client: Spotify, playlist_id: str, lim: int, offset: int, shuffle: bool) -> List[str]:
    """
    Return all tracks in a given Spotify playlist.

    Parameters:
    :client: Spotify client
    :playlist_id: Spotify playlist ID
    :lim: Number of tracks selected from the Spotify playlist
    :offset: The first ... tracks skipped from the Spotify playlist upon selection
    :randomized: Indication of randomizing the tracks in the playlist
    :return: List of tracks (randomized or not)
    """
    if lim == 0:
        print("No songs were selected.")
        return []

    tracks: List[str] = []
    num_fetched = 0
    current_offset = offset

    while num_fetched < lim:            
        results = client.playlist_tracks(
            playlist_id, 
            limit = min(100, lim - num_fetched), 
            offset = offset
        )
        for item in results['items']:
            # Checks if the track (and a URI) exists
            if item and item.get('track') and item['track'].get('uri'):
                tracks.append(item['track']['uri'])
                num_fetched += 1
                if num_fetched > lim:
                    break
        
        if not results['next']:
            break

        current_offset += len(results['items'])

    # Fewer tracks than requested
    if len(results['items']) < lim:
        print("Playlist {playlist_id} has fewer songs than the indicated limit.")

    # Shuffle the playlist if indicated
    if shuffle:
        rand.shuffle(tracks)

    return tracks

def get_playlists(client: Spotify) -> List[Dict]:
    """
    Return all playlists in your Spotify music library.

    Parameters:
    :client: Spotify client
    :return: List of playlists
    """
    playlists = []
    results = client.current_user_playlists()
    playlists.extend(results['items'])
    
    while results['next']:
        results = client.next(results)
        playlists.extend(results['items'])

    return playlists

def name_playlists(client: Spotify) -> None:
    """
    List all created playlists in your Spotify account.

    Parameters:
    :client: Spotify client
    """
    playlists = get_playlists(client)

    print("\nYour Spotify Playlists:")
    print(f"{"ID":<30} {'Name'}")
    print("-" * 60)

    for playlist in playlists:
        print(f"{playlist['id']:<30} {playlist['name']}")
    print(f"\nTotal: {len(playlists)} playlists")

def name_tracks(client: Spotify, playlist_id: str, lim: int, offset: int) -> None:
    """
    List all track URIs in a Spotify playlist.

    Parameters:
    :client: Spotify client
    :playlist_id: Spotify playlist ID
    :lim: Number of tracks selected from the Spotify playlist
    :offset: The first ... tracks skipped from the Spotify playlist upon selection
    """
    tracks = get_tracks(client, playlist_id, lim, offset, bool)

    print("\nYour Tracks in Playlist {playlist_id}:")
    print(f"{"URI":<40} {'Name'}")
    print("-" * 40)

    for track in tracks:
        print(track)
    print(f"\nTotal: {len(tracks)} tracks")

def generate_playlist(client: Spotify, uris: List[str], playlist_name: str, status: bool, collab: bool, desc: str) -> None:
    """
    Generate a new playlist from track URIs.

    Parameters:
    :client: Spotify client
    :uris: List of track URIs
    :playlist_name: Name of newly generated Spotify playlist
    :status: Privacy of newly generated Spotify playlist
    :collab: Collaboration indication of newly generated Spotify playlist
    :desc: Description of newly generated Spotify playlist
    """
    new_playlist = client.current_user_playlist_create(
        playlist_name, 
        public = status, 
        collaborative = collab, 
        description = desc
    )
    
    for i in range (0, len(uris), 100):
        client.playlist_add_items(new_playlist['id'], uris[i: i + 100])