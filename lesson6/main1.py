from itertools import cycle
import time


class TrafficLight():

    def __init__(self, run_cycles=3):
        self.__color = {"Red": 7, "Yellow": 2, "Green": 5}  # c версии 3.5 словари упроядочены поэтому проверка не нужна

    def running(self, run_cycles=3):
        i = 0
        for color in cycle(self.__color.keys()):
            if i >= run_cycles * len(self.__color.keys()):
                break
            print(f"Color of traffic light is {color} and cycle number is {i // len(self.__color.keys()) + 1}")
            for sec in range(self.__color[color], 0, -1):
                print(sec)
                time.sleep(1)
            i += 1


tr_1 = TrafficLight()
tr_1.running(2)
