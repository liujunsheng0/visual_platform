#!/usr/bin/python3
# -*- coding: utf-8 -*-

from flask import Blueprint

main = Blueprint('test', __name__)

from . import views

