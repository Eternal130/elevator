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
                状态集.D[e] = 1
                # print(状态集.D[e])
            else:
                状态集.S[0][f][e] = True
                状态集.M[0][状态集.EF[e] - 1][e] = True
                状态集.EE[f][e] = True
                状态集.D[e] = 0


def EAF(状态集: 状态集, e: int, f: int):  # 电梯e到达f层
    if 状态集.EB[f][e]:
        状态集.EB[f][e] = False
        状态集.W[状态集.EF[e]][e] = 1
    # 状态集.EF[e] = f
    # 状态集.EF[e] = f
    # 状态集.M[0][f][e] = False
    # 状态集.M[1][f][e] = False
    # 如果电梯e在运行且f层的当前方向被按下，则将电梯e的当前路径候选楼层中的f层清空
    if 状态集.D[e] != -1 and 状态集.FB[f][状态集.D[e]]:
        状态集.FB[f][状态集.D[e]] = False
        状态集.EE[f][e] = False
        状态集.W[状态集.EF[e]][e] = 1
        print('c')
    # 否则如果电梯e在运行且f层的非当前方向被按下，并且f层是电梯当前运行路径的最后一层
    elif 状态集.D[e] != -1 and 状态集.FB[f][1 - 状态集.D[e]] and not any(
            [状态集.EE[i][e] for i in range(状态集.f) if (i > f if 状态集.D[e] == 1 else i < f)]):
        # #如果电梯e当前路径候选楼层只有f层,则将电梯e当前位置候选楼层清空
        # if not any([状态集.EE[i][e] for i in range(状态集.f) if i != f]):
        #     状态集.EE[f][e] = False
        #     print('a')
        # else:
        #     状态集.EE[f][e] = False
        #     状态集.EW[f][e] = True
        状态集.EE[f][e] = False
        # 状态集.EW[f][e] = True
        状态集.D[e] = 1 - 状态集.D[e]
        状态集.FB[状态集.EF[e]][状态集.D[e]] = False
        状态集.W[f][e] = 1
        # print(状态集.EE[f+1][e]+状态集.EE[f][e])
    elif 状态集.D[e] != -1 and 状态集.FB[f][1 - 状态集.D[e]]:
        状态集.EE[f][e] = False
        状态集.EW[f][e] = True
    elif 状态集.D[e] == -1:
        状态集.W[状态集.EF[e]][e] = 1
        状态集.EE[f][e] = False
    elif 状态集.D[e] != -1:
        状态集.EE[f][e] = False
        # 状态集.EW[f][e] = False
    # 如果电梯e的当前路径候选楼层为空，则将电梯e非当前路径候选楼层和电梯e当前路径候选楼层交换
    if not any(row[e] for row in 状态集.EE):
        for k in range(状态集.f):
            状态集.EE[k][e] = 状态集.EW[k][e]
            状态集.EW[k][e] = False
        if not any(row[e] for row in 状态集.EE):  # 如果交换后电梯e的当前路径候选楼层仍为空，则电梯在此处停止运行
            状态集.D[e] = -1
            状态集.W[f][e] = 1
            状态集.M[0][f][e] = False
            状态集.M[1][f][e] = False
            状态集.S[0][f][e] = False
            状态集.S[1][f][e] = False
            print('b')
        else:  # 根据电梯e当前所处楼层和电梯e当前路径候选楼层中与当前楼层最近的楼层确定电梯e的运行方向
            print('a')
            if 状态集.EF[e] < min([i for i in range(状态集.f) if 状态集.EE[i][e]]):
                状态集.D[e] = 1
            else:
                状态集.D[e] = 0
            状态集.FB[状态集.EF[e]][状态集.D[e]] = False
            # 电梯e的位置改为当前方向的下一个楼层
            # 状态集.EF[e] += 1 if 状态集.D[e] > 0 else -1
    else:
        状态集.S[状态集.D[e]][f][e] = True
        # 状态集.W[f][e] = 1
        状态集.FB[状态集.EF[e]][状态集.D[e]] = False
        # 状态集.EF[e] += 1 if 状态集.D[e] > 0 else -1
    if 状态集.D[e] != -1:
        状态集.FB[f][状态集.D[e]] = False
    else:
        状态集.FB[f][0] = False
        状态集.FB[f][1] = False


def FBP(状态集: 状态集, d: int, f: int):  # f层向d方向按钮被按下
    # S(状态集，e, f, d)的或运算,e的范围为状态集中电梯的个数
    if not 状态集.FB[f][d] and not any([状态集.EF[e] == f and 状态集.D[e] == d for e in range(状态集.e)]):
        状态集.FB[f][d] = True
        # 将当前正在运行且沿当前运行方向可以到达f层的电梯以及处于等待状态的电梯id加入到列表中
        e_list = []
        for i in range(状态集.e):
            if d == 1 and 状态集.EF[i] < f:
                e_list.append(i)
            elif d == 0 and 状态集.EF[i] > f:
                e_list.append(i)
            elif 状态集.D[i] == -1:
                e_list.append(i)
        # 如果e_list为空,将电梯0加入列表
        if len(e_list) == 0:
            状态集.EW[f][0] = True
        else:
            # 将e_list中的电梯按照当前楼层到达f层的距离从小到大排序
            e_list.sort(key=lambda x: abs(状态集.EF[x] - f))
            # 如果e_list[0]电梯运行方向与楼层按钮方向相同或者电梯处于闲置状态,则将e_list[0]电梯的当前路径候选楼层中加入f层
            if (状态集.EF[e_list[0]] > f) if 状态集.D[e_list[0]] == 0 else (状态集.EF[e_list[0]] < f) or 状态集.D[e_list[0]] == -1:
                # if 状态集.D[e_list[0]] == d or 状态集.D[e_list[0]] == -1:
                状态集.EE[f][e_list[0]] = True
                print('候选')
            else:  # 否则将e_list[0]电梯的非当前路径候选楼层中加入f层
                状态集.EW[f][e_list[0]] = True
                print('非候选')
            # 根据当前电梯的位置设置电梯方向
            if 状态集.EF[e_list[0]] < f:
                状态集.D[e_list[0]] = 1
            else:
                状态集.D[e_list[0]] = 0


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
        状态集.W[f][e] = 0


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
            状态集.W[f][e] = 0


def elevator_update(状态集: 状态集):
    for e in range(状态集.e):
        if 状态集.W[状态集.EF[e]][e] == 1:
            状态集.W[状态集.EF[e]][e] = 0
        else:
            if any(row[e] for row in 状态集.EE):
                状态集.EF[e] += 1 if 状态集.D[e] > 0 else -1 if 状态集.D[e] == 0 else 0
                if 状态集.EF[e] > 状态集.f - 1:
                    状态集.EF[e] = 状态集.f - 1
                elif 状态集.EF[e] < 0:
                    状态集.EF[e] = 0
                # if 状态集.EE[状态集.EF[e]][e]:
                    # 状态集.W[状态集.EF[e]][e] = 1
                EAF(状态集, e, 状态集.EF[e])
