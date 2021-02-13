from flask import Flask, render_template, jsonify
from flaskext.mysql import MySQL
import pymysql
import json

app = Flask(__name__)

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '*****'
app.config['MYSQL_DATABASE_DB'] = 'productes_general'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
conn = mysql.connect()
cursor =conn.cursor()

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/api_products')
def products():
	json_productes = []
	cursor.execute("SELECT id,referencia,nom,preu,iva FROM productes_general.productes")
	data=cursor.fetchall()
	for pr in data:
		json_productes.append({"id":pr[0],"referencia":pr[1],"nom":pr[2],"preu":str(pr[3]),"iva":str(pr[4])})

	return json.dumps({'data':json_productes})

@app.route('/taula')
def taula():
	return render_template("taula.html")
