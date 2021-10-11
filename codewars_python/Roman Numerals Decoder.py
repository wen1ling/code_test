"""
问题描述
https://www.codewars.com/kata/51b6249c4612257ac0000005
"""


# !/usr/bin/python
# -*- coding: UTF-8 -*-

def solution(roman):
    result = 0
    for i in range(0, len(roman)):
        # 依次判断罗马字符
        if roman[i] == 'M':
            result += 1000
        elif roman[i:i + 2] == 'CM' or roman[i:i + 2] == 'CD':
            # CM/CD比较特殊，分别为900和400，通过-100方式可以避免重复运算
            result += -100
        elif roman[i] == 'D':
            result += 500
        elif roman[i] == 'C':
            result += 100
        elif roman[i:i + 2] == 'XC' or roman[i:i + 2] == 'XL':
            # 如上
            result += -10
        elif roman[i] == 'L':
            result += 50
        elif roman[i] == 'X':
            result += 10
        elif roman[i:i + 2] == 'IV' or roman[i:i + 2] == 'IX':
            # 如上
            result += -1
        elif roman[i] == 'V':
            result += 5
        elif roman[i] == 'I':
            result += 1
        else:
            pass
    return result


print(solution('XIX'))
