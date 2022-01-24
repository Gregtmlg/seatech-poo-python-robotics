import abc

class Sportif(metaclass=abc.ABCMeta):

    @abc.abstractclassmethod
    def sport(self):
        """Give the sport of the player"""
        pass

    @abc.abstractclassmethod
    def name(self):
        """Give the name of the player"""
        pass

    @abc.abstractclassmethod
    def age(self):
        """Give the age of the player"""
        pass