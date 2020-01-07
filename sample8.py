def append():
    print("データを追加")

def update():
    print("datachage")

def delete():
    print("datadelete")

list = [append, update, delete]

res = int(input("操作番号を入力してください。(0~2)"))

if 0 <= res and res < len(list):
    list[res]()
