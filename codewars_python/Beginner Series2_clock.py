#!/usr/bin/python
# -*- coding: UTF-8 -*-

def past(h, m, s):
    if 0 <= h <= 23 and 0 <= m <= 59 and 0 <= s <= 59:
        past_1 = ((h * 60 + m) * 60 + s) * 1000
        print(past_1)
    else:
        print(0)
past(0, 0, 0)