class Footballeur(Foot, Sportif):

    def __init__(self, name = "Nom", age = 18):
        self.__name = name
        self.__age = age
    
    def name(self):
        print(f"""My name is {self.__name}""")

    def age(self):
        print(f"""I am {self.__age} years old""")