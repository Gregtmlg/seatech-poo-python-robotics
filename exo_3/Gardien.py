from Footballeur import Footballeur


class Gardien(Footballeur):

    def __init__(self, name, age):
        Footballeur.__init__(self,name, age)

    def parade(self):
        print(f"""{self._name} fait une parade""")
    
    def degagement(self):
        print(f"""{self._name} dégage sons camp""")