import datetime

dt = datetime.datetime.now()

print("Content-type: text/html; charset=UTF-8")
print()
print("<html>")
print("<body>")
print("現在は", dt, "です。<br>")
print("年:", dt.year, "<br>")
print("月:", dt.month, "<br>")
print("日:", dt.date, "<br>")
print("successfully!<br>")
print("</body>")
print("</html>")