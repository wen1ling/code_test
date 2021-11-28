"""
问题链接
https://www.codewars.com/kata/514b92a657cdc65150000006
"""


# !/usr/bin/python
# -*- coding: UTF-8 -*-


def solution(number):
    three_number = 0
    five_number = 0
    result = 0
    if not isinstance(number, int):
        result = "error!!!"
    elif 3 < number <= 5:
        result = 3
    elif number <= 3:
        result = 0
    elif number > 5:
        for i in range(3, number, 3):
            three_number += i
        for j in range(5, number, 5):
            if j not in range(3, number, 3):
                five_number += j
        result = three_number + five_number
    return result


print(solution(99))