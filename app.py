from flask import Flask,render_template,request
from flask_mysqldb import MySQL
app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'MyDB'

mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        details = request.form
        Username = details['u_name']
        Password = details['u_pass']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO MyUsers(Username, Password) VALUES (%s, %s)", (Username, Password))
        mysql.connection.commit()
        cur.close()
        return 'success'
    return render_template('index.html')
@app.route('/abc')
def testing():
    return render_template('testing.html')
if __name__ == "__main__":
    app.run(debug=True)