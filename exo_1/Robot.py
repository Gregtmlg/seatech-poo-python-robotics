import time

class Robot():

    def __init__(self, name):
        if name:
            self.__name = name
        else :
            self.__name = "<unnamed>"
        self.__state = False
        self.__battery = 100
        self.__speed = 0
        self.__max_speed = 100      #on limite la vitesse du robot
        self.__time_action = None       #variable de temps enregistrée au début de chaque action

    #renommage du robot s'il n'a pas été nommé à sa création
    def rename(self, name):
        if self.__name == "<unnamed>":
            self.__name = name
        else:
            print(f"""{self.__name} can't change his name""")

    #allumage robot
    def power_on(self):
        self.__time_action = time.time()
        if self.__state:
            print(f"""{self.__name} is already ON""")
        elif self.__battery == 0:
            print(f"""No Battery""")
        else :
            self.__state = True
            print(f"""{self.__name} ignition""")

    #extinction robot
    def shutdown(self):
        if self.__state:
            self.__state = False
            if self.__speed>0:
                self.stop()
            print("See ya later")
        else:
            print(f"""{self.__name} is already OFF""")

    #mise en charge du robot
    def charge(self, battery_wanted = 100):
        if self.__speed>0:
            self.stop()
        max_charge_time = 10
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

    
    #attribution d'une vitesse de déplacement
    def speed(self, value):
        self.__conso_batterie()
        self.__time_action = int(time.time())
        if self.__state:
            if value <= self.__max_speed:
                self.__speed = value
            else:
                self.__speed = self.__max_speed
        else:
            print(f"""{self.__name} is OFF and can't move""")

    def stop(self):
        self.__conso_batterie()
        self.__time_action = int(time.time())
        if self.__speed>0:
            self.__speed = 0
        else:
            print(f"""{self.__name} est déjà à l'arrêt""")
    
    def global_state(self):
        self.__conso_batterie()
        self.__time_action = time.time()
        if self.__state:
            etat = "ON"
        else:
            etat = "OFF"
        print(f"""###########
Name : {self.__name}
State : {etat}
Battery : {int(self.__battery)}%
Speed : {self.__speed}km/h
###########""")


    #méthode de calcul de la consommation de la batterie
    def __conso_batterie(self):
        now = int(time.time())
        if self.__state == True and self.__speed == 0:
            battery  = max(self.__battery - int(now - self.__time_action)*0.01, 0)
            self.__battery = int(battery)
        elif self.__state == True and self.__speed != 0:
            battery  = max(self.__battery - int(now - self.__time_action)*0.01*self.__speed, 0)
            self.__battery = int(battery)
    
    @property
    
    def get_speed(self):
        if self.__speed>0:
            print(f"""{self.__name} avance à {self.__speed}km/h""")
        else:
            print(f"""{self.__name} est à l'arrêt""")
        return self.__speed
        
