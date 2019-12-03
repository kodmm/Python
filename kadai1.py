# G019C1028 
# 俵積田 航成
import random
print('ようこそ占いの館へ')
name = str(input("あなたの名前を入力してください>"))
age = int(input("あなたの年齢を入力してください>"))
fortune = random.randint(1, 3)
fortune += 1
print("占いの結果が出ました！")
print(str(age) + "歳の" + name + "さん、あなたの運気番号は" + str(fortune) + "です。" )
print("1:大吉 2:中吉 3:吉4:凶")
print(age, "歳の", name, "さん、あなたの運気番号は" ,fortune, "です")

