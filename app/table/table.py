#!/usr/bin/python3
# -*- coding: utf-8 -*-

from flask import render_template


class Table(object):
    def __init__(self, name: str, head: list, rows: list):
        """
        html中基本的图表
        :param name: 表名
        :param head: 表头
        :param rows: 每一行的内容, [[], []...]
        """
        self.name = name
        self.head = head
        self.rows = rows
        length = len(head)
        for i in rows:
            if len(i) != length:
                raise Exception('len(row) != len(head)')

    def render_template(self):
        return render_template('table/base_table.html', tb=self)


class BootstrapTable(object):
    def __init__(self, name: str, columns: list, rows: list, page_size: int=50):
        """
        :param name: 表名
        :param columns: [dict, ], dict由 cls.factory_column生成
        :param rows: [dict, ]
        """
        self.name = name
        self.columns = columns
        self.rows = rows
        self.page_size = page_size

    @classmethod
    def factory_column(cls,
                       field: str,
                       title: str="",
                       align: str="center",
                       valign: str="middle",
                       sortable: bool=True,
                       order: str="asc",
                       visible: bool=True,
                       checkbox: bool=False,
                       ) -> dict:
        """
        生成bootstrap-table需要的列数据, 只是表中的其中一列
        :param field: The column field name.
        :param title: The column title name.
        :param align: Indicate how to align the column data. 'left', 'right', 'center' can be used.
        :param valign: Indicate how to align the cell data. 'top', 'middle', 'bottom' can be used.
        :param sortable: True to allow the column can be sorted.
        :param order: The default sort order, can only be 'asc' or 'desc'.
        :param visible: False to hide the columns item.
        :param checkbox: True to show a checkbox. The checkbox column has fixed width
        :return: dict;
        """
        if not title:
            title = field
        if order not in ('asc', 'desc'):
            raise ValueError("order should be asc/desc")
        if align not in ('left', 'right', 'center'):
            raise ValueError("align should be left/right/center")
        if valign not in ('top', 'middle', 'bottom'):
            raise ValueError("valign should be top/middle/bottom")
        col = locals()
        col.pop("cls")
        return col

    def render_template(self):
        data = {'data': self.rows, 'columns': self.columns, 'pageSize': self.page_size}
        return render_template('table/bootstrap_table.html', data=data, table_name=self.name)
