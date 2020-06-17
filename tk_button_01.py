# Tkinterライブラリのインポート
import tkinter as tk

# メインウィンドウの生成
root = tk.Tk()

# ボタンが押されたときの処理
def func():
    print("Pushed")

#ボタンの生成
button = tk.Button(root, text="Push!", command=func)

#ボタンを配置
button.pack()

# mainloopの実行
root.mainloop()