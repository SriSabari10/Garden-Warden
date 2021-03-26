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