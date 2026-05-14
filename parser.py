import argparse

def parse_arguments():
    """
    Creating command-line arguments for using the program.
    """
    parser = argparse.ArgumentParser(
        prog = 'RandomSpotifyGenerator',
        description = "Generate new playlists with randomly selected songs from existing Spotify playlists.",    
    )
    parser.add_argument(
        "--playlist-ids",
        type = str,
        nargs = '+',
        help = "One or more Spotify playlist IDs."
    )
    parser.add_argument(
        "--limit", 
        type = int,
        help = "Number of songs taken from selected playlists."
    )
    parser.add_argument(
        "--offset", 
        type = int, 
        default = 0,
        help = "Number of songs skipped in the playlist upon selection."
    )
    parser.add_argument(
        "--list-tracks",
        action = "store_true",
        help = "List the names and URIs of all your tracks in a given Spotify playlist."
    )
    parser.add_argument(
        "--list-playlists",
        action = "store_true",
        help = "List the names and IDs of all your Spotify playlists."
    )
    parser.add_argument(
        "--shuffle",
        action = "store_true",
        default = True,
        help = "Spotify playlist is shuffled."
    )
    return parser.parse_args()