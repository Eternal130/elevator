class 状态集:

    def __init__(self):
        self.W = None
        self.S = None
        self.M = None
        self.FB = None
        self.EB = None
        self.EF = None

    def 设置状态集(self, m: int, n: int):
        # 电梯内按钮状态,默认均为False,False表示未按下,True表示按下,EB[i][j]为True表示电梯i内请求到j层的按钮亮起
        self.EB = [[False for _ in range(n)] for _ in range(m)]
        # 楼层按钮状态,默认均为False,False表示未按下,True表示按下,FB[i][j]为True表示j层请求电梯向i方向运动的按钮亮起.i的值为0或1,0表示向下,1表示向上
        self.FB = [[False for _ in range(2)] for _ in range(m)]
        # 电梯状态,默认均为False,False表示未运行,True表示运行,M[i][j][k]为True表示电梯i正沿k方向移动,即将到达第j层,k的值为0或1,0表示向下,1表示向上
        self.M = [[[False for _ in range(n)] for _ in range(m)] for _ in range(2)]
        # 电梯状态,默认均为False,False表示未运行,True表示运行,S[i][j][k]为True表示电梯i停在第j层，将朝k方向移动(尚未关门),k的值为0或1,0表示向下,1表示向上
        self.S = [[[False for _ in range(n)] for _ in range(m)] for _ in range(2)]
        # 电梯状态,默认均为False,False表示未运行,True表示运行,W[i][j]为True表示电梯i停在第j层等待(已关门)
        self.W = [[False for _ in range(n)] for _ in range(m)]
        # 电梯位置,默认均为0,EF[i]为0表示电梯i停在第0层
        self.EF = [0 for _ in range(n)]
