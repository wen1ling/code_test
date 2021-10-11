"""
问题描述
https://www.codewars.com/kata/55c04b4cc56a697bb0000048
"""


# !/usr/bin/python
# -*- coding: UTF-8 -*-

def scramble(s1, s2):
    boolean = True
    if len(s1) <= len(s2):
        a1 = s1
        a2 = s2
    else:
        a1 = s2
        a2 = s1
    # 比较大小，降低计算量
    for i in range(97, 123):
        if chr(i) in a1:
            # chr(i)和range(97, 123)为a-z
            boolean = chr(i) in a2
            # a1和a2是否共用字母
            if a1.count(chr(i)) > a2.count(chr(i)):
                boolean = False
                break
                # 当偏小的a1拥有某元素数量大于偏大的a2时，说明不匹配

    return boolean


print(scramble('cedewaraaossoqqyt', 'codewars'))
