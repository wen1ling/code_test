"""
问题描述
https://www.codewars.com/kata/545cedaa9943f7fe7b000048
"""

# !/usr/bin/python
# -*- coding: UTF-8 -*-

import string


def is_pangram(s):
    s_end = sorted(s.lower(), reverse=True)
    # 转化为小写并翻转减少计算量
    c = True
    for i in range(0, len(string.ascii_lowercase)):
        # 调用string库小写字母变量进行循环
        if string.ascii_lowercase[i] not in s_end:
            c = False
            break
        # 当某一个字母没有在小写字母库内时退出循环
    return c
