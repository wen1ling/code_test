#!/usr/bin/python
# -*- coding: UTF-8 -*-

import math


def is_triangular(t):
    if t >= 0 and t == math.ceil(t):
        first_n = math.floor(math.sqrt(t * 2))
        end_n = math.ceil(math.sqrt(t * 2) - 1)
        a = t
        for i in (first_n, end_n + 1):
            tn = i * (i + 1) / 2
            if tn == t:
                a = True
                break
            else:
                a = False
        return a
    else:
        return print("error!")



print(is_triangular(1.9))