from 电梯图形界面 import *
from 状态集 import *

if __name__ == '__main__':
    root = tk.Tk()
    root.title('电梯模拟器')
    num_elevators = 5
    num_floors = 18  # Change this to the number of floors you need
    电梯状态 = 状态集(m=num_floors, n=num_elevators)
    # 状态.设置状态集(n=num_elevators, m=num_floors)
    elevator_gui = ElevatorGUI(root, num_elevators, num_floors, 电梯状态)
    root.mainloop()
