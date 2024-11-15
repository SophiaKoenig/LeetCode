class ParkingSystem(object):
    """
    Design a parking system for a parking lot. The parking lot has three kinds of parking spaces:
    big, medium, and small, with a fixed number of slots for each size.
    mplement the ParkingSystem class:

    ParkingSystem(int big, int medium, int small) Initializes object of the ParkingSystem class.
    The number of slots for each parking space are given as part of the constructor.
    bool addCar(int carType) Checks whether there is a parking space of carType
    for the car that wants to get into the parking lot.
    carType can be of three kinds: big, medium, or small,
    which are represented by 1, 2, and 3 respectively.
    A car can only park in a parking space of its carType.
    If there is no space available, return false,
    else park the car in that size space and return true.

    :type big: int
    :type medium: int
    :type small: int
    """

    def __init__(self, big, medium, small):
        self.big = big
        self.medium = medium
        self.small = small

    def get_big(self):
        return self.big

    def set_big(self, big):
        self.big = big

    def get_medium(self):
        return self.medium

    def set_medium(self, medium):
        self.medium = medium

    def get_small(self):
        return self.small

    def set_small(self, small):
        self.small = small

    def addCar(self, carType):
        if carType not in [1, 2, 3]:
            return None
        if carType == 1:
            big_spaces = self.get_big()
            if big_spaces >= 1:
                self.set_big(big_spaces - 1)
                return True
            else:
                return False

        if carType == 2:
            medium_spaces = self.get_medium()
            if medium_spaces >= 1:
                self.set_medium(medium_spaces - 1)
                return True
            else:
                return False
        if carType == 3:
            small_spaces = self.get_small()
            if small_spaces >= 1:
                self.set_small(small_spaces - 1)
                return True
            else:
                return False


