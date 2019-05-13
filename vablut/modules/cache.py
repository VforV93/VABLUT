# -*- coding: utf-8 -*-

from vablut.evaluate.base import INF
from collections import namedtuple, OrderedDict

Entry = namedtuple('Entry', 'move depth score state')

class Cache(object):
    EXACT = object()
    UPPERBOUND = object()
    LOWERBOUND = object()