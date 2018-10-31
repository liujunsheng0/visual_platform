#!/usr/bin/python3
# -*- coding: utf-8 -*-


from flask import render_template, session

from . import auth


@auth.route('/login')
def login():
    return render_template('auth/login.html')


@auth.route('/logout')
def logout():
    session.clear()
    return render_template('auth/login.html')
