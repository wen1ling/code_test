"""
问题描述
https://www.codewars.com/kata/51b66044bce5799a7f000003
"""


# !/usr/bin/python
# -*- coding: UTF-8 -*-

class RomanNumerals:
    # 罗马字母代表的值
    num_list = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    roman_list = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

    def from_roman(roman_num):
        result = 0
        # 对十进制数判断位数，依次进行循环
        for i in range(0, len(roman_num)):
            # 根据罗马字母的列表匹配后依次循环叠加
            for j in range(0, len(RomanNumerals.roman_list)):
                if roman_num[i] == RomanNumerals.roman_list[j]:
                    result += RomanNumerals.num_list[j]
                    # 由于不能避免的存在双字母，依次减去
                    if roman_num[i:i + 2] == "CM" or roman_num[i:i + 2] == "CD":
                        result -= 200
                    elif roman_num[i: i + 2] == "XC" or roman_num[i:i + 2] == "XL":
                        result -= 20
                    elif roman_num[i:i + 2] == "IX" or roman_num[i:i + 2] == "IV":
                        result -= 2
                    else:
                        pass
        return result

    def to_roman(val):
        result = ""
        # 当输入的十进制数为0后结束循环（此时result已经叠加完毕）
        while val != 0:
            # 由于列表和循环的特殊性，先对大于1000和等于1的进行排除
            if val >= RomanNumerals.num_list[0]:
                val -= RomanNumerals.num_list[0]
                result += "M"
            elif val == RomanNumerals.num_list[-1]:
                val -= 1
                result += "I"
            else:
                # 对于1-1000内的数值，与准备的十进制列表匹配，匹配成功后对result叠加罗马数字，并减去对应匹配的值
                for i in range(0, len(RomanNumerals.num_list) - 1):
                    if val in range(RomanNumerals.num_list[i + 1], RomanNumerals.num_list[i]):
                        val -= RomanNumerals.num_list[i + 1]
                        result += RomanNumerals.roman_list[i + 1]
                    else:
                        pass
        return result


print(RomanNumerals.to_roman(1020))
