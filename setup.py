#!/usr/bin/env python
import shutil
import os
from os.path import join, expanduser, join
from distutils.core import setup

# distutils do not allow to change the filename
# and I don't want to keep file named .mess in the repo
shutil.copy('sample-config', '.mess')

setup(name = 'mess',
      version = '1.0',
      description = 'Easy sharing of files using scp',
      author = 'Nikolay Bachiyski',
      author_email = 'nb@nikolay.bg',
      license = 'BSD',
      url = 'http://github.com/nb/mess/',
      scripts = ['mess'],
      data_files = [(join(expanduser('~')), ['.mess'])]
     )
     
os.unlink('.mess')