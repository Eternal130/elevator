import tkinter as tk
from functools import partial
from 事件集 import *


class ElevatorGUI:
    def __init__(self, root, num_elevators, num_floors, 状态集):
        self.root = root
        self.num_elevators = num_elevators
        self.num_floors = num_floors
        self.状态集 = 状态集

        # Create labels for elevator floors and door status
        self.elevator_labels = []
        for i in range(num_elevators):
            elevator_label = tk.Label(root, text=f'电梯 {i + 1}')
            elevator_label.grid(row=0, column=i + 1)
            self.elevator_labels.append(elevator_label)

        self.floor_labels = []
        for i in range(num_floors):
            floor_label = tk.Label(root, text=f'楼层 {i + 1}')
            floor_label.grid(row=num_floors - i, column=0)
            self.floor_labels.append(floor_label)

        # Create buttons for elevator and floor buttons
        self.elevator_buttons = []
        self.floor_buttons = []
        self.rooms = [[None for _ in range(num_elevators)] for _ in range(num_floors)]

        for i in range(num_elevators):
            for j in range(num_floors):
                room = tk.Label(root, text='🗄')
                room.grid(row=num_floors - j, column=i + 1)
                self.rooms[j][i] = room
        for i in range(num_elevators):
            self.rooms[0][i]['text'] = '●'

        TL = tk.Toplevel(root)
        TL.title('电梯内按钮')
        for i in range(num_elevators):
            elevator_buttons = []
            for j in range(num_floors):
                button = tk.Button(TL, text=f'EB {i + 1}-{j + 1}',
                                   command=partial(self.press_button, self.状态集, i, j, False))
                button.grid(row=num_floors - j, column=i + 1)
                elevator_buttons.append(button)
            self.elevator_buttons.append(elevator_buttons)

        for i in range(num_floors):
            floor_buttons = []
            for j in range(2):
                button = None
                if i == 0 and j == 0 or i == num_floors - 1 and j == 1:
                    button = tk.Button(root, text=f'FB {i + 1}' + ('上' if j > 0 else '下'), state=tk.DISABLED)
                else:
                    button = tk.Button(root, text=f'FB {i + 1}' + ('上' if j > 0 else '下'),
                                       command=partial(self.press_button, self.状态集, i, j, True))
                button.grid(row=num_floors - i, column=num_elevators + 1 + j)
                floor_buttons.append(button)
            self.floor_buttons.append(floor_buttons)

    def press_button(self, 电梯状态, i: int, j: int, isFloor: bool):
        if isFloor:
            FBP(电梯状态, j, i)
            # 当楼层j某个方向按钮状态为True时,高亮图形界面上的按钮
            if 电梯状态.FB[i][j]:
                self.floor_buttons[i][j].configure(relief=tk.SUNKEN)
            # else:
            #     self.floor_buttons[i][j].configure(relief=tk.RAISED)
            # print(f'FBP {i + 1} {j + 1}')
        else:
            # print(电梯状态.D[i])
            EBP(电梯状态, i, j)
            # 当电梯i内某个按钮状态为True时,修改图形界面上的按钮状态为亮起
            if 电梯状态.EB[j][i]:
                self.elevator_buttons[i][j].configure(relief=tk.SUNKEN)
            # else:
            #     self.elevator_buttons[i][j].configure(relief=tk.RAISED)
            # print(电梯状态.D[i])
            # print(f'EBP {i + 1} {j + 1}')

    def draw_room_label(self):
        # print('awa')
        # elevator_update(self.状态集)
        for i in range(self.num_elevators):
            for j in range(self.num_floors):
                if not self.状态集.EB[j][i]:
                    self.elevator_buttons[i][j].configure(relief=tk.RAISED)
                if not self.状态集.FB[j][0]:
                    self.floor_buttons[j][0].configure(relief=tk.RAISED)
                if not self.状态集.FB[j][1]:
                    self.floor_buttons[j][1].configure(relief=tk.RAISED)
                if self.状态集.EF[i] == j:
                    # 当电梯i当前楼层在其当前位置候选楼层时,显示●,如果电梯在当前楼层开门,显示○,否则显示▲或▼
                    if self.状态集.W[self.状态集.EF[i]][i] == 1:
                        self.rooms[j][i]['text'] = '○'
                    elif self.状态集.D[i] == -1:
                        self.rooms[j][i]['text'] = '●'
                    else:
                        self.rooms[j][i]['text'] = '▼' if self.状态集.D[i] == 0 else '▲'
                    # self.rooms[j][i]['text'] = '▼' if self.状态集.D[i] == 0 else '▲' if self.状态集.D[i] == 1 else '●' if self.状态集.W[self.状态集.EF[i]][i] == 0 else '○'
                    # self.rooms[j][i]['text'] = '○' if self.状态集.W[self.状态集.EF[i]][i] == 1 else '●' if self.状态集.EE[self.状态集.EF[i]][i] == 1 else '▼' if self.状态集.D[i] == 0 else '▲' if self.状态集.D[i] == -1 else '▲' if self.状态集.D[i] == 1 else '●'
                else:
                    self.rooms[j][i]['text'] = '🗄'
        elevator_update(self.状态集)
