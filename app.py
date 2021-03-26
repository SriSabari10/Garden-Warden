from flask import Flask,render_template,request
from flask_mysqldb import MySQL
app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'srisabari@%'
app.config['MYSQL_PASSWORD'] = 'sabaharibala'
app.config['MYSQL_DB'] = 'mysql'

mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/abc',methods=['GET','POST'])
def signup():
     if request.method == "POST":
         Username = request.form['u_name']
         Password = request.form['u_pass']
         cur = mysql.connection.cursor()
         cur.execute("INSERT INTO MyUsers(Username, Password) VALUES (%s, %s)", (Username, Password))
         mysql.connection.commit()
         cur.close()
         return 'success'
     return render_template('testing.html')

@app.route('/bcd',methods=['GET','POST'])
def login():
    return render_template('Drop.html')

if __name__ == "__main__":
    app.run(debug=True)