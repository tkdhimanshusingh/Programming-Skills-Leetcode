class ParkingSystem:

    def __init__(self, big, medium, small):
        self.spaces = {1: big, 2: medium, 3: small}

    def addCar(self, carType):
        self.spaces[carType] -= 1
        return self.spaces[carType] >= 0
        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)