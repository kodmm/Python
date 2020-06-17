import tkinter as tk    

root = tk.Tk()

def push_func():
    vm = hex(int(e.get()))
    label_2.config(text = vm)
    e.delete(0, tk.END)


label_1 = tk.Label(root, text="10 -> 16進変換")
label_1.pack()

vm = tk.IntVar()

label_2 = tk.Label(root, text="Value %d" % vm.get())
label_2.pack()

e = tk.Entry(root, textvariable = vm)
e.delete(0, tk.END)
e.pack()

button = tk.Button(root, text="変換", command = push_func)
button.pack()
root.mainloop()
