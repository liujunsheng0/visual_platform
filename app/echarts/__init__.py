#!/usr/bin/python3
# -*- coding: utf-8 -*-

from flask import Blueprint

main = Blueprint('echarts', __name__)

from . import views
from . import test_views
