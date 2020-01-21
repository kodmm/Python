import mysql.connector
nn = mysql.connector.connect(user="root", password="root", host="localhost",database="dokoQL")
c = conn.cursor()
c.execute("DROP TABLE IF EXISTS product")
c.execute("CREATE TABLE product(name CHAR(20), price INT)")
c.execute("INSERT INTO product VALUES('鉛筆', 80)")
c.execute("INSERT INTO product VALUES('消しゴム', 100)")