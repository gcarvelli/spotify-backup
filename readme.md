
# spotify-backup
Download your Spotify playlists information! This application utilizes [Spotipy](https://github.com/plamere/spotipy) (an unofficial Spotify API wrapper for Python).

### Using spotify-backup

1. Visit [developer.spotify.com](developer.spotify.com) and register your application.
1. Copy `example-config.json` to `config.json` and enter your client id, client secret, and redirect uri (this is arbitrary, I use http://localhost/callback)
1. Find your username by navigating to your profile and clicking 'Copy Spotify URL', then enter it into `config.json`.

Then just launch to download playlist metadata!
```
python backup.py
```
