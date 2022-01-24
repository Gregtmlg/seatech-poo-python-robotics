import abc

class Sport(metaclass=abc.ABCMeta):

    @abc.abstractclassmethod
    def ball(self):
        """Give the shape of the ball"""
        pass

    #@abc.abstractclassmethod