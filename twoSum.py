#-*- coding:utf-8 -*-


def twoSum(num, target):
    dictMap = {}
    for index, value in enumerate(num):
        if target - value in dictMap:
            return dictMap[target - value] + 1, index + 1
        dictMap[value] = index


list = [0, 4, 3, 0]

print(twoSum(list, 0))