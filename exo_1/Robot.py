import time

class Robot():

    def __init__(self, name):
        if name:
            self.__name = name
        else :
            self.__name = "<unnamed>"
        self.__state = False

    #allumage robot
    def power_on(self):
        if self.__state:
            print("Robot already ON")
        else :
            self.__state = True
            print("Robot ignition")
    

