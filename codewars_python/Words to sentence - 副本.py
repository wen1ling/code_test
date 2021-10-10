"""
问题描述
https://www.codewars.com/kata/57a06005cf1fa5fbd5000216
"""


# !/usr/bin/python
# -*- coding: UTF-8 -*-

def words_to_sentence(words):
    strings = ""
    for i in range(0, len(words)):
        strings = strings + words[i] + " "
        # 通过循环进行叠加字符串
        if i == len(words) - 1:
            strings = strings[:-1]
        # 去除最后的空格
    return strings


print(words_to_sentence(["hello", "world", "abc", "bcd"]))
