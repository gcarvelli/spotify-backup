import spotipy
import spotipy.util as util
import os
import json
import datetime

username = os.getenv('SPOTIPY_USERNAME')

token = util.prompt_for_user_token(username, 'playlist-read-private playlist-read-collaborative')

sp = spotipy.Spotify(auth=token)

playlists = sp.user_playlists(username)
discover = next((p for p in playlists['items'] if p['name'] == 'Discover Weekly'), None)

if discover:
    # spotify playlists are owner by the spotify user "spotifydiscover"
    save = {}
    save['name'] = discover['name']
    save['timestamp'] = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')
    save['tracks'] = []
    tracks = sp.user_playlist_tracks(discover['owner']['id'], discover['id'])

    for track in tracks['items']:

        t_save = {}
        t_save['id'] = track['track']['id']
        t_save['name'] = track['track']['name']
        t_save['album'] = track['track']['album']['name']
        t_save['artist'] = [ artist['name'] for artist in track['track']['artists'] ]
        save['tracks'].append(t_save)

    #if not os.path.exists(directory):
    #    os.makedirs(directory)
    print json.dumps(tracks)
