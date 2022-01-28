from Footballeur import Footballeur

class Attaquant(Footballeur):

    def __init__(self, name, age):
        Footballeur.__init__(self,name, age)

    def tacle(self):
        print(f"""{self._name} tacle son adversaire""")
    
    def tir(self):
        print(f"""{self._name} tir dans les cages adverses""")