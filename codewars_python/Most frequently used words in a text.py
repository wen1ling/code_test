"""
问题描述
https://www.codewars.com/kata/51e056fe544cf36c410000fb
"""

# !/usr/bin/python
# -*- coding: UTF-8 -*-

import re


def top_3_words(text):
    list_base = re.findall(r'[\'a-zA-Z]+', text)
    list_base_key = []
    list_base_value = []
    for i in range(0, len(list_base)):
        list_base[i] = list_base[i].lower()
        if not re.match(r'[\']?[a-zA-Z]+', list_base[i]):
            pass
        elif list_base[i] not in list_base_key:
            list_base_value.append(1)
            list_base_key.append(list_base[i])
        elif list_base[i] in list_base_key:
            list_base_value[list_base_key.index(list_base[i])] += 1
    result = []
    if len(list_base_key) >= 1:
        max_first = max(list_base_value)
        result.append(list_base_key[list_base_value.index(max_first)])
        if len(list_base_key) >= 2:
            list_base_key.remove(list_base_key[list_base_value.index(max_first)])
            list_base_value.remove(max_first)
            max_second = max(list_base_value)
            result.append(list_base_key[list_base_value.index(max_second)])
            if len(list_base_key) >= 2:
                list_base_key.remove(list_base_key[list_base_value.index(max_second)])
                list_base_value.remove(max_second)
                max_third = max(list_base_value)
                result.append(list_base_key[list_base_value.index(max_third)])
    return result
