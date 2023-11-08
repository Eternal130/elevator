import 状态集


def V(状态集: 状态集, e: int, f: int):#电梯e是否停在f层
    # return 状态集.S[0][f][e] or 状态集.S[1][f][e] or 状态集.W[f][e]
    return 状态集.EF[e] == f and 状态集.D[e] == -1


def S(状态集: 状态集, e: int, f: int, d: int):#电梯e停在f层且移动方向由d确认，0向下，1向上，-1待定
    if d == -1:
        return not (状态集.S[0][f][e] or 状态集.S[1][f][e])
    return 状态集.S[d][f][e]

