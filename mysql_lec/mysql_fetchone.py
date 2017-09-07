import MySQLdb

db = MySQLdb.connect('localhost','root','1111','raspberry')
cur = db.cursor()
sql = "select id, name, phone from mysql_test"
cur.execute(sql)

rs = cur.fetchall()
result = []

for i in rs:
	result.append(i)

iterator = iter(result)
for item in iterator:
	print next(item), type(item)


cur.close()
db.close()
