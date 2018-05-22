# -*- coding: utf-8 -*-
from flask import Flask

import logging
import sys

log = logging.getLogger(__name__)
out_hdlr = logging.StreamHandler(sys.stdout)
out_hdlr.setFormatter(logging.Formatter('%(asctime)s %(message)s'))
out_hdlr.setLevel(logging.INFO)
log.addHandler(out_hdlr)
log.setLevel(logging.INFO)


app = Flask(__name__)
app.config.from_object('config')

from app import base_views


if __name__ == '__main__':
    app.run()
