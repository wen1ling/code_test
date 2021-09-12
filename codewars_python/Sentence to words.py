"""
问题描述
https://www.codewars.com/kata/57a05e0172292dd8510001f7
"""


# !/usr/bin/python
# -*- coding: UTF-8 -*-


def splitSentence(s):
    word = ""
    j = 0
    origin = []
    for i in range(0, len(s)):
        word += s[i]
        if word[i] == " ":
            origin.append(str(s[j:i]))
            j = i + 1
        if i == len(s) - 1:
            origin.append(str(s[j:i + 1]))
    return origin
