class Person():
    count = 0
    # Person（クラス名）にするとpr2で呼び出されたときに変数値がresetされない。selfにすればresetされる。
    def __init__(self, name, age):
        Person.count = Person.count+ 1
        self.name = name
        self.age = age
    
    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age
    
    @classmethod
    def getCount(cls):
        return cls.count
# @classmethodからアクセスできるのは、count変数とグローバル変数のみ。
pr1 = Person("相澤", 50)
pr2 = Person("丹後", 50)

print(pr1.getName(), "さんは", pr1.getAge(), "歳です。")
print(pr2.getName(), "さんは", pr2.getAge(), "歳です。")
