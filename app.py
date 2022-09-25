from flask import Flask, render_template, request
from flask_mysqldb import MySQL 
import yaml
app = Flask(__name__)

db = yaml.load(open('db.yaml'))
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_DB'] = db['mysql_db']
app.config['MYSQL_PASSWORD'] = db['mysql_password']

mysql = MySQL(app)
@app.route("/", methods=['GET'])
def HomePage():
    if request.method == "GET":
        return render_template("index.html")


@app.route("/entry", methods=['GET', 'POST'])
def Entry():
    if request.method == "GET":
        return render_template("entry.html")
    if request.method == 'POST':
        # fetch from data
        carDetails = request.form
        Reg_no = carDetails['Reg_num']
        Color = carDetails['Color']
        PersonID = carDetails['PersonID']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO Cars(Reg_num, Color, PersonID) VALUES(%s, %s, %s)", (Reg_no, Color, PersonID))
        mysql.connection.commit()
        cur.close()
        return 'sucess'

if __name__ == '__main__':
    app.run(debug=True)

    