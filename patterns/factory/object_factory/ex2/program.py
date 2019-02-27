
import music


config = {
    'spotify_client_key': 'SPOTIFY_CLIENT_KEY',
    'spotify_client_secret': 'SPOTIFY_CLIENT_SECRET',
    'pandora_client_key': 'PANDORA_CLIENT_KEY',
    'pandora_client_secret': 'PANDORA_CLINET_SECRET',
    'local_music_location': '/usr/data/music'
}

pandora = music.services.get('PANDORA', **config)
pandora.test_connection()

spotify = music.services.get('SPOTIFY', **config)
spotify.test_connection()

local = music.services.get('LOCAL', **config)
local.test_connection()


pandora_two = music.services.get('PANDORA', **config)
print(f'id(pandora) == id(pandora_two) : {id(pandora) == id(pandora_two)}')

spotify_two = music.services.get('SPOTIFY', **config)
print(f'id(spotify) == id(spotify_two) : {id(spotify) == id(spotify_two)}')