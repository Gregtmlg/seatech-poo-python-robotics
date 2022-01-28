import abc

class Sport(metaclass=abc.ABCMeta):

    @abc.abstractclassmethod
    def ball(self):
        """Give the shape of the ball"""
        pass

    @abc.abstractclassmethod
    def raquette_or_not(self):
        """Says if the sport is played with raquette"""
        pass
    