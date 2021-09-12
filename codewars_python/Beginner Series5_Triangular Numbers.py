"""
问题描述
https://www.codewars.com/kata/56d0a591c6c8b466ca00118b
"""


# !/usr/bin/python
# -*- coding: UTF-8 -*-

import math


def is_triangular(t):
    if t >= 0 and t == math.ceil(t):
        first_n = math.floor(math.sqrt(t * 2))
        end_n = math.ceil(math.sqrt(t * 2) - 1)
        # 离给出的点数可能存在的边长
        for i in (first_n, end_n + 1):
            tn = i * (i + 1) / 2
            if tn == t:
                a = True
                break
            else:
                a = False
        return a
    # 利用可能存在的边长区间根据公式与点数比较。
    # 用a赋值，便于返回并避免出现无return返回None的情况。
    else:
        return print("error!")


print(is_triangular(1.9))
