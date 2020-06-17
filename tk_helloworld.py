# Tkinterライブラリをインポート
import tkinter as tk

# メインウィンドウの生成
root = tk.Tk()

# ラベルの生成
label = tk.Label(root, text="Hello World")

# ラベルを配置
label.pack()

root.mainloop()