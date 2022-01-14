import time

class Robot():

    def __init__(self, name):
        if name:
            self.__name = name
        else :
            self.__name = "<unnamed>"
        self.__state = False
        self.__battery = 0

    #renommage du robot s'il n'a pas été nommé à sa création
    def rename(self, name):
        if self.__name == "<unnamed>":
            self.__name = name
        else:
            print(f"""{self.__name} can't change his name""")

    #allumage robot
    def power_on(self):
        if self.__state:
            print(f"""{self.__name} is already ON""")
        else :
            self.__state = True
            print(f"""{self.__name} ignition""")

    #extinction robot
    def shutdown(self):
        if self.__state:
            self.__state = False
            print("See ya later")
        else:
            print(f"""{self.__name} is already OFF""")

    #mise en charge du robot
    def charge(self, battery_wanted = 100):
        max_charge_time = 10
        self.__charge_connection = True
        print(f"""{self.__name} in charge""")
        now = int(time.time())
        while self.__battery < battery_wanted and int(time.time()) < now + max_charge_time:
            print(f"""{self.__battery} %""")                                        #problème : la charge doit se faire entièrement
            self.__battery +=1
            time.sleep(0.09)
        if self.__battery == 100:
            print(f"""{self.__name} is fully charged""")
        else : 
            print(f"""{self.__name} is {self.__battery}% charged""")

    

