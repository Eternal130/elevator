import 状态集


def V(状态集: 状态集, e: int, f: int):#电梯e是否停在f层
    return 状态集.S[e][f][0] or 状态集.S[e][f][1] or 状态集.W[e][f]


def S(状态集: 状态集, e: int, f: int, d: int):#电梯e停在f层且移动方向由d确认，0向下，1向上，-1待定
    if d == -1:
        return 状态集.S[e][f][0] or 状态集.S[e][f][1] or 状态集.W[e][f]
    return 状态集.S[e][f][d]

