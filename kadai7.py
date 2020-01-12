class Unit:
    
    def __init__(self, name, age, job, hp, power):
        self.__name = name #__name : privatevariable　__init__上では読み書きできるがほかは参照はできるが変更不可
        self.__age = age 
        self.__job = job 
        self.__hp = 100
        self.__power = power
        print("unit created")
    
    def show(self):
        return self.__name, self.__age, self.__job, self.__power, self.__hp
        # return self._age
        # return self._job
        # return self._power
        # return self._hp
    
uni = Unit("尾花", 47, "cooker", 50, 100)
uni2 = Unit("")
print(uni.show())

