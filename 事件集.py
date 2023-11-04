import 状态集
from 谓词集 import *


def EBP(状态集: 状态集, e: int, f: int):  # 电梯e内f层按钮被按下
    if not 状态集.EB[e][f] and not V(状态集, e, f):
        状态集.EB[e][f] = True


def EAF(状态集: 状态集, e: int, f: int):  # 电梯e到达f层
    if 状态集.EB[e][f]:
        状态集.EB[e][f] = False


def FBP(状态集: 状态集, d: int, f: int):  # f层向d方向按钮被按下
    # S(状态集，e, f, d)的或运算,e的范围为状态集中电梯的个数
    if not 状态集.FB[f][d] and not any([S(状态集, e, f, d) for e in range(len(状态集.S))]):
        状态集.FB[f][d] = True


def EAFF(状态集: 状态集, f: int):  # 有电梯到达f层
    for d in [0, 1]:
        if 状态集.FB[f][d] and any([S(状态集, e, f, d) for e in range(len(状态集.S))]):
            状态集.FB[f][d] = False
