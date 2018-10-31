#!/usr/bin/python3
# -*- coding: utf-8 -*-

from flask import render_template, request, session, g, redirect, url_for

from . import main


@main.route('/', methods=['GET', 'POST'])
def index():
    username = request.form.get('username', '')
    password = request.form.get('password', '')
    if not username and not session.get('username'):
        return redirect(url_for('auth.login'))
    if username:
        session['username'] = username
        g.user = username
    return render_template('base/base.html')
