from ..exo_1.Robot import Robot
from Humain import Humain

class Cyborg(Robot, Humain):
    
    def __init__(self, name, sexe):
        Robot.__init__(self, name)
        Humain.__init__(self, sexe)