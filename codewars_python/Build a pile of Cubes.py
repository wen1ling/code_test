"""
问题描述
https://www.codewars.com/kata/5592e3bd57b64d00f3000047
"""

# !/usr/bin/python
# -*- coding: UTF-8 -*-


import math


def find_nb(m):
    initial = -1
    initial_result = 0
    left_result = math.floor(pow(2 * m, 1 / 4))
    right_result = math.ceil(pow(8 * m, 1 / 4))
    for i in range(1, left_result):
        initial_result = initial_result + i * i * i
        # 降低计算量，先将基本的初始值得到
    print(initial_result, left_result)
    for j in range(left_result, right_result):
        # 估算n的范围
        initial_result = initial_result + j * j * j
        if initial_result == m:
            initial = j
            # 记录出现相等时j的值
        if initial != -1:
            break
    # 当出现正确的j值时退出循环，避免冗余计算
    return initial


print(find_nb(2187923905358930025))
