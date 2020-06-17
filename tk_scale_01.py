import tkinter as tk

root = tk.Tk()

# スライドバーの値を格納する場所を生成
val = tk.IntVar()
# varに0を代入
val.set(0)

#スライドバーを動かしたときの処理
def func(scl):
    #ラベルの表示を変更
    label.config(text = 'Value = %d' % int(scl))

#スライドバーの値を表示するラベルを生成
label = tk.Label(root, text = 'Value = %d' % val.get())
label.pack()

#スライドバーの作成
s = tk.Scale(root, label='Scale', orient = 'h', from_ = 0, to = 100, showvalue = False, variable = val, command = func)

s.pack()

#終了ボタン
def finish_func():
    root.quit()

botton = tk.Button(root, text="finish", command = finish_func)
botton.pack()
root.mainloop()