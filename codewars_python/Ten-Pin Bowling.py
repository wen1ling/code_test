"""
问题描述
https://www.codewars.com/kata/5531abe4855bcc8d1f00004c
"""


# !/usr/bin/python
# -*- coding: UTF-8 -*-

# 计算每局得到的分数（不包含加分）
# score默认调用的为字符串
def pin_score(score):
    score_sum = 0
    for i in range(0, len(score)):
        if score[i] == 'X':
            score_sum += 10
        elif score[i] == '/':
            print(score[0])
            score_sum += 10 - int(score[0])
            print("xxx")
        elif 0 <= int(score[i]) <= 9:
            score_sum += int(score[i])
        else:
            pass
    return score_sum


def bowling_score(frames):
    # pin表示局数
    pin = 1
    # list_frames为字符串转化为列表
    list_frames = frames.split()
    result = 0
    # 计算基础分数
    for i in range(0, len(list_frames)):
        result += pin_score(list_frames[i])
    # 计算加分
    for j in range(0, len(frames)):
        # 计算局数
        if frames[j] == " ":
            pin += 1
        # 当前九局有补中时加分
        if frames[j] == "/" and pin <= 9:
            result += pin_score(frames[j:].replace(" ", "")[1])
        # 当前九局有一次击中时加分
        elif frames[j] == "X" and pin <= 9:
            print(j, frames[j:])
            # 根据循环得到后续组成的字符串，然后去空格取值即为结果
            result += pin_score(frames[j:].replace(" ", "")[1:3])
        else:
            pass

    return result
