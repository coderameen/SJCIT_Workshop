from flask import Flask,render_template,redirect,request
from database import conn,cursor
#initilize app
app = Flask(__name__)

@app.route("/")
def home():
    res = cursor.execute('''SELECT * FROM employees''')
    res = res.fetchall()
    return render_template('index.html', res = res)

@app.route("/add")
def add():
    return render_template('add.html')

@app.route("/adddb", methods=['GET','POST'])
def adddb():
    if request.method == 'POST':
        empid = request.form['empid']
        name = request.form['name']
        designation = request.form['designation']
        # print([empid,name,designation])
        cursor.execute('''INSERT INTO employees(empid,name,designation) VALUES(?,?,?)''',(empid,name,designation))
        conn.commit()
        print("Employee inserted successfully!!")
        
        return redirect("/")
    
    
@app.route("/edit/<id>")
def edit(id):
    res = cursor.execute('''SELECT * FROM employees WHERE empid=?''',(id,))
    res = res.fetchone()
    return render_template('edit.html',res=res)


@app.route('/editdb', methods=['GET','POST'])
def editdb():
    if request.method == 'POST':
        empid = request.form['empid']
        name = request.form['name']
        designation = request.form['designation']
        cursor.execute('''UPDATE employees SET name=?,designation=? WHERE empid=?''',(name,designation,empid))
        conn.commit()
        return redirect("/")
    
@app.route("/delete/<id>")
def delete(id):
    cursor.execute('''DELETE FROM employees WHERE empid=?''',(id,))
    conn.commit()
    return redirect("/")
if __name__=='__main__':
    app.run(debug=True)