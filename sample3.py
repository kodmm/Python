def sell(place, price, num):
    print(place, "支店で", num, "者に", price, "万円の販売が行われた")
    tt = price * num
    return tt

ymd = sell("東京", 100, 5)

print(ymd)

def sell():
    y = 2018
    m = 10
    d = 1
    print(y, "年", m, "月", d, "日")
    return y, m, d

a, i, u = sell()
print(a, i, u)