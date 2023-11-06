import tkinter as tk
from 状态集 import 状态集


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
            floor_label.grid(row=i + 1, column=0)
            self.floor_labels.append(floor_label)

        # Create buttons for elevator and floor buttons
        self.elevator_buttons = []
        self.floor_buttons = []

        for i in range(num_elevators):
            for j in range(num_floors):
                tk.Label(root, text=0).grid(row=j + 1, column=i + 1)

        TL = tk.Toplevel(root)
        TL.title('电梯内按钮')
        for i in range(num_elevators):
            elevator_buttons = []
            for j in range(num_floors):
                button = tk.Button(TL, text=f'EB {i + 1}-{j + 1}')
                button.grid(row=j + num_floors + 1, column=i + 1)
                elevator_buttons.append(button)
            self.elevator_buttons.append(elevator_buttons)

        for i in range(num_floors):
            floor_buttons = []
            for j in range(2):
                button = None
                if i == 0 and j == 0 or i == num_floors - 1 and j == 1:
                    button = tk.Button(root, text=f'FB {i + 1}' + ('上' if j > 0 else '下'), state=tk.DISABLED)
                else:
                    button = tk.Button(root, text=f'FB {i + 1}' + ('上' if j > 0 else '下'))
                button.grid(row=i + 1, column=num_elevators + 1 + j)
                floor_buttons.append(button)
            self.floor_buttons.append(floor_buttons)

    def update_door_status(self, elevator_idx, is_open):
        pass  # Implement door status update as needed
