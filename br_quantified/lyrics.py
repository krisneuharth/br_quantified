from time import sleep

from lyricwikia import Artist

from br_quantified.settings import *

ROOT = './br_quantified'


def get_lyrics():
    logger.info('Getting lyrics for %s...', BAND)
    artist = Artist(BAND)

    logger.info('Found %s albums.' % len(artist.albums))

    # Create paths
    os.makedirs('%s/data/%s' % (ROOT, BAND), exist_ok=True)

    # Albums
    for album in artist.albums:
        logger.info('ALBUM: %s - %s' % (album.year, album.title))

        os.makedirs(
            '%s/data/lyrics/%s/%s - %s' %
            (ROOT, BAND, album.year, album.title),
            exist_ok=True
        )

        # Songs
        for track, song in enumerate(album.songs):
            logger.info('\tSONG: %s - %s' % (track + 1, song.title))

            # Write out lyrics files
            with open('%s/data/lyrics/%s/%s - %s/%s - %s.txt' % (
                    ROOT, BAND, album.year, album.title, track + 1, song.title
                ), 'w+'
            ) as f:
                # File header
                f.write('# %s - %s\n\n' % (track + 1, song.title))

                # Lyrics
                f.write(song.lyrics)
                f.write('\n')

            # After song, sleep
            sleep(0.25)

        # After album, sleep
        sleep(0.5)
