from flask import Flask, render_template, request
from flask_mysqldb import MySQL 
from datetime import datetime

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
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM Vehicles")
        vehicles = cur.fetchall()
        return render_template("index.html", vehicles = vehicles)


@app.route("/entry", methods=['GET', 'POST'])
def Entry():
    if request.method == "GET":
        return render_template("entry.html")
    if request.method == 'POST':
        # fetch from data
        carDetails = request.form
        Reg_num = carDetails['Reg_num']
        Owner_ID = carDetails['Owner_ID']
        Model_name = carDetails['Model_name']
        Color = carDetails['Color']
        V_Type = carDetails['V_Type']
        Entry_time = datetime.now()
        sql.connection.cursor()
        cur.execute("INSERT INTO Vehicles(Reg_num, Owner_ID, Model_name, Color, V_Type, Entry_time) VALUES(%s, %s, %s, %s, %s, %s)", 
        (Reg_num,Owner_ID,Model_name,Color,V_Type, Entry_time))
        mysql.connection.commit()
        cur.close()
        return "Sucess"
    

def BillCalculator(entry_time):
    exit_time = datetime.now()
    diff_year =  (exit_time.date().year - entry_time.date().year)*365
    diff_month = (exit_time.date().month - entry_time.date().month)*30
    diff_day = (exit_time.date().day - entry_time.date().day)
    total_date = diff_year + diff_month + diff_day
    
    diff_hour =  (exit_time.time().hour - entry_time.time().hour)*60
    diff_min = (exit_time.time().minute - entry_time.time().minute)*1/60
    total_min = total_date*24*60 + diff_hour + diff_min
    total_bill = 1/6 * total_min
    return total_min


def BillHandler(Reg_Num):
    cur = mysql.connection.cursor()
    cur.execute("SELECT Owner_ID, Entry_time FROM Vehicles WHERE Reg_Num = %s", [Reg_Num])
    car = cur.fetchall()
    mysql.connection.commit()
    cur.close()
    owner_id = car[0][0]
    entry_time = car[0][1]
    total_amount = BillCalculator(entry_time)
    cur = mysql.connection.cursor()
    cur.execute("UPDATE Customers SET Bill_Amount = Bill_Amount + %s WHERE Customer_ID = %s", (total_amount, owner_id))
    mysql.connection.commit()
    cur.close()

@app.route("/exit", methods=['GET', 'POST'])
def Exit():
    if request.method == "POST":
        carDetails = request.form
        Reg_num = carDetails['Reg_num']
        cur = mysql.connection.cursor()
        BillHandler(Reg_num)
        # cur.execute("DELETE FROM Vehicles WHERE Reg_num = %s", [Reg_num])
        mysql.connection.commit()
        cur.close()
        return "Delete sucess"
    if request.method == "GET":
        return render_template("exit.html")
    


if __name__ == '__main__':
    app.run(debug=True)

    