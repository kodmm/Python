try:
    f = open("sample3.py", "r")

except FileNotFoundError:
    print("ファイルを開けなかったよ")

else:
    lines = f.readlines()
    for line in lines:
        print(line, end="") # end="" 改行なし
    f.close()

finally:
    print("処理を終了します。")