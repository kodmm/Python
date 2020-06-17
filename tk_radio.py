import tkinter as tk  

root = tk.Tk()

def func():
    root.quit()

def release_func(ev):
    button.config(text = "終了")

button = tk.Button(root, text="push", command=func)
button.bind('<Enter>', release_func)
button.pack()

#ラジオボタンの値を格納する場所を生成
sel = tk.StringVar()
#selに1を代入　
sel.set("hoge")

label = tk.Label(root, textvariable=sel)

label.pack()

def func_button():
    print(sel.get())

#ラジオボタン1の生成
rb1 = tk.Radiobutton(root, text="ボタン1", variable = sel, value = "ボタン1", command = func_button)

#ラジオボタン1を配置
rb1.pack()

#ラジオボタン2の生成
rb2 = tk.Radiobutton(root, text="ボタン2", variable = sel, value = "ボタン2", command = func_button)

#ラジオボタン2の配置
rb2.pack()





root.mainloop()