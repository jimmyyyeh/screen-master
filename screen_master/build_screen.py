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
from configparser import ConfigParser


class BuildScreen:
    """
    USAGE:
        python3 build_screen.py -s [section]
        -s section:
            build screen with specific section in config.ini
        -h help:
            show docstring
    CONFIG TEMPLATE:
        [section]
        window title = command (allow multiple lines)

    CONFIG EXAMPLE:
        [hello]
        window01 = python3
        window02 = echo \"HELLO world\"
        window03 = echo \"HELLO WORLD\";echo \"HEY PYTHON\"
        window04 = echo \"hello world\"
                   echo \"hey python\"
    """

    @staticmethod
    def _load_config(section):
        """
        load config in config.ini with specific section
        :param section:
        :return:
        """
        config = ConfigParser()
        config.read('config.ini')
        if section not in config:
            sys.exit(f'section not found in config {section}')
        return config[section]

    @staticmethod
    def _init_screen(section):
        """
        kill exists screen then create new one
        :param section:
        :return:
        """
        # kill exists screen
        os.system(f'screen -X -S {section} quit')
        # create new screen
        os.system(f'screen -dmS {section}')

    @staticmethod
    def _run_command_in_screen(section, window, command):
        """
        run command in screen which named after section with specific window
        :param section:
        :param window:
        :param command:
        :return:
        """
        os.system(
            f'screen -x -S {section} -p {window} -X stuff "{command}"')
        os.system(f'screen -x -S {section} -p {window} -X stuff "\n"')

    @classmethod
    def _build_screen(cls, section, config):
        """
        build screen with config
        :param section:
        :param config:
        :return:
        """
        for window, command_string in config.items():
            # create new window with title
            os.system(f'screen -S {section} -X screen -t {window}')
            for command in command_string.split(';'):
                cls._run_command_in_screen(section=section,
                                           window=window,
                                           command=command)

    @classmethod
    def run(cls):
        opts, args = getopt(sys.argv[1:], 'h-s:', ['help=', 'section='])
        opts_dict = dict(opts)

        if '-s' not in opts_dict:
            sys.exit(cls.__doc__)
        if not os.path.exists('../config.ini'):
            sys.exit('config.ini not found')

        section = opts_dict['-s']
        config = cls._load_config(section=section)

        cls._init_screen(section=section)
        cls._build_screen(section=section,
                          config=config)


if __name__ == '__main__':
    BuildScreen.run()
