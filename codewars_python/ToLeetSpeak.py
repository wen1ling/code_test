"""
问题描述
https://www.codewars.com/kata/57c1ab3949324c321600013f
"""

# !/usr/bin/python
# -*- coding: UTF-8 -*-


def to_leet_speak(str):
    end_str = ""
    leet_speak_tuple = ('@', 8, '(', 'D', 3, 'F', 6,
                        "#", "!", 'J', 'K', 1, 'M',
                        'N', '0', 'P', 'Q', 'R', '$',
                        7, 'U', 'V', 'W', 'X', 'Y', '2')
    # 建立leet_speak的的元组
    for i in range(0, len(str)):
        if 65 <= ord(str[i]) <= 90:
            # 字母为大写的进行转化
            a = leet_speak_tuple[ord(str[i]) - 65]
        else:
            # 非大写字母直接输出
            a = str[i]
        end_str += format(a)
    return end_str

print(to_leet_speak("REVFFV"))