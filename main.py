from flask import *
from mysql.connector import *

a=connect(host="localhost",user="root",password="niveselva1996")
c=a.cursor()

#c.execute("create database if not exists visitor")
a=connect(host="localhost",user="root",password="niveselva1996",db="visitor")
c=a.cursor()

#c.execute("create table record (Visitor_Name varchar(30),Visitor_location varchar(30),Visitor_Mobile_No bigint)")
a.commit()

myapp = Flask(__name__)
myapp.secret_key="nive96"

@myapp.route('/')
def content():
    c.execute("SELECT * FROM record")
    visitors = c.fetchall()
    return render_template('Visitor.record.html',visitors=visitors)

@myapp.route('/add_visitor', methods=['POST','GET'])
def add_visitor():
    if request.method == "POST":
        l = request.form["name"]
        m = request.form["location"]
        n = request.form["phone"]
        c.execute("insert into record values (%s,%s,%s)", (l, m, n))
        a.commit()
        return redirect(url_for('content'))
    else:
        return "Wrong Input"

myapp.run(port=5053, debug=True)
