"""
问题描述
https://www.codewars.com/kata/5629db57620258aa9d000014
"""


# !/usr/bin/python
# -*- coding: UTF-8 -*-


def mix(s1, s2):
    # 这步可以优化，基本就是为了获得两个字符串的字母和字母个数
    dict_s1 = {}
    dict_s2 = {}
    for j in s1:
        if ord(j) in range(97, 123):
            if j not in dict_s1.keys():
                dict_s1[j] = 1
            elif j in dict_s1.keys():
                dict_s1[j] += 1
            else:
                pass
        else:
            pass
    for k in s2:
        if ord(k) in range(97, 123):
            if k not in dict_s2.keys():
                dict_s2[k] = 1
            elif k in dict_s2.keys():
                dict_s2[k] += 1
            else:
                pass
        else:
            pass
    # list_all就是两个字符串含有的字母总和
    list_all = list(set(dict_s1.keys()) | set(dict_s2.keys()))
    # 用列表存储要输出的每一部分
    result = []
    for i in list_all:
        if s1.count(i) > s2.count(i) and s1.count(i) > 1:
            result.append("1:" + i * dict_s1[i] + "/")
        elif s1.count(i) < s2.count(i) and s2.count(i) > 1:
            result.append("2:" + i * dict_s2[i] + "/")
        elif s1.count(i) == s2.count(i) and s1.count(i) > 1:
            result.append("=:" + i * dict_s1[i] + "/")
        else:
            pass
    # sorted处理列表，得到排序后的完美列表
    result = sorted(result, key=lambda item: (-len(item), item))
    mix_result = ''
    # 将准备好的列表转化为字符串，去除末尾的/
    for i in range(0, len(result)):
        mix_result += result[i]
    return mix_result[:-1]


print(mix("Sadus:cpms>orqn3zecwGvnznSgacs", "MynwdKizfd$lvse+gnbaGydxyXzayp"))
