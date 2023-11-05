import 状态集
from 谓词集 import *


def EBP(状态集: 状态集, e: int, f: int):  # 电梯e内f层按钮被按下
    if not 状态集.EB[e][f] and not V(状态集, e, f):
        状态集.EB[e][f] = True
        if 状态集.EF[e] < f:
            状态集.M[e][f][1] = True
        elif 状态集.EF[e] > f:
            状态集.M[e][f][0] = True


def EAF(状态集: 状态集, e: int, f: int):  # 电梯e到达f层
    if 状态集.EB[e][f]:
        状态集.EB[e][f] = False


def FBP(状态集: 状态集, d: int, f: int):  # f层向d方向按钮被按下
    # S(状态集，e, f, d)的或运算,e的范围为状态集中电梯的个数
    if not 状态集.FB[f][d] and not any([S(状态集, e, f, d) for e in range(len(状态集.S))]):
        状态集.FB[f][d] = True
        #让距离f层最近的且沿d方向可以到达f层的一台电梯开始运行,或者让处于等待状态的一台电梯向f层运行




def EAFF(状态集: 状态集, f: int):  # 有电梯到达f层
    for d in [0, 1]:
        if 状态集.FB[f][d] and any([S(状态集, e, f, d) for e in range(len(状态集.S))]):
            状态集.FB[f][d] = False


def DC(状态集: 状态集, e: int, f: int):  # 电梯e在楼层f关门
    if S(状态集, e, f, 0):
        状态集.M[e][f - 1][0] = True
    elif S(状态集, e, f, 1):
        状态集.M[e][f + 1][1] = True
    elif S(状态集, e, f, -1):
        状态集.W[e][f] = True


def ST(状态集: 状态集, e: int, f: int):  # 电梯e靠近f层时触发传感器，电梯控制器决定是否在当前楼层停下
    for d in [0, 1]:
        if 状态集.FB[d][f] or 状态集.EB[e][f]:  # 电梯e要在f层停下
            # 状态集.S[e][f][d] = True
            状态集.M[e][f][d] = False
            # 状态集.W[e][f] = False
            状态集.FB[d][f] = False
            状态集.EB[e][f] = False
            DC(状态集, e, f)
            return
        else:  # 电梯e不在f层停下
            状态集.M[e][f][d] = False
            状态集.M[e][f + 1 if d > 0 else f - 1][d] = True
            状态集.S[e][f][d] = False
            状态集.W[e][f] = False


def RL(状态集: 状态集, e: int, f: int, d: int, E: bool):#电梯或楼层按钮被按下，E为True表示按下的是电梯内按钮，否则按下的是楼层按钮
    if E:
        EBP(状态集, e, f)
        #如果电梯处于等待状态，且电梯内按钮被按下，则电梯开始运行
        if 状态集.W[e][f]:
            状态集.W[e][f] = False
            状态集.S[e][f][d] = True
            状态集.M[e][f][d] = True
    else:
        FBP(状态集, d, f)
