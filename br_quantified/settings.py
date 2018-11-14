import os
import logging

# General
DEBUG = False
BAND = 'Bad Religion'

# Genius
# https://genius.com/artists/Bad-religion
# https://genius.com/api-clients
GENIUS_CLIENT_ID = os.environ.get('GENIUS_CLIENT_ID')
GENIUS_CLIENT_SECRET = os.environ.get('GENIUS_CLIENT_SECRET')
GENIUS_CLIENT_ACCESS_TOKEN = os.environ.get('GENIUS_CLIENT_ACCESS_TOKEN')

# Spotify
# https://open.spotify.com/artist/2yJwXpWAQOOl5XFzbCxLs9
# https://developer.spotify.com/dashboard/applications
SPOTIFY_CLIENT_ID = os.environ.get('SPOTIFY_CLIENT_ID')
SPOTIFY_CLIENT_SECRET = os.environ.get('SPOTIFY_CLIENT_SECRET')

# Logging
logging.basicConfig(
    format='%(levelname)s - %(message)s',
    level=logging.DEBUG if DEBUG else logging.INFO
)
logger = logging.getLogger()
