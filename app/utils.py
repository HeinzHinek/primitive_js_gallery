# -*- coding: utf-8 -*-
from config import BASEDIR
from app import log
from flask import flash, redirect, url_for, session
from functools import wraps
from flask_login import current_user
from xml.dom import minidom


def admin_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user.is_admin:
            return f(*args, **kwargs)
        else:
            flash(u'アクセスが制限されています！', 'alert-danger')
            return redirect(url_for('index'))
    return decorated_function


def sync_session_page(endpoint, page):
    cache = session.get('curr_page_cache', {})

    if page:
        cache[endpoint] = page
    else:
        page = cache[endpoint] if endpoint in cache and cache[endpoint] > 1 else 1

    session['curr_page_cache'] = cache

    return page


def show_fatal_error(ex):
    log.error(ex)
    template = u"エラーが発生しました! エラーの種類：{0}。アーギュメント：\n{1!r}"
    message = template.format(type(ex).__name__, ex.args)
    flash(message, 'alert-danger')


def parse_svg(svg_path):
    doc = minidom.parse(svg_path)

    rect = doc.getElementsByTagName('rect')[0]
    rect_data = {
        'x': rect.getAttribute('x'),
        'y': rect.getAttribute('y'),
        'width': rect.getAttribute('width'),
        'height': rect.getAttribute('height'),
        'fill': rect.getAttribute('fill'),
    }

    path_data = [{
        'd': path.getAttribute('d'),
        'fill': path.getAttribute('fill'),
        'fillOpacity': path.getAttribute('fill-opacity'),
    } for path in doc.getElementsByTagName('path')]
    
    return {
        'rect': rect_data,
        'paths': path_data
    }
