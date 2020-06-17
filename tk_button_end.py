#Tkinterライブラリのインポート
import tkinter as tk 

# メインウィンドウの生成
root = tk.Tk()

# ラベルの生成
label = tk.Label(root, text="サンプル")

# ラベルの配置
label.pack()



# ボタンの生成
button = tk.Button(root, text="終了", command=root.quit)



#ボタンを配置
button.pack()

#mainloopの実行
root.mainloop()