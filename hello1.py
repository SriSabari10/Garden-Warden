from flask import Flask,render_template,request
import sqlite3 as sql
import requests
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    return render_template('testing.html')

@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
   if request.method == 'POST':
      try:
         print(request.form)
         uname = request.form['u_name']
         uage = request.form['u_age']
         uloc = request.form['u_loc']
         uemail = request.form['u_email']
         upass = request.form['u_pass']
         
         with sql.connect("newRegister.db") as con:
            cur = con.cursor()
            
            cur.execute("INSERT INTO newSignup (name,age,location,email,password) VALUES (?,?,?,?,?)",(uname,uage,uloc,uemail,upass) )
            
            con.commit()
            msg = "Record successfully added" 
            
            
      except:
         con.rollback()
         msg = "error in insert operation"
      
      finally:
         con.close()
         return render_template("result.html",msg = msg)

@app.route('/login',methods=['GET','POST'])
def login():
    return render_template('testing2.html')

if __name__ == "__main__":
    app.run(debug=True)