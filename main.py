import threading
import time

from 电梯图形界面 import *
from 事件集 import *
from 状态集 import *

def update_gui():
    elevator_gui.draw_room_label()
    # print('bwb')
    timer = threading.Timer(2, update_gui)  # 每隔5秒执行一次update_gui函数
    timer.start()

if __name__ == '__main__':
    root = tk.Tk()
    root.title('电梯模拟器')
    num_elevators = 5
    num_floors = 10  # Change this to the number of floors you need
    电梯状态 = 状态集(m=num_floors, n=num_elevators)
    # 状态.设置状态集(n=num_elevators, m=num_floors)
    elevator_gui = ElevatorGUI(root, num_elevators, num_floors, 电梯状态)
    update_gui()
    root.mainloop()
    # while True:
    #     time.sleep(5)
    #     elevator_gui.draw_room_label()
    #     print('bwb')
    #     root.update()
