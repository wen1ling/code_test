"""
问题描述
https://www.codewars.com/kata/52f677797c461daaf7000740
"""

# !/usr/bin/python
# -*- coding: UTF-8 -*-

# 虽然是四星题，但这个题本质考察数学能力，而非编程能力
# 本题目的在于求列表内最大公约数
import math


def solution(a):
    # 列表长度为1时直接返回
    if len(a) == 1:
        list_gcd = a[0]
    elif len(a) >= 2:
        # 列表长度大于等于2时求一下公约数
        list_gcd = math.gcd(a[0], a[1])
        # 列表大于2时开始循环，用两个数的公约数与下一个数不断循环求公约数
        if len(a) > 2:
            for i in a[2:]:
                list_gcd = math.gcd(list_gcd, i)
                # 当公约数为1时可以不必再进行比较，直接返回
                if list_gcd == 1:
                    break
    # 列表为0时返回0代表进程结束
    else:
        list_gcd = 0
    list_sum = len(a) * list_gcd
    return list_sum
