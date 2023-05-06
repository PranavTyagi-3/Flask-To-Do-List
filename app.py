from flask import Flask, render_template,request, session, redirect, url_for
import sqlite3 as sql
import random
import os

app = Flask(__name__)
app.secret_key='Hello World'
app.config['UPLOAD_FOLDER'] = 'static/uploads'

@app.route('/login',methods=("GET","POST"))
def login():
    session['user_id']=None
    if request.method=='POST':
        #try:
        conn=sql.connect('users.db')
        cur=conn.cursor()
        cur.execute('select * from user_info;')
        rows = cur.fetchall()
        
        print(rows)
        try:
            mailid=request.form['id']
            password=request.form['pass']
            print(mailid)
            print(password)
        except:
            new_id=request.form['sign_id']
            new_pass=request.form['sign_pass']
            mailid=""
            password=""

        if len(mailid)!=0:
            
            if (mailid,password) in [ i[1:] for i in rows]:

                cur.execute("select id from user_info where user_id=?",(mailid,))
                session['user_id'] = cur.fetchall()[0][0]
                conn.close()
                return redirect(url_for('home'))
            else:
                conn.close()
                return render_template('login.html',message="Wrong Id or Password")

        elif len(new_id)!=0:
            while True:
                c_id = random.randint(1000,9999)
                if c_id not in [i[0] for i in rows]:
                    break
            if new_id in [i[1] for i in rows]:
                conn.close()
                return render_template('login.html',message='User Id Already Exists')
            else:
                conn.execute('insert into user_info values(?,?,?)',(c_id,new_id,new_pass))
                conn.commit()
                conn.close()
                session['user_id'] = c_id
                return redirect(url_for('home'))
        #except:
            #return ("<h1> Some Error Occured, please try later </h1>")
    
    return render_template('login.html')

@app.route('/home',methods=("GET","POST"))
def home():
    user_id = session.get('user_id')

    if user_id is None:
        return redirect(url_for('login'))

    if request.method=='POST':
        heading = request.form['heading']
        desc = request.form['desc']
        date = request.form['date']

        try:
            f=request.files['file']
            file_name=user_id+f.filename
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], file_name))
        except:
            file_name=''
        conn=sql.connect('users.db')
        cur=conn.cursor()
        if file_name!='':
            cur.execute(f'insert into todo values(?,?,?,?,?);',(user_id,heading,desc,date,file_name))
        else:
            cur.execute(f'insert into todo(id,task_heading,task_desc,task_date) values(?,?,?,?);',(user_id,heading,desc,date))
        conn.commit()
        conn.close()
    
    
    
    conn=sql.connect('users.db')
    cur = conn.cursor()
    cur.execute("select * from todo where id=?;",(user_id,))
    tasks=cur.fetchall()
    print(tasks)
    conn.close()
    return render_template('index.html',tasks=tasks,id=user_id)

@app.route('/delete/<heading>/<desc>')
def delete(heading,desc):
    desc = desc.replace("_"," ")
    conn=sql.connect('users.db')
    cur = conn.cursor()
    cur.execute('delete from todo where task_heading=? and task_desc=?',(heading,desc))
    conn.commit()
    conn.close()
    return redirect(url_for('home'))

if __name__=='__main__':
    app.run(debug=True)
