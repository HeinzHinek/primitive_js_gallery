# -*- coding: utf-8 -*-
import os
import glob

SECRET_KEY = "super secret change this plz"

BASEDIR = os.path.abspath(os.path.join(os.path.dirname(__file__)))

IMG_DIR = os.path.join(BASEDIR, 'app', 'static', 'img')
SVG_DIR = os.path.join(BASEDIR, 'app', 'static', 'svg')
