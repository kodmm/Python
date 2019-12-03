import csv

fd = open('KEN_ALL_1.csv')
csv_f = csv.reader(fd)
it = iter(csv_f)
bango = next(it)
ken = next(it)
chiho = next(it)
menseki = next(it)
jinko = next(it)
print(bango)
print(ken)
print(chiho)
print(menseki)
print(jinko)

Menseki = [int(c) for c in menseki]
Jinko = [int(x)for x in jinko]
for c in zip(bango, ken):
    print(c)


menseki_max = Menseki.index(max(Menseki))
# print(max(Menseki))
print("面積が最大の都道府県")
print(ken[menseki_max])

menseki_min = Menseki.index(min(Menseki))
print("面積が最小の都道府県")
print(ken[menseki_min])

jinko_max = Jinko.index(max(Jinko))
print("人口が最大の都道府県")
print(ken[jinko_max])

jinko_min = Jinko.index(min(Jinko))
print("人口が最小の都道府県")
print(ken[jinko_min])

Density = []
for i in range(len(Jinko)):
    P_Density = Jinko[i] / Menseki[i]
    Density.append(P_Density)
print(Density)


Density_max = Density.index(max(Density))
print("人口密度が最大の都道府県")
print(ken[Density_max])

Density_min = Density.index(min(Density))
print("人口密度が最小の都道府県")
print(ken[Density_min])

Region_PH_sum = 0
Region_PT_sum = 0
Region_PK_sum = 0
Region_PC_sum = 0
Region_Pkinki_sum = 0
Region_PS_sum = 0
Region_PO_sum = 0
for i in range(len(Jinko)):
    if '北海道' == chiho[i]:
        Region_PH_sum = Region_PH_sum + Jinko[i]
    elif '東北' == chiho[i]:
        Region_PT_sum = Region_PT_sum + Jinko[i]
    elif '関東' == chiho[i]:
        Region_PK_sum = Region_PK_sum + Jinko[i]
    elif '中部' == chiho[i]:
        Region_PC_sum = Region_PC_sum + Jinko[i]
    elif '近畿' == chiho[i]:
        Region_Pkinki_sum = Region_Pkinki_sum + Jinko[i]
    elif '四国' == chiho[i]:
        Region_PS_sum = Region_PS_sum + Jinko[i]
    else:
        Region_PO_sum = Region_PO_sum + Jinko[i]
print("地方ごとの総人口")
print('北海道:', Region_PH_sum)
print('東北:', Region_PT_sum)
print('関東:', Region_PK_sum)
print('中部:', Region_PC_sum)
print('近畿:', Region_Pkinki_sum)
print('四国:', Region_PS_sum)
print('九州・沖縄:', Region_PO_sum)

Region_PHH_sum = 0
Region_PTT_sum = 0
Region_PKK_sum = 0
Region_PCC_sum = 0
Region_PkinkiI_sum = 0
Region_PSS_sum = 0
Region_POO_sum = 0
for i in range(len(Menseki)):
    if '北海道' == chiho[i]:
        Region_PHH_sum = Region_PHH_sum + Menseki[i]
    elif '東北' == chiho[i]:
        Region_PTT_sum = Region_PTT_sum + Menseki[i]
    elif '関東' == chiho[i]:
        Region_PKK_sum = Region_PKK_sum + Menseki[i]
    elif '中部' == chiho[i]:
        Region_PCC_sum = Region_PCC_sum + Menseki[i]
    elif '近畿' == chiho[i]:
        Region_PkinkiI_sum = Region_PkinkiI_sum + Menseki[i]
    elif '四国' == chiho[i]:
        Region_PSS_sum = Region_PSS_sum + Menseki[i]
    else:
        Region_POO_sum = Region_POO_sum + Menseki[i]
print("地方ごとの総面積")
print('北海道:', Region_PHH_sum)
print('東北:', Region_PTT_sum)
print('関東:', Region_PKK_sum)
print('中部:', Region_PCC_sum)
print('近畿:', Region_PkinkiI_sum)
print('四国:', Region_PSS_sum)
print('九州・沖縄:', Region_POO_sum)

for i in range(1):
    Region_PH_sum = Region_PH_sum / Region_PHH_sum * 1000
    Region_PT_sum = Region_PT_sum / Region_PTT_sum * 1000
    Region_PK_sum = Region_PK_sum / Region_PKK_sum * 1000
    Region_PC_sum = Region_PC_sum / Region_PCC_sum * 1000
    Region_Pkinki_sum = Region_Pkinki_sum / Region_PkinkiI_sum * 1000
    Region_PS_sum = Region_PS_sum / Region_PSS_sum * 1000
    Region_PO_sum = Region_PO_sum / Region_POO_sum * 1000

print("地方ごとの総人口密度")
print('北海道:', Region_PH_sum)
print('東北:', Region_PT_sum)
print('関東:', Region_PK_sum)
print('中部:', Region_PC_sum)
print('近畿:', Region_Pkinki_sum)
print('四国:', Region_PS_sum)
print('九州・沖縄:', Region_PO_sum)




