# -*- coding: utf-8 -*-
import os
import glob
import json

import utils
from app import app
from flask import render_template, redirect, url_for, request, jsonify
from config import BASEDIR, IMG_DIR, SVG_DIR


@app.route('/')
def index():
    return 'ahoj'


@app.route('/show')
def show():
    img_path = '/static/img/IMAG0175.jpg'
    svg_path = os.path.join(BASEDIR, 'app', 'static', 'svg', 'IMAG0175.svg')
    with open(svg_path) as infile:
        svg_data = infile.read()
    return render_template('show.html',
                           img_path=img_path,
                           svg_data=svg_data)


@app.route('/generate', methods=['GET', 'POST'])
def generate():
    ALL_IMGS = [path.split('/app')[1] for path in glob.glob(IMG_DIR + '/*.*')]

    curr_idx = request.args.get('curr_idx')
    if curr_idx is None:
        curr_idx = 0
    curr_idx = int(curr_idx)

    if curr_idx >= len(ALL_IMGS):
        return redirect(url_for('finished'))

    img_path = ALL_IMGS[curr_idx]
    img_name = img_path.split('/')[-1].split('.')[0]

    if request.method == 'POST':

        svg_path = os.path.join(SVG_DIR, '{}.svg'.format(img_name))

        with open(svg_path, 'w+') as outfile:
            outfile.write(request.form['vector'])

        return redirect(url_for('generate', curr_idx=curr_idx + 1))

    return render_template('generate.html',
                           img_path=img_path,
                           curr_idx=curr_idx)


@app.route('/finished')
def finished():
    return 'Finished.'
