#!/usr/bin/python3
# -*- coding: utf-8 -*-

from flask import render_template

"""
文档: http://www.echartsjs.com/option.html#tooltip.trigger
"""


class Echarts(object):
    def __init__(self, option: dict, div_size: tuple=('80%', '600px'), **kwargs):
        """
        :param option:
        :param div_size: html中 <div> 大小, len=2, 值可为百分制 / (int)px
        :param kwargs: option.update(kwargs)
        """
        if kwargs:
            option.update(kwargs)
        self.option = option
        self.div_size = div_size

    def render_template(self, title: str=''):
        return render_template('echarts/charts.html', option=self.option, title=title, size=self.div_size)
