#!/usr/bin/python
# -*- coding: UTF-8 -*-

import math


def cockroach_speed(s):
    if s >= 0:
        cm_sec = math.floor(s * math.pow(10, 5) / 3600)
        return cm_sec


print(cockroach_speed(0))
