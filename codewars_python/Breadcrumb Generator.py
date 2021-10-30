"""
问题描述
https://www.codewars.com/kata/563fbac924106b8bf7000046
"""

# !/usr/bin/python
# -*- coding: UTF-8 -*-


# !/usr/bin/python
# -*- coding: UTF-8 -*-

import re
import copy


def generate_bc(url, separator):
    # abbr_str为后续缩减所用字符
    abbr_str = ["the", "of", "in", "from", "by", "with", "and", "or", "for", "to", "at", "a"]
    # 使用正则从url里面提取出各组成部分
    re_exp = re.match(r'([\w]+://)?([^/]*)([^.?#]+)?(.*)', url)
    # re_exp.group(1)为链接协议方法，如https://
    # re_exp.group(2)为www和域名在内的部分
    str_home = re_exp.group(2)
    # re_exp.group(3)为链接的目录部分，用findall将其分为列表便于后续使用
    str_href = []
    if re_exp.group(3):
        str_href = re.findall(r'[^/]+', re_exp.group(3))
    # re_exp.group(4)为尾端
    # 最后输出部分
    str = ''

    # 去除index类型的目录
    if len(str_href) >= 1 and str_href[-1] == 'index':
        str_href.pop()
    str_href_link = copy.copy(str_href)
    # 由于链接和输出的href名称不同，因此新建一个存储
    for i in range(1, len(str_href)):
        str_href_link[i] = str_href_link[i - 1] + '/' + str_href_link[i]
    # 字符串缩减
    for j in range(0, len(str_href)):
        if len(str_href[j]) > 30:
            str_href_exp = re.findall(r'[\w]+', str_href[j])
            str_href[j] = ""
            for k in range(0, len(str_href_exp)):
                print(k, str_href_exp[k])
                if str_href_exp[k] in abbr_str:
                    pass
                else:
                    str_href[j] += "".join(str_href_exp[k][0])
        elif len(str_href[j]) >= 0:
            str_href[j] = re.sub(r'-', " ", str_href[j])

    # 输出最后的流
    if str_home != '' and str_href != []:
        str = '<a href="/">HOME</a>'
        if str_href and len(str_href) >= 2:
            for i in range(0, len(str_href) - 1):
                str += separator + '<a href="/' + str_href_link[i] + '/">' + str_href[i].upper() + '</a>'
    # 官方设定，如果仅有网址无href的话，输出span类型的HOME
    elif str_href == []:
        str = '<span class="active">HOME</span>'

    # span与a、href标签不同，单独输出
    if len(str_href) >= 1:
        str += separator + '<span class="active">' + str_href[-1].upper() + '</span>'

    return str