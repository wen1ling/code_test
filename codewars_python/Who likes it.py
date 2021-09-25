"""
问题描述
https://www.codewars.com/kata/5266876b8f4bf2da9b000362
"""


# !/usr/bin/python
# -*- coding: UTF-8 -*-


def likes(names):
    likes_result = ""
    if len(names) == 0:
        likes_result = "no one likes this"
    elif len(names) == 1:
        likes_result = names[0] + " likes this"
    elif len(names) == 2:
        likes_result = names[0] + " and " + names[1] + " like this"
    elif len(names) == 3:
        likes_result = names[0] + ", " + names[1] + " and " + names[2] + " like this"
    elif len(names) >= 4:
        likes_result = names[0] + ", " + names[1] + " and " + str(len(names) - 2) + " others like this"
    return likes_result


print(likes(["A", "Bb", "Ccc"]))
