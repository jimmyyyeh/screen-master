# -*- coding: utf-8 -*
"""
      ┏┓       ┏┓
    ┏━┛┻━━━━━━━┛┻━┓
    ┃      ☃      ┃
    ┃  ┳┛     ┗┳  ┃
    ┃      ┻      ┃
    ┗━┓         ┏━┛
      ┗┳        ┗━┓
       ┃          ┣┓
       ┃          ┏┛
       ┗┓┓┏━━━━┳┓┏┛
        ┃┫┫    ┃┫┫
        ┗┻┛    ┗┻┛
    God Bless,Never Bug
"""

import os
import sys
from getopt import getopt

from utils.utils import Utils


class KillScreen:
    """
    USAGE:
        skill -s [screen name]
        -s screen name:
            screen which want to kill
        -h help:
            show docstring
    """

    @classmethod
    def _kill_screen(cls, screen_name=None):
        """
        execute kill screen command
        :param screen_name:
        :return:
        """
        os.system(f'screen -X -S {screen_name} quit')

    @classmethod
    def main(cls):
        opts, args = getopt(sys.argv[1:], 'h-s:', ['help=', 'screen='])
        opts_dict = dict(opts)
        screen_name = opts_dict.get('-s') or Utils.get_screen_name()

        if '-h' in opts_dict:
            sys.exit(cls.__doc__)

        if isinstance(screen_name, list):
            list(map(cls._kill_screen, screen_name))
        else:
            cls._kill_screen(screen_name=screen_name)


if __name__ == '__main__':
    KillScreen.main()
