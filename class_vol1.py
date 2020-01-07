class Person:
    def getName(self):
        return self.name 
    def getAge(self):
        return self.age 

pr = Person()
pr.name = "尾花"
pr.age = 48
n = pr.getName()
a = pr.getAge()

print(n, "夏樹は", a, "歳です")
