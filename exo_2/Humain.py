import random as rd

class Humain():
    def __init__(self, name = '<unnamed>', sexe = '<No Gender>'):
        self.__name = name
        self.__sexe = sexe
        self.__good_food = []
        self.__bad_food = ['cailloux']

    def eat(self, aliment_list = ['cailloux']):
        for aliment in aliment_list:
            if aliment in self.__good_food:
                print(f"""{self.__name} aime bien cet aliment : {aliment}""")
            elif aliment in self.__bad_food:
                print(f"""{self.__name} n'aime pas cet aliment : {aliment}""")
            else:
                self.__like_or_not(aliment)

    def __like_or_not(self, aliment):
        choix = rd.randint(0,1)
        if choix == 1:
            self.__good_food.append(aliment)
            print(f"""{self.__name} aime bien cet aliment : {aliment}""")
        else : 
            self.__bad_food.append(aliment)
            print(f"""{self.__name} n'aime pas cet aliment : {aliment}""")