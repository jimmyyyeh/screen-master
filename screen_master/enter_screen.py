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


class EnterScreen:
    """
    USAGE:
        srun -s [screen name]
        -s screen name:
            screen which want to enter
        -h help:
            show docstring
    """

    @classmethod
    def _enter_screen(cls, screen_name=None):
        """
        execute enter screen command
        :param screen_name:
        :return:
        """
        os.system(f'screen -r {screen_name}')

    @classmethod
    def main(cls):
        opts, args = getopt(sys.argv[1:], 'h-s:', ['help=', 'screen='])
        opts_dict = dict(opts)
        screen_name = opts_dict.get('-s') or Utils.get_screen_name()

        if '-h' in opts_dict:
            sys.exit(cls.__doc__)

        if isinstance(screen_name, list):
            list(map(cls._enter_screen, screen_name))
        else:
            cls._enter_screen(screen_name=screen_name)


if __name__ == '__main__':
    EnterScreen.main()
