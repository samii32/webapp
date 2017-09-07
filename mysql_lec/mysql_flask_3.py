import MySQLdb
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
	db = MySQLdb.connect('localhost','root','1111','raspberry')
	cur = db.cursor()
        sql = "select id, name, phone from mysql_test"
        cur.execute(sql)
        rs = cur.fetchall()

        cur.close()
        db.close()
        return render_template('select_id.html',data=rs)

@app.route('/GET/ID/<string:id>')
def get_id(id):
	db = MySQLdb.connect('localhost','root','1111','raspberry')
	cur = db.cursor()
        sql = "select id, name, phone from mysql_test where id = '%s'" % id
        cur.execute(sql)
        rs = cur.fetchall()

        cur.close()
        db.close()
        return render_template('select_id.html',data=rs)


@app.route('/POST/<string:id>/<string:name>')
def insert_id(id,name):
        db = MySQLdb.connect('localhost','root','1111','raspberry')
        cur = db.cursor()
        sql = "insert into mysql_test values('%s','%s','010-0000')" %(id ,name)

	try:
	        cur.execute(sql)
		db.commit()
	except:
		db.rollback()

	cur.close()
        db.close()
        return index()

@app.route('/PUT/<string:id>')
def update_id(id):
        db = MySQLdb.connect('localhost','root','1111','raspberry')
        cur = db.cursor()
        sql = "update mysql_test set id ='sami' where id ='%s'" %id

        try:
                cur.execute(sql)
                db.commit()
        except:
                db.rollback()

	cur.close()
        db.close()
        return index()

@app.route('/DELETE/<string:id>')
def delete_id(id):
        db = MySQLdb.connect('localhost','root','1111','raspberry')
        cur = db.cursor()
        sql = "delete from mysql_test where id='%s'" %id

        try:
                cur.execute(sql)
                db.commit()
        except:
                db.rollback()


        cur.close()
        db.close()
        return index()


if __name__ == "__main__":
	app.run(debug = True, host='0.0.0.0', port = 8888)

