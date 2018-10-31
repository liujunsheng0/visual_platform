#!/usr/bin/python3
# -*- coding: utf-8 -*-

from . import main
from .echarts import Echarts
from .options import line_option, bar_option, scatter_option, pie_option


@main.route('/test/line')
def test_line():
    option = line_option([1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6])
    return Echarts(option).render_template(title='echarts line test')


@main.route('/test/lines')
def test_lines():
    option = line_option([{'name': 'a', 'data': [1, 2, 3, 4, 5, 6, 7]},
                          {'name': 'b', 'data': [8, 9, 10, 11, 12, 13, 14]}], [1, 2, 3, 4, 5, 6, 7],
                         x_axis_type='category')
    return Echarts(option).render_template(title='echarts lines test')


@main.route('/test/bar')
def test_bar():
    option = bar_option([1, 2, 3, 4], [1, 2, 3, 4])
    return Echarts(option).render_template(title='echarts bar test')


@main.route('/test/scatter')
def test_scatter():
    option = scatter_option([1, 2, 3, 4], [1, 2, 3, 4])
    return Echarts(option).render_template(title='echarts scatter test')


@main.route('/test/pie')
def test_pie():
    option = pie_option([{'name': 'a', 'value': 1}, {'name': 'b', 'value': 2}])
    return Echarts(option).render_template(title='echarts pie test')

