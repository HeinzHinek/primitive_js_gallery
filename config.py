# -*- coding: utf-8 -*-
import os
import glob
import random

SECRET_KEY = "super secret change this plz"

BASEDIR = os.path.abspath(os.path.join(os.path.dirname(__file__)))

IMG_DIR = os.path.join(BASEDIR, 'app', 'static', 'img')
SVG_DIR = os.path.join(BASEDIR, 'app', 'static', 'svg')


IMAGE_NAMES = [item.split('/')[-1]
               for item
               in glob.glob(
                   os.path.join(BASEDIR, 'app', 'static', 'img') + '/*.*')
              ]
random.shuffle(IMAGE_NAMES)
