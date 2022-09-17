from flask import Flask, render_template, request
from flask_mysqldb import MySQL 
import yaml
app = Flask(__name__)

db = yaml.load(open('db.yaml'))
app.config['MYSQL_HOST'] = db['mysql_hsot']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_DB'] = db['mysql_db']
app.config['MYSQL_PASSWORD'] = db['mysql_password']


@app.route("/", methods=['GET', 'POSTS'])
def HomePage():
    if method.request == 'POST':
        # fetch from data
        carDetails = requst.form
        plate = carDetails['plate']
        name = carDetails['name']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO car(plat, name) VALUES(%s, %s)", (plate, name))
        mysql.connection.commit()
        cur.close()
        return 'sucess'
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)