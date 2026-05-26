import random

userNums = []       # 사용자가 입력한 숫자 저장
randNums = []       # 랜덤으로 입력한 숫자 저장
collect = []        # 사용자가 맞춘 숫자 저장

def setUNumbers(ns):    # setter set + UNumbers
    global userNums
    userNums = ns

def getUNumbers():      # getter get + UNumbers
    return userNums

def setRNumbers():
    global randNums
    randNums =random.sample(range(1, 46), 6)

def getRNumbers():
    return randNums

def compareNumbers():
    global userNums
    global randNums
    global collect

    collect = []
    for item in userNums:
        if randNums.count(item) != 0:
            collect.append(item)

    return collect