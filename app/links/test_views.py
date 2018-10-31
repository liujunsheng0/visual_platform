#!/usr/bin/python3
# -*- coding: utf-8 -*-

from flask import render_template as template

from . import main, render_template


@main.route('/test/baidu')
def test_baidu():
    return render_template("https://www.baidu.com")
