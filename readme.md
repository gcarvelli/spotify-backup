
# spotify-backup
Download your Spotify playlists information! This application utilizes [Spotipy](https://github.com/plamere/spotipy) (an unofficial Spotify Python API wrapper).

### Using spotify-backup

spotify-backup requires the following environment variables to be declared.

```
SPOTIPY_CLIENT_ID="Spotify client ID from developer.spotify.com"
SPOTIPY_CLIENT_SECRET="Spotify client secret from developer.spotify.com"
SPOTIPY_REDIRECT_URI="callback you added in your Spotify app (ex. http://localhost/callback)"
SPOTIPY_USERNAME="your Spotify username (find by navigating to your profile and clicking 'Copy Spotify URL')"
SPOTIPY_DIRECTORY="directory to store backups"
```

Then just launch to download playlists!
```
python backup.py
```
