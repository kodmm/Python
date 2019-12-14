import csv

fd = open('KEN_ALL_1.csv')
csv_f = csv.reader(fd)
it = iter(csv_f)
bango = next(it)
ken = next(it)
chiho = next(it)
menseki = next(it)
jinko = next(it)
# print(bango)
# print(ken)
# print(chiho)
# print(menseki)
# print(jinko)

Bango = [int(c) for c in bango]
Menseki = [int(c) for c in menseki]
def menseki(prefectures, menseki, juni):
    Bango_Menseki = dict(zip(prefectures, menseki))
    MENSEKI = sorted(Bango_Menseki.items(), key=lambda x:x[1], reverse = True)
    

    # print(MENSEKI)
    print(MENSEKI[juni - 1])

    
    return Bango_Menseki.keys[i], MENSEKI[juni]

juni = int(input("順位は？"))
menseki(ken, Menseki, juni)


