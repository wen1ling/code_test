#!/usr/bin/python
# -*- coding: UTF-8 -*-

def paperwork(n, m):
    if n >= 0 and m >= 0:
        past = n * m
        return past
    else:
        return 0


print(paperwork(-5, 5))
