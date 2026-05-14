import sys
import random as rand
from spotipy.oauth2 import SpotifyOauthError
from auth import auth_client
from playlist import *
from parser import parse_arguments

def main():
    args = parse_arguments()

    print(f"Authenticating...")
    try:
        client = auth_client()
        print("Authentication successful.")
    except SpotifyOauthError:
        print("Authentication failed, please check that your client ID and secret are correct.")
        sys.exit(1)

    # Checking arguments
    if args.list_playlists:
        name_playlists(client)
        sys.exit(1)

    if args.list_tracks:
        if not args.playlist_ids:
            print("At least one playlist ID is required.")
        for playlist in args.playlist_ids:
            name_tracks(client, playlist, args.limit, args.offset)
        sys.exit(0)

    if not args.playlist_ids:
        print("At least one playlist ID is required.")
        sys.exit(1)

    if not args.limit:
        print(f"The default limit used is {len(track_uris)}.")
    if not args.offset:
        print("The default offset used is 0.")
    if not args.shuffle:
        print("The playlist is not shuffled.")

    # Begin song selection
    print(f"Selecting songs...")
    print(f"Playlist IDs: {args.playlist_ids}")
    print(f"Limit per playlist: {args.limit}")
    print(f"Offset per playlist: {args.offset}")
    
    track_uris = []
    for playlist in args.playlist_ids:
        uris = get_tracks(client, playlist, args.limit, args.offset, args.shuffle)
        track_uris.extend(uris)

    if not track_uris:
        print("No tracks were retrieved. Program exitting.")
        sys.exit(1)

    print(f"Total tracks selected: {len(track_uris)}")

    # Begin playlist generation
    playlist_name = input("Enter name for the new playlist: ").strip()    
    if not playlist_name:
        playlist_name = "New Playlist"
    status = input("Make playlist public? (y/n): ").strip().lower() == 'y'
    collab = input("Make playlist collaborative? (y/n): ").strip().lower() == 'y'
    desc = input("Enter playlist description: ").strip().lower()

    generate_playlist(client, track_uris, playlist_name, status, collab, desc)
    print("Playlist generation completed!")    
    sys.exit(1)

if __name__ == "__main__":
    main()
