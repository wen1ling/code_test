#!/usr/bin/python
# -*- coding: UTF-8 -*-

def get_sum(a, b):
    s = 0
    if a < b:
        for i in range(a, b + 1):
            s += i
    elif a > b:
        for i in range(b, a + 1):
            s += i
    else:
        return a
    return s


print(get_sum(1, 3))
