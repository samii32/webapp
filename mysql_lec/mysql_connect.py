import MySQLdb

db = MySQLdb.connect('localhost','root','1111','raspberry')
cur = db.cursor()
sql = "insert into mysql_test(id,name,phone) value('ssar4','jooh4','010-5555')"

try:
	cur.execute(sql)
	db.commit()

except:
	db.rollback()

cur.close()
db.close()
