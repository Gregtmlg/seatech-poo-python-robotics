import time

class Robot():
    def __init__(self, name = None):
        if name:
            self.__name = name
        else :
            self.__name = "<unnamed>"
        self.__state = False

    #allumage robot
    def power_on(self):
        if self.__state:
            return """Robot already ON"""
        else :
            self.__state = True
            return """Robot ignition"""
    

