#!/usr/bin/python3
# -*- coding: utf-8 -*-

_line_default_option = {
    'tooltip': {'trigger': 'axis'},
    'toolbox': {'show': 'true',
                'feature': {
                    'mark': {'show': 'true'},
                    'dataView': {'show': 'true', 'readOnly': 'false'},
                    'magicType': {'show': 'true', 'type': ['line', 'bar']},
                    'restore': {'show': 'true'},
                    'saveAsImage': {'show': 'true'}
                }
                },
    'calculable': 'true',
}

def line_option(series: list, x_axis: list, title: str='', x_name: str='x', y_name: str='y', legend: list=None,
                background_color: str='', x_axis_type: str='category'):
    """
    :param series: y轴数据, list
        一条线: [values1, value2...]
        多条线: [{'name': 'legend', 'data': list}, .....]
    :param x_axis: x轴坐标点
    :param title: 图的标题
    :param x_name: x轴名字
    :param y_name: y轴名字
    :param legend: 图标
    :param background_color: 背景颜色
    :param x_axis_type: category/value
    :return: dict
    """
    if x_axis_type not in ['category', 'value']:
        raise ValueError('x_axis_type error')
    xAxis = {'type': x_axis_type, 'data': x_axis, 'name': x_name, 'boundaryGap': 'false'}
    yAxis = {'type': 'value', 'name': y_name, 'axisLabel': {'formatter': '{value}'}}

    # 一个图中存在多条线
    if len(series) > 0 and isinstance(series[0], dict):
        for s in series:
            if isinstance(s, dict):
                s['type'] = 'line'
    else:
        series = [{'data': series, 'type': 'line', 'title': title,
                   'markPoint': {'data': [{'type': 'max', 'name': '最大值'}, {'type': 'min', 'name': '最小值'}]},
                   'markLine': {'data': [{'type': 'average', 'name': '平均值'}]}
                   }]
    option = {'xAxis': xAxis,
              'yAxis': yAxis,
              'series': series,
              'backgroundColor': background_color,
              }
    option.update(_line_default_option)
    if title:
        option['title'] = {'text': title, 'x': 'center'}
    if legend is None and len(series) > 0 and isinstance(series[0], dict):
        legend = [i.get('name') for i in series if isinstance(i, dict) and i.get('name')]
    if legend:
        option['legend'] = {'data': legend, 'y': 'top', 'x': 'left', 'orient': 'vertical'}
    return option

def bar_option(series: list, x_axis: list, title: str='', x_name: str='x', y_name: str='y',
               background_color: str=''):
    option = {'tooltip': {'trigger': 'axis'},
              'toolbox': {'show': 'true',
                          'feature': {'mark': {'show': 'true'},
                                      'dataView': {'show': 'true', 'readOnly': 'false'},
                                      'restore': {'show': 'true'},
                                      'magicType': {'show': 'true', 'type': ['line', 'bar']},
                                      'saveAsImage': {'show': 'true'}
                                      }
                          },
              'backgroundColor': background_color,
              'xAxis': {'name': x_name, 'data': x_axis},
              'yAxis': {'name': y_name},
              'series': [{'markPoint': {'data': [{'type': 'max', 'name': '最大值'},
                                                 {'type': 'min', 'name': '最小值'}]},
                          'markLine': {'data': [{'type': 'average', 'name': '平均值'}]},
                          'type': 'bar',
                          'data': series,
                          'title': title
                          }]
              }
    if title:
        option['title'] = {'text': title, 'x': 'center'}
    return option

def scatter_option(series: list, x_axis: list, title: str='', x_name: str='x', y_name: str='y',
                   background_color: str=''):
    option = bar_option(**locals())
    option['series'][0]['type'] = 'scatter'
    return option

def pie_option(series: list, title: str='', legend: list=None, radius: float=0.8, center: tuple=(0.5, 0.5)):
    """
    :param series: list, [{'name': name, 'value': value}....]
    :param title: 图的标题
    :param legend: 图标
    :param radius: 半径: 0~1
    :param center: 中心点坐标, (x, y) in 0~1
    :return: dict
    """
    radius = '%s' % (min(1, radius) * 100) + '%'
    center = ['%s' % (min(1, i) * 100) + '%' for i in center]
    option = {
        'tooltip': {'trigger': 'item', 'formatter': "{b}:{d}%"},
        'toolbox': {'show': 'true',
                    'feature': {
                        'mark': {'show': 'true'},
                        'dataView': {'show': 'true', 'readOnly': 'false'},
                        'restore': {'show': 'true'},
                        'saveAsImage': {'show': 'true'}
                    },
        },
        'calculable': 'true',
        'series': [{
            'title': title,
            'type': 'pie',
            'radius': radius,
            'center': center,
            'data': series,
        }, ]
    }
    if title:
        option['title'] = {'text': title, 'x': 'center'}

    if legend is None and len(series) > 0 and isinstance(series[0], dict):
        legend = [i.get('name') for i in series if isinstance(i, dict) and i.get('name')]
    if legend:
        option['legend'] = {'data': legend, 'y': 'top', 'x': 'left', 'orient': 'vertical'}

    return option
