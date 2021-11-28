"""
问题描述
https://www.codewars.com/kata/5208f99aee097e6552000148
"""


# !/usr/bin/python
# -*- coding: UTF-8 -*-


def solution(s):
    return_s = ""
    for i in range(0, len(s)):
        if ord(s[i]) < 65 or ord(s[i]) > 90:
            return_s = return_s + s[i]
        # 非大写字母正常添加
        else:
            return_s = return_s + " " + s[i]
        # 大写字母添加空格，记得添加原元素，否则会跳过。
    return return_s


print(solution("numberProblemPersonBigDaY"))
