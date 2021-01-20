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
import setuptools

with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
    name='screen-master',
    version='0.0.1',
    author='Jimmy Yeh',
    author_email='chienfeng0719@hotmail.com',
    description='A tool for build GNU screen automatically',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/chienfeng0719/screen-master',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    entry_points={
        'console_scripts': [
            'sbuild = screen_master:BuildScreen.main',
            'skill = screen_master:KillScreen.main',
            'srun = screen_master:EnterScreen.main',
        ]
    },
    python_requires='>=3.6',
)
