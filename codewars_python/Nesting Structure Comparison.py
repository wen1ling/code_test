"""
问题描述
https://www.codewars.com/kata/520446778469526ec0000001
"""


# !/usr/bin/python
# -*- coding: UTF-8 -*-

# 第一string_to_list用于出现嵌套list时进行循环处理
def strings_to_list(original_list, other_list):
    result_list = True
    # 由于此字段不断循环时可能存在各自类型，所以保证两个均为列表且第二个列表不为零（避免第二个列表有int值后续的len()出现问题）
    if isinstance(other_list, list) and len(other_list) != 0:
        for j in range(0, len(original_list)):
            # 第一个仍未列表时继续循环
            if isinstance(original_list[j], list):
                result_list = strings_to_list(original_list[j], other_list[j])
            # 两个列表循环的值类型不同且长度不等可以返回False
            elif type(original_list[j]) != type(other_list[j]) or len(original_list) != len(other_list):
                result_list = False
                break
            # 前面排除掉了特殊情况，进入此循环的仅存在两个均为普通列表
            elif len(original_list) == len(other_list):
                result_list = True
            else:
                result_list = False
    # 两个列表均为空值时返回True
    elif original_list == [] and original_list == other_list:
        result_list = True
    else:
        result_list = False
    return result_list


def same_structure_as(original, other):
    # result为最后判断结果
    result = True
    # 仅两个均为列表且第一个为非零值才进行循环
    if isinstance(original, list) and isinstance(other, list) and len(original) != 0:
        # 以一个列表为基础进行循环
        for i in range(0, len(original)):
            # 列表进行循环时，如果存在某两个对应位置的值存在一个是列表但两者类型不同时为False
            if (isinstance(original[i], list) or isinstance(other[i], list)) and type(original[i]) != type(other[i]):
                result = False
                break
            # 列表出现嵌套循环时，调用string_to_list
            elif isinstance(original[i], list):
                result = strings_to_list(original[i], other[i])
            # 列表内长度相同时，且未存在嵌套循环时，返回True
            elif len(original) == len(other):
                result = True
            else:
                result = False
                break
    # 两个都为空集时直接返回
    elif original == [] and original == other:
        result = True
    else:
        result = False
    return result
