"""
问题描述
https://www.codewars.com/kata/55f9bca8ecaa9eac7100004a
"""


# !/usr/bin/python
# -*- coding: UTF-8 -*-

def past(h, m, s):
    if 0 <= h <= 23 and 0 <= m <= 59 and 0 <= s <= 59:
        past_1 = ((h * 60 + m) * 60 + s) * 1000
        return past_1
    else:
        return 0


print(past(0, 2, 0))
