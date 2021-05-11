from flask import Flask,render_template,request,session,redirect,url_for,flash
import sqlite3 as sql
import requests
import bcrypt
from passlib.hash import sha256_crypt
from flask_mail import Mail
import hashlib
import datetime
app = Flask(__name__)
mail = Mail(app)
app.config['SECRET_KEY'] = 'sabaharibala2818'
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
         upass=request.form['u_pass']

         with sql.connect("mydatabase.db") as con:
            cur = con.cursor()
            
            cur.execute("INSERT INTO mySignup (name,age,location,email,password) VALUES (?,?,?,?,?)",(uname,uage,uloc,uemail,upass) )
            
            con.commit()
            msg = "Record successfully added" 
            
            
      except:
         con.rollback()
         msg = "Error in inserting"
      
      finally:
         con.close()
         return render_template("result.html",msg = msg)
         
@app.route('/login',methods=['GET','POST'])
def login():
    # if request.method == 'POST':
    #   try:
    #      print(request.form)
    #      uemail = request.form['u_email']
    #      upass=request.form['u_pass']

    #      with sql.connect("mydatabase.db") as con:
           
    #        cur = con.cursor()
    #        cur.execute("select * from mySignup where email=? & password=?",(uemail,upass))
    #        con.commit()
    #        msg1 ="Hi"
    #   except:
    #      con.rollback()
    #      msg = "Hello"

    #   finally:
    #         con.close()
    #         if(msg1 == 'Hi') 
              uemail = request.form['u_email']
              print(request.form)
              session['emailid']=uemail
              return render_template('testing2.html')

@app.route('/email',methods=['GET','POST'])
def send_simple_message():
    userName = session['emailid']
    plantName = session['plant']
    value = requests.post(
        "https://api.mailgun.net/v3/sandboxd9e1ae88ae5e4dab9f8704ad7783d00e.mailgun.org/messages",
        auth=("api", "2a6c8831dd190e35b7755626f18c9b4a-2a9a428a-2f6444a8"),
        data={"from": "Garden Warden <postmaster@sandboxd9e1ae88ae5e4dab9f8704ad7783d00e.mailgun.org>",
              "to": [userName],
              "subject": "Descriptions",
              "text": "You provided that your leaf is in Brown color.First you want check that your plant is getting efficient sunlight and also you to water the plants as mentioned."})
    print(value)
    flash('You have successfully Subscribed')
    return redirect(url_for(plantName))

@app.route('/cmail',methods=['GET','POST'])
def cmail():
    return render_template(
        'mail.html')

@app.route('/chill',methods=['GET','POST'])
def chill():
    session['plant']="chill"
    return render_template(
        'chill.html')

@app.route('/tom',methods=['GET','POST'])
def tomato():
    session['plant']="tomato"
    return render_template(
        'tom.html')

@app.route('/brinj',methods=['GET','POST'])
def brinjal():
    session['plant']="brinjal"
    return render_template(
        'brinj.html')

@app.route('/coria',methods=['GET','POST'])
def coriander():
    session['plant']="coriander"
    return render_template(
        'coria.html')

@app.route('/bitt',methods=['GET','POST'])
def bittergaurd():
    session['plant']="bittergaurd"
    return render_template(
        'bitt.html')

@app.route('/cucu',methods=['GET','POST'])
def cucumber():
    session['plant']="cucumber"
    return render_template(
        'cucu.html')

@app.route('/mint',methods=['GET','POST'])
def mint():
    session['plant']="mint"
    return render_template(
        'mint.html')

@app.route('/spin',methods=['GET','POST'])
def spinach():
    session['plant']="spinach"
    return render_template(
        'spin.html')

@app.route('/radd',methods=['GET','POST'])
def raddish():
    session['plant']="raddish"
    return render_template(
        'radd.html')

@app.route('/caps',methods=['GET','POST'])
def caspsicum():
    session['plant']="capsicum"
    return render_template(
        'caps.html')

if __name__ == "__main__":
    app.run(debug=True)