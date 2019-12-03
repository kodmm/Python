import random


x = True
random_1 = random.randint(1,100)
print("[", random_1, "]")
while x == True:
    y = str(input("次に発生させる乱数は？\"high?\" low? oh high&low!"))
# エラー処理
    while (y not in ("h", "l")):
        y = str(input("次に発生させる乱数は？\"hight?\" low? oh high&low!"))
    random_2 = random.randint(1,100)
    print("[", random_2, "]")
    if y == 'h':
            if random_1 < random_2:
                print("pinpon")
                print("[", random_2, "]")
                random_1 = random_2
            else:
                    print("どんまい")
                    x = False
    elif y == 'l':
        if random_1 > random_2:
                print("pinpon")
                print("[", random_2, "]")
                random_1 = random_2
        else:
             print("どんまい")
             x = False









