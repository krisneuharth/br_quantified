from br_quantified.settings import *

from br_quantified.audio import *
from br_quantified.lyrics import *


def run():
    get_lyrics()
    get_audio()


if __name__ == '__main__':
    # Run from command line but provide a way to run as method
    run()
