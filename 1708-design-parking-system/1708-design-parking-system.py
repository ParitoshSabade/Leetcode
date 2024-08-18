class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.bigSpace = big
        self.mediumSpace = medium
        self.smallSpace = small

    def addCar(self, carType: int) -> bool:
        if carType == 1:
            if self.bigSpace > 0:
                self.bigSpace -= 1
                return True
            else:
                return False
        elif carType == 2:
            if self.mediumSpace > 0:
                self.mediumSpace -= 1
                return True
            else:
                return False
        else:
            if self.smallSpace > 0:
                self.smallSpace -= 1
                return True
            else:
                return False




# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)