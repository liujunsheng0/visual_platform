#!/usr/bin/python3
# -*- coding: utf-8 -*-

from flask import Blueprint
from flask import render_template as template

main = Blueprint('links', __name__)


def render_template(link_url: str):
    """
    :param link_url: 链接, 如: https://www.baidu.com
    :return: render_template
    """
    return template('base/link.html', link=link_url)


from . import test_views
