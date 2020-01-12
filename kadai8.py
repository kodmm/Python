class Car:
    def __init__(self, capacity, gas):
        self._capacity = capacity
        self._gas = gas
        print("Car created")
    
    def setGas(self, gas):
        self.__gas = gas
        print("Refueling completed")
    
    def show(self):
        print("capacity is", self.__capacity)
        print("gas is", self.__gas)

class Track(Car):
    def __init__(self, capacity, gas):
        super().__init__(capacity, gas)
        self.__burden = 0
        print("track created")
    
    def addBurden(self, burden):
        self.__burden += burden
        print("積荷completed")
    
    def setGas(self, gas):
        self._gas = gas
        print("Refueling completed")

    def show(self):
        # super().show() __を使用した場合
        print("capacity is", self._capacity)
        print("gas is", self._gas)
        print("積荷 is", self.__burden)

trk = Track(6, 100)
trk.addBurden(200)
trk.setGas(50)
trk.show()


# super().show()