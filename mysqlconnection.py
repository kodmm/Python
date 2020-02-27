import mysql.connector
nn = mysql.connector.connect(user="root", password="root", host="localhost",database="dokoQL")
c = nn.cursor()
c.execute("DROP TABLE IF EXISTS product")
c.execute("CREATE TABLE product(name CHAR(20), price INT)")
c.execute("INSERT INTO product VALUES('鉛筆', 80)")
c.execute("INSERT INTO product VALUES('消しゴム', 100)")


nn.commit()
c.execute("SELECT * FROM product")

for row in c.fetchall():
    print(row)


ul = int(input("hoge"))
li = int(input("hogehoge"))

c.execute("SELECT * FROM product WHERE price BETWEEN %s AND %s" ,[ul, li])
for row in c.fetchall():
    print(row)
nn.close()
