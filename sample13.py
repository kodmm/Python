city =["tokyo", "kyoto", "nagoya", "osaka"]
sale = [80, 60, 22, 50, 75]

print(city)
print(sale)

# データの組み合わせ
for d in zip(city, sale):
    print(d)

# データの分解
for c, s in zip(city, sale):
    print(c, d)
