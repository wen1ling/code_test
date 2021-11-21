"""
问题描述
https://www.codewars.com/kata/58905bfa1decb981da00009e
"""


# !/usr/bin/python
# -*- coding: UTF-8 -*-

class Dinglemouse(object):
    queue_people = []
    queue_k = []
    queue = ()
    lift_max = 0
    now_people = []
    Lift_floor = []
    Lift_result = []
    result_e = []

    def del_dup(self, get):
        if get[0] != 0:
            get = [0] + get
        if get[-1] != 0:
            get.append(0)
        return_value = []
        return_value.append(get[0])
        for i in get:
            if return_value[-1] != i:
                return_value.append(i)
        return return_value

    def __init__(self, queues, capacity):
        Dinglemouse.queue = queues
        Dinglemouse.queue_people = []
        Dinglemouse.lift_max = capacity
        for i in range(0, len(queues)):
            Dinglemouse.queue_people.append(list(queues[i]))
            Dinglemouse.queue_k.append(list())

    def theLift(self):
        while not [x for a in Dinglemouse.queue_people for x in a] == []:
            Dinglemouse.Lift_on(self)
        else:
            result = Dinglemouse.result_e
            Dinglemouse.result_e = []
            if result == []:
                result = [0]
            result = Dinglemouse.del_dup(self, result)
            return result

    def Lift_on(self):
        # queue_k获取电梯一次上升未承载的人群
        for i in range(0, len(Dinglemouse.queue_people)):
            Dinglemouse.queue_k.append(list())
        # 对电梯内上升的人群依次读取
        for floor in range(0, len(Dinglemouse.queue_people)):
            # 去除已经到达某层后下电梯的人群
            if floor in Dinglemouse.now_people:
                Dinglemouse.now_people = [x for x in Dinglemouse.now_people if x != floor]
                # 因为下车了，电梯会停在某层，所以Life_floor要添加
                Dinglemouse.Lift_floor.append(floor)
            for people in range(0, len(Dinglemouse.queue_people[floor])):
                # 当有上升人群出现后且电梯未达负载时，now_people记录当前人群，Lift_floor记录当前电梯停留层数和要上升的层数
                if Dinglemouse.queue_people[floor][people] > floor and len(
                        Dinglemouse.now_people) < Dinglemouse.lift_max:
                    Dinglemouse.now_people.append(Dinglemouse.queue_people[floor][people])
                    Dinglemouse.Lift_floor.append(Dinglemouse.queue_people[floor][people])
                    Dinglemouse.Lift_floor.append(floor)
                # 当有上升人群但电梯已达负载时，电梯会停留，当人群不能进入电梯，queue_k记录当前层未上电梯的人员
                elif Dinglemouse.queue_people[floor][people] > floor and len(
                        Dinglemouse.now_people) >= Dinglemouse.lift_max:
                    Dinglemouse.Lift_floor.append(floor)
                    Dinglemouse.queue_k[floor].append(Dinglemouse.queue_people[floor][people])
                else:
                    pass
        # 用c得到单次电梯上升时的电梯停留的层数
        c = list(set(Dinglemouse.Lift_floor))
        c.sort()
        Dinglemouse.Lift_result += c
        # 清零
        Dinglemouse.now_people = []
        Dinglemouse.Lift_floor = []
        # 对电梯内下降的人群依次读取
        for floor in range(len(Dinglemouse.queue_people) - 1, -1, -1):
            # 去除已经到达某层后下电梯的人群
            if floor in Dinglemouse.now_people:
                Dinglemouse.now_people = [x for x in Dinglemouse.now_people if x != floor]
                # 因为下车了，电梯会停在某层，所以Life_floor要添加
                Dinglemouse.Lift_floor.append(floor)
            for people in range(0, len(Dinglemouse.queue_people[floor])):
                # 当有下降人群出现后且电梯未达负载时，now_people记录当前人群，Lift_floor记录当前电梯停留层数和要下降的层数
                if Dinglemouse.queue_people[floor][people] < floor and len(
                        Dinglemouse.now_people) < Dinglemouse.lift_max:
                    Dinglemouse.now_people.append(Dinglemouse.queue_people[floor][people])
                    Dinglemouse.Lift_floor.append(Dinglemouse.queue_people[floor][people])
                    Dinglemouse.Lift_floor.append(floor)
                # 当有下降人群但电梯已达负载时，电梯会停留，当人群不能进入电梯，queue_k记录当前层未上电梯的人员
                elif Dinglemouse.queue_people[floor][people] < floor and len(
                        Dinglemouse.now_people) >= Dinglemouse.lift_max:
                    Dinglemouse.Lift_floor.append(floor)
                    Dinglemouse.queue_k[floor].append(Dinglemouse.queue_people[floor][people])
        # 用c得到单次电梯下降时的电梯停留的层数
        d = list(set(Dinglemouse.Lift_floor))
        d.sort(reverse=True)
        Dinglemouse.Lift_result += d
        Dinglemouse.queue_people = Dinglemouse.queue_k
        # 清零
        Dinglemouse.queue_k = []
        Dinglemouse.Lift_floor = []
        result = Dinglemouse.Lift_result
        Dinglemouse.Lift_result = []
        Dinglemouse.result_e += result
        Dinglemouse.now_people = []