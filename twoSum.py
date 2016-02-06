#-*- coding:utf-8 -*-

"""
Map的解法
注:enumerate函数,将list变成键对应值 eg:
enumerate(list) --> (0, list[0]), (1, list[1]), ...
"""
def twoSum(num, target):
    dictMap = {}
    for index, value in enumerate(num):
        if target - value in dictMap:
            return dictMap[target - value] + 1, index + 1
        dictMap[value] = index


list = [0, 4, 3, 0]

print(twoSum(list, 0))