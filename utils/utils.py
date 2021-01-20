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


class Utils:
    @classmethod
    def get_screen_name(cls):
        """
        list all screen
        :return:
        """
        screen_name_list = os.popen('screen -r |'
                                    ' awk \'/[At|De]tached/ {print $1}\' |'
                                    ' awk \'BEGIN {FS="."} {print $2}\'').readlines()
        if not screen_name_list:
            sys.exit('screen not found')

        screen_name_list = [screen_name.strip() for screen_name in screen_name_list]
        screen_name_menu = '\n'.join([f'【{index}.】 {screen_name}'
                                      for index, screen_name in enumerate(screen_name_list)])

        index = input('Please Enter Screen Index:\n'
                      '====================\n'
                      f'{screen_name_menu}\n'
                      f'====================\n')
        if index == '':
            return screen_name_list
        else:
            index = int(index)
            if index > len(screen_name_list):
                sys.exit('screen index error')
            else:
                screen_name = screen_name_list[index]
                return screen_name
