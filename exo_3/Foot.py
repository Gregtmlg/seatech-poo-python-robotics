from Sport import Sport

class Foot(Sport):

    def __init__(self):
        self.__ball = "Rond"
    
    def ball(self):
        print(f"""Ce sport se joue avec un ballon {self.__ball.lower()}""")

    def raquette_or_not(self):
        print(False)

    