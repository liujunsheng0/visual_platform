#!/usr/bin/python3
# -*- coding: utf-8 -*-


from . import main
from .table import Table, BootstrapTable


@main.route('/test/base_table', methods=['GET', 'POST'])
def test_base_table():
    t = Table('table name', ['a', 'b'], [[1, 2], [3, 4]])
    return t.render_template()


@main.route('/test/bootstrap_table', methods=['GET', 'POST'])
def test_bootstrap_table():
    columns = [{'field': 'a', 'title': 'A'}, {'field': 'b', 'title': 'B'}]
    data = [{'a': 1, 'b': 2}, {'a': 3, 'b': 4}]
    return BootstrapTable('bootstrap table name', columns, data).render_template()
