class Person:
    def getName(self):
        return self.name 
    
    def getAge(self):
        return self.age 

pr1 = Person()
pr1.name = "平子"
pr1.age = 23

n1 = pr1.getName()
a1 = pr1.getAge()

pr2 = Person()
pr2.name = "京野"
pr2.age = 50
n2 = pr2.getName()
a2 = pr2.getAge()

print(n1, "さんは", a1, "歳です。")
print(n2, "さんは", a2, "歳です。")

