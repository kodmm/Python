# 文字を数値に変換
def toInt(c):
    idx = 0
    code  = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A","B", "C", "D", "E", "F"]
    
    while code[idx] != c:
        idx += 1
        return idx

def toStr(n):
     code  = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A","B", "C", "D", "E", "F"]

     return code[n]

def change(i, s):
    if s == 2:
        Binary_2 = bin(i)
        print("2進数値は"+ Binary_2 + "です。")
        return Binary_2
    elif s == 8:
        Octal_8 = oct(i)
        print("8進数値は" + Octal_8 + "です。")
        return Octal_8
    elif s == 16:
        Hexadecimal = hex(i)
        print("16進数値は" + Hexadecimal + "です。")
        return Hexadecimal
    else:
        print(i)
        return i

print(int('1010', 2))
input_value = str(input("数値 or 文字列を入力せよ:"))
print(input_value)
num = int(input("それは何進数？"))
input_number = int(input("何進数にしたいですか？:"))

Decimal_0 = int(input_value, num)
change(Decimal_0, input_number)


def radixConv(16, "FE", 7):
    tmp = "abcde"
    # frdx進数の数字　⇒　１０進数の数値
    # 10進数の数値⇒trdx進数数字
    return tmp

for i in range(len(fnum)):
    print(fnum[i])
    print(toInt(fnum[i]))
    val = val * frdx + toInt(fnum[i])
