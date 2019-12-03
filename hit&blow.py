import random
print("hit & game" )
list_1 = list(range(1, 5))
r = random.sample(list_1, k=4)
bit = 0
while bit != 4:

    bit = 0
    pull = 0
    print(r)
    a_b= (input("数値を一文字づつ空白で入力してください").split())
    # 内包表記
    a = [int(c) for c in a_b] 


    for i in range(4):
        if r[i] == a[i]:
            bit += 1
            i += 1
        else:
            pull += 1
            i += 1
    print("hit", bit)
    print("blow", pull)
print("owari")