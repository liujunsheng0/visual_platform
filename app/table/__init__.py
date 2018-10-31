#!/usr/bin/python3
# -*- coding: utf-8 -*-


from flask import Blueprint

main = Blueprint('table', __name__)

from . import test_views
