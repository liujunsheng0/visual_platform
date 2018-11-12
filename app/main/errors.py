#!/usr/bin/python3
# -*- coding: utf-8 -*-

from flask import render_template

from . import main

@main.app_errorhandler(404)
def page_not_found(e):
    # return '404, %s' % str(e), 404
    return render_template('error/404.html', error=str(e))


@main.app_errorhandler(500)
def internal_server_error(e):
    # return '500, %s' % str(e), 500
    return render_template('error/500.html', error=str(e))

