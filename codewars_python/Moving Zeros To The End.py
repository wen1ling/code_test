"""
问题描述
https://www.codewars.com/kata/52597aa56021e91c93000cb0
"""


# !/usr/bin/python
# -*- coding: UTF-8 -*-

def move_zeros(array):
    # 通过新建一个列表进行改写
    new_array = []
    k = 0
    for i in range(0, len(array)):
        if array[i] != 0:
            new_array.append(array[i])
        elif array[i] == 0:
            k = k + 1
        else:
            pass
    for i in range(0, k):
        new_array.append(0)
    return new_array