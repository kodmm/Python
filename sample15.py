data =[
    ["tokyo", 32, 25],
    ["osaka", 23, 21],
    ["nagoya", 27, 20],
    ["kyoto", 26, 19],
    ["fukuoka", 27, 22]
]
print(data)

for dat in data:
    print(dat)
    for d in dat:
        print(d, end="\t")
    print()
print(data[0][0], "の最高気温は", data[0][1], "最低気温は", data[0][2], "です。")
