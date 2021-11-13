"""
问题描述
https://www.codewars.com/kata/51fda2d95d6efda45e00004e
"""

# !/usr/bin/python
# -*- coding: UTF-8 -*-

import math


class User:
    # 等级范围
    rank_range = [-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8]
    # 每级升级需要的分数
    rank_progress = 100

    # 定义初始值
    def __init__(self):
        self.rank = -8
        self.progress = 0

    # 挑战题目的情况
    def inc_progress(self, new_core):
        # 输入的题目必须在等级范围内
        if new_core in self.rank_range:
            # d为完成的题目等级与自身等级差
            d = self.rank_range.index(new_core) - self.rank_range.index(self.rank)
            # 不同题目等级完成后的得分情况
            if d == 0:
                self.progress += 3
            elif d == -1:
                self.progress += 1
            elif d < -1:
                pass
            elif d > 0:
                self.progress += 10 * d * d
            else:
                pass
            # 当等级达到最高级时，不再增加等级，且progress进度为0
            if self.rank == self.rank_range[-1] and self.progress != 0:
                User.rank_top(self)
        # 如果题目等级不在等级范围内，报错
        else:
            raise False
        # 当progress进度大于每级升级需要的分数时，且自身等级小于等于最高级时，调用rank_new函数进行升级
        if self.progress >= self.rank_progress and self.rank <= self.rank_range[-1]:
            User.rank_new(self, self.progress)

    # 升级函数
    def rank_new(self, progress):
        # 可升级的值
        rank_add = math.floor(progress / 100)
        # 自身等级加上升级值在等级的索引位置
        rank_result_range = self.rank_range.index(self.rank) + rank_add
        # 索引范围正常时，正常升级
        if rank_result_range in range(0, len(self.rank_range) - 1):
            self.rank = self.rank_range[rank_result_range]
            self.progress = progress - rank_add * 100
        # 当索引范围超过等级范围时（即获得的等级已经超出最高值），认定等级达到最高级，不再增加等级，且progress进度为0
        elif rank_result_range >= len(self.rank_range) - 1:
            User.rank_top(self)

    # 当等级达到最高级时，不再增加等级，且progress进度为0
    def rank_top(self):
        self.rank = self.rank_range[-1]
        self.progress = 0
