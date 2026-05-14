# Random Spotify Playlist Generator
Python program which allows you to create random Spotify playlists from existing created playlists in your Spotify account. The tool also allows you to view all your Spotify playlists from your Spotify library.

## Installation
Clone the Git repository onto your local machine. The program is run in the terminal and can be run using Python or [uv](https://docs.astral.sh/uv/guides/tools/#requesting-different-sources).
All commands are executed in the root of the project and all files are created in the root of the project. Note that the root of the project refers to the directory that the configuration file `pyproject.toml` is in.

## Configuration
### File with environmental variables (.env)
1. Go to [Spotify for Developers](https://developer.spotify.com/dashboard) and create a new application.
2. Note the Client ID and Client Secret.
3. Click "Edit Settings" and add `http://localhost:4070/callback` to Redirect URIs, where `localhost` is your local IP address.
4. Create a `.env` file in the project root with:
   - CLIENT_ID = your_client_id_here
   - CLIENT_SECRET = your_client_secret_here
   - REDIRECT_URI = http://localhost:4070/callback
   - SCOPE = playlist-read-private playlist-modify-private
  - Note that the scope parameters allow you to read and modify your Spotify private playlists.

### Parsed Arguments
- `--playlist-ids`: Spotify playlist IDs (one or more)
- `--limit`: Number of songs selected from an indicated playlist (or more).
- `--offset`: Number of songs skipped in an indicated playlist (or more) upon selection.
- `--list-tracks`: List the names and URIs of all the tracks in an indicated Spotify playlist (or more).
- `--list-playlists`: List the names and IDs of all your Spotify playlists in your Spotify library.
- `--shuffle`: Spotify playlist is shuffled upon selection.

## Usage
### Listing Playlists
To list all your Spotify playlists in your Spotify library, run the following command:
- Running in Python
  `python main.py --list-playlists`
- Running in uv
  `uv main.py --list-playlists`

### Listing Tracks
To list all the tracks in an indicated Spotify playlist, where `pid` is the ID of the Spotify playlist(s), run the following command:
- Running in Python
  `python main.py --playlist-ids pid --list-tracks`
- Running in uv
  `uv main.py --playlist-ids pid --list-tracks`

### Creating New Playlist from Existing Playlists
To create a new Spotify playlist of songs from existing Spotify playlists in an indicated Spotify, where `pid` is the ID of the Spotify playlist(s), `lim` is the number of songs selected from the indicated playlist(s), `ofs` is the number of songs skipped in the indicated playlist(s), run the following command:
- Running in Python
  `python main.py --playlist-ids pid --limit lim --offset ofs`
- Running in uv
  `uv  main.py --playlist-ids pid --limit lim --offset ofs`
By default, the song selection when creating the playlist is randomized, hence `--shuffle True` does not have to be added to the command. If you do NOT want to randomize the song selection from the playlist, add `--shuffle False` to the command.

## Contributions
All contributions are welcome! If you like this project, consider leaving a star.

## License
The source code of this project falls under the [MIT](https://github.com/thplko/rand-spotify-playlist-generator/blob/main/LICENSE), but it uses libraries with license AGPLv3 (thus a fully distributed version of this falls under AGPLv3).
