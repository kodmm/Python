x = int(input("好きな数字を入力してください："))

print(x)
if x % 15 == 0:
    print("FizzBuzz")
elif x % 3 == 0:
    print("Fizz")
elif x % 5 == 0:
    print("Buzz")
else:
    print('？？？？')
