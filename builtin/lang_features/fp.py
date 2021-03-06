# -*- coding: utf8 -*-
from __future__ import print_function


def loop(n, func):
    def inner(n):
        if n <= 0:
            return
        else:
            func(n)
            inner(n - 1)
    inner(n)


loop(10, lambda i: print('Hello World {0}.', i))
