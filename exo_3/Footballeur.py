from Foot import Foot
from Sportif import Sportif

class Footballeur(Foot, Sportif):

    def __init__(self, name = "Nom", age = 18):
        self._name = name
        self._age = age
    
    def name(self):
        print(f"""My name is {self._name}""")

    def age(self):
        print(f"""I am {self._age} years old""")
    
    def sport(self):
        print(f"""I play football""")


    def celebre(self):
        print(f"""{self._name} célèbre son action""")