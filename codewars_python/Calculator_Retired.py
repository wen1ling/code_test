# 在我写完这个解法时候，codewars已经把这个题目retired了，也就是下架了，题目链接是https://www.codewars.com/kata/5235c913397cbf2508000048

# !/usr/bin/python
# -*- coding: UTF-8 -*-
import re


class Calculator():
    def __init__(self):
        self.result = 0

    def evaluate(self, string):
        if string.count('(') == string.count(')'):
            string = re.sub(r' ', '', string)
            Calculator.result = Calculator.step(self, string)
        return Calculator.result

    def step(self, str_cal):
        print("self", str_cal)
        if re.search(r'[0-9.]+[*,/][0-9.]+', str_cal):
            step_cal = re.search(r'[0-9.]+[*,/][0-9.]+', str_cal)
            step_cal_result = Calculator.basic_calc_str(self, step_cal.group(0))
            str_cal = re.sub(r'[0-9.]+[*,/][0-9.]+', step_cal_result, str_cal, count=1)
        elif re.search(r'[0-9.]+[+-][0-9.]+', str_cal):
            step_cal = re.search(r'[0-9.]+[+-][0-9.]+', str_cal)
            step_cal_result = Calculator.basic_calc_str(self, step_cal.group(0))
            str_cal = re.sub(r'[0-9.]+[+-][0-9.]+', step_cal_result, str_cal, count=1)
        elif re.search(r'\([0-9.]+\)', str_cal):
            str_cal_num = re.search(r'\(([0-9.]+)\)', str_cal).groups()[0]
            print("qqq", str_cal, str_cal_num)
            str_cal = re.sub(r'[(][0-9.]+[)]', str_cal_num, str_cal)
            print("end", str_cal)
        else:
            pass
        if re.search(r'[(,)+,--*/]', str_cal):
            Calculator.step(self, str_cal)
        else:
            Calculator.result = str_cal
            print("nnn", str_cal)
        return Calculator.result

    def basic_calc_str(self, step_str):
        m = re.match(r'([0-9.]+)([+,--,*/]+)([0-9.]+)', step_str)
        first_num = float(m.group(1))
        calc_symbol = m.group(2)
        second_num = float(m.group(3))
        basic_result = 0
        if calc_symbol == '+':
            basic_result = first_num + second_num
        elif calc_symbol == '-':
            basic_result = first_num - second_num
        elif calc_symbol == '*':
            basic_result = first_num * second_num
        elif calc_symbol == '/':
            basic_result = first_num / second_num
        else:
            pass
        return str(basic_result)


print(Calculator().evaluate("1.1 * 2.2 * 3.3"))
