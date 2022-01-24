import abc

class Sportif(metaclass=abc.ABCMeta):

    @abc.abstractclassmethod
    def sport(self):
        """Give the sport of the player"""
        pass

    #@abc.abstractclassmethod