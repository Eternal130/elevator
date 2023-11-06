import 状态集
from 谓词集 import *


def EBP(状态集: 状态集, e: int, f: int):  # 电梯e内f层按钮被按下
    if not 状态集.EB[f][e] and not V(状态集, e, f):
        状态集.EB[f][e] = True
        if 状态集.EF[e] < f and 状态集.D[e] == 1:
            状态集.S[1][f][e] = True
            状态集.M[1][状态集.EF[e] + 1][e] = True
            状态集.EE[f][e] = True
        elif 状态集.EF[e] < f and 状态集.D[e] == 0:
            状态集.S[0][f][e] = True
            状态集.M[0][状态集.EF[e] - 1][e] = True
            状态集.EW[f][e] = True
        elif 状态集.EF[e] > f and 状态集.D[e] == 1:
            状态集.S[1][f][e] = True
            状态集.M[1][状态集.EF[e] + 1][e] = True
            状态集.EW[f][e] = True
        elif 状态集.EF[e] > f and 状态集.D[e] == 0:
            状态集.S[0][f][e] = True
            状态集.M[0][状态集.EF[e] - 1][e] = True
            状态集.EE[f][e] = True
        elif 状态集.D[e] == -1:
            if 状态集.EF[e] < f:
                状态集.S[1][f][e] = True
                状态集.M[1][状态集.EF[e] + 1][e] = True
                状态集.EE[f][e] = True
            else:
                状态集.S[0][f][e] = True
                状态集.M[0][状态集.EF[e] - 1][e] = True
                状态集.EE[f][e] = True


def EAF(状态集: 状态集, e: int, f: int):  # 电梯e到达f层
    if 状态集.EB[f][e]:
        状态集.EB[f][e] = False
    # 电梯e的当前路径候选楼层和非当前路径候选楼层中删除f层
    状态集.EE[f][e] = False
    状态集.EW[f][e] = False


def FBP(状态集: 状态集, d: int, f: int):  # f层向d方向按钮被按下
    # S(状态集，e, f, d)的或运算,e的范围为状态集中电梯的个数
    if not 状态集.FB[f][d] and not any([S(状态集, e, f, d) for e in range(状态集.e)]):
        状态集.FB[f][d] = True
        # 将当前正在运行且沿当前运行方向可以到达f层的电梯以及处于等待状态的电梯id加入到列表中
        e_list = []
        for i in range(状态集.e):
            if d == 1 and 状态集.D[i] == d and 状态集.EF[i] < f:
                e_list.append(i)
            elif d == 0 and 状态集.D[i] == d and 状态集.EF[i] > f:
                e_list.append(i)
            elif 状态集.D[i] == -1:
                e_list.append(i)
        # 如果e_list为空,将电梯0加入列表
        if len(e_list) == 0:
            状态集.EW[f][0] = True
        else:
            # 将e_list中的电梯按照当前楼层到达f层的距离从小到大排序
            e_list.sort(key=lambda x: abs(状态集.EF[x] - f))
            # 向e_list[0]电梯的当前路径候选楼层添加f层
            状态集.EE[f][e_list[0]] = True


def EAFF(状态集: 状态集, f: int):  # 有电梯到达f层
    for d in [0, 1]:
        if 状态集.FB[f][d] and any([S(状态集, e, f, d) for e in range(状态集.e)]):
            状态集.FB[f][d] = False


def DC(状态集: 状态集, e: int, f: int):  # 电梯e在楼层f关门
    if S(状态集, e, f, 0):
        状态集.M[0][f - 1][e] = True
    elif S(状态集, e, f, 1):
        状态集.M[1][f + 1][e] = True
    elif S(状态集, e, f, -1):
        状态集.W[f][e] = True


def ST(状态集: 状态集, e: int, f: int):  # 电梯e靠近f层时触发传感器，电梯控制器决定是否在当前楼层停下
    for d in [0, 1]:
        if 状态集.FB[f][e] or 状态集.EB[f][e]:  # 电梯e要在f层停下
            # 状态集.S[e][f][d] = True
            状态集.M[d][f][e] = False
            # 状态集.W[e][f] = False
            状态集.FB[e][d] = False
            状态集.EB[f][e] = False
            DC(状态集, e, f)
            return
        else:  # 电梯e不在f层停下
            状态集.M[d][f][e] = False
            状态集.M[d][f + 1 if d > 0 else f - 1][e] = True
            状态集.S[d][f][e] = False
            状态集.W[f][e] = False


def elevator_update(状态集: 状态集):
    pass