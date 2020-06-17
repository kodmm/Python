import tkinter as tk 

root = tk.Tk()

def func():
    root.quit()


button = tk.Button(root, text="button", command = func)
button.pack()

val = tk.StringVar()
val.set("hoge")
label = tk.Label(root, text = "Label %s" % val.get())
label.pack()
#リターンが押されたときの動作
def push_func(ev):
    label.config(text = e.get())

#テキストボックスを生成
e = tk.Entry(root)
e.pack()
#テキストボックスにリターンキーが押下されたときのイベントを追加
e.bind('<Return>',push_func)

root.mainloop()
