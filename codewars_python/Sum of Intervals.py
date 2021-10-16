"""
问题描述
https://www.codewars.com/kata/52b7ed099cdc285c300001cd
"""


# !/usr/bin/python
# -*- coding: UTF-8 -*-

def sum_of_intervals(intervals):
    # result用来计数
    result = 0
    # result_list用来排除重复值
    result_list = []
    # 外列表循环
    for i in range(0, len(intervals)):
        # 列表内的列表循环
        for j in range(intervals[i][0], intervals[i][-1]):
            if j not in result_list:
                result_list.append(j)
                result += 1
    return result
